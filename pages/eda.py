
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Retail Data Analytics | Regent Business School",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Retail Data Analytics")
st.caption("Regent Business School | Masterclass 4")
st.write(
    "Upload a retail transactions CSV file to explore sales, "
    "customer behaviour, products, and store performance."
)

# --------------------------------------------------
# 1. Upload CSV
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Retail Transactions CSV",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload a CSV file to begin your analysis.")
    st.stop()

try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"Unable to read CSV: {e}")
    st.stop()

required_columns = [
    "Transaction_ID", "Date", "Customer_ID", "Store",
    "Product", "Category", "Quantity", "Unit_Price_ZAR",
    "Revenue_ZAR", "Unit_Cost_ZAR", "Promotion"
]

missing = [c for c in required_columns if c not in df.columns]

if missing:
    st.error(f"Missing required columns: {', '.join(missing)}")
    st.stop()

# --------------------------------------------------
# 2. Clean and prepare data
# --------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

numeric_columns = [
    "Quantity", "Unit_Price_ZAR",
    "Revenue_ZAR", "Unit_Cost_ZAR"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove invalid transaction records
original_count = len(df)

df = df.dropna(
    subset=["Date", "Quantity", "Revenue_ZAR", "Unit_Cost_ZAR"]
).copy()

if len(df) < original_count:
    st.warning(
        f"{original_count - len(df)} rows were excluded "
        "because of invalid dates or numeric values."
    )

if df.empty:
    st.error("No valid transaction records found.")
    st.stop()

# Derived metrics
df["Total_Cost_ZAR"] = df["Quantity"] * df["Unit_Cost_ZAR"]
df["Profit_ZAR"] = df["Revenue_ZAR"] - df["Total_Cost_ZAR"]

df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Day"] = df["Date"].dt.date

# --------------------------------------------------
# 3. Sidebar filters
# --------------------------------------------------

st.sidebar.header("🔎 Data Filters")

stores = st.sidebar.multiselect(
    "Store",
    sorted(df["Store"].dropna().unique()),
    default=sorted(df["Store"].dropna().unique())
)

categories = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].dropna().unique()),
    default=sorted(df["Category"].dropna().unique())
)

products = st.sidebar.multiselect(
    "Product",
    sorted(df["Product"].dropna().unique()),
    default=sorted(df["Product"].dropna().unique())
)

promotions = st.sidebar.multiselect(
    "Promotion",
    sorted(df["Promotion"].dropna().unique()),
    default=sorted(df["Promotion"].dropna().unique())
)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

revenue_min = float(df["Revenue_ZAR"].min())
revenue_max = float(df["Revenue_ZAR"].max())

if revenue_min < revenue_max:
    revenue_range = st.sidebar.slider(
        "Transaction Revenue (ZAR)",
        min_value=revenue_min,
        max_value=revenue_max,
        value=(revenue_min, revenue_max)
    )
else:
    revenue_range = (revenue_min, revenue_max)

# Apply filters
filtered = df[
    df["Store"].isin(stores)
    & df["Category"].isin(categories)
    & df["Product"].isin(products)
    & df["Promotion"].isin(promotions)
    & df["Revenue_ZAR"].between(*revenue_range)
].copy()

if len(date_range) == 2:
    filtered = filtered[
        filtered["Day"].between(date_range[0], date_range[1])
    ]

if filtered.empty:
    st.warning("No transactions match the selected filters.")
    st.stop()

# --------------------------------------------------
# 4. Summary statistics
# --------------------------------------------------

st.header("📊 Key Performance Indicators")

total_revenue = filtered["Revenue_ZAR"].sum()
total_profit = filtered["Profit_ZAR"].sum()
total_transactions = filtered["Transaction_ID"].nunique()
total_customers = filtered["Customer_ID"].nunique()
total_units = filtered["Quantity"].sum()

avg_transaction = (
    total_revenue / total_transactions
    if total_transactions else 0
)

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue else 0
)

c1, c2, c3 = st.columns(3)

c1.metric("Total Revenue", f"R {total_revenue:,.2f}")
c2.metric("Total Profit", f"R {total_profit:,.2f}")
c3.metric("Profit Margin", f"{profit_margin:.1f}%")

c4, c5, c6 = st.columns(3)

c4.metric("Transactions", f"{total_transactions:,}")
c5.metric("Unique Customers", f"{total_customers:,}")
c6.metric("Units Sold", f"{total_units:,.0f}")

st.metric(
    "Average Transaction Value",
    f"R {avg_transaction:,.2f}"
)

st.divider()

# --------------------------------------------------
# 5. Interactive charts
# --------------------------------------------------

st.header("📉 Interactive Visualisations")

metric_options = {
    "Revenue": "Revenue_ZAR",
    "Profit": "Profit_ZAR",
    "Quantity Sold": "Quantity",
    "Transaction Count": "Transaction_ID"
}

selected_metric = st.selectbox(
    "Choose a metric to analyse",
    list(metric_options.keys())
)

metric_col = metric_options[selected_metric]

def aggregate_data(data, group_column):
    if metric_col == "Transaction_ID":
        result = (
            data.groupby(group_column, as_index=False)
            .agg(Value=("Transaction_ID", "nunique"))
        )
    else:
        result = (
            data.groupby(group_column, as_index=False)
            .agg(Value=(metric_col, "sum"))
        )
    return result

tab1, tab2, tab3, tab4 = st.tabs([
    "Store Performance",
    "Products & Categories",
    "Sales Trends",
    "Promotions"
])

with tab1:
    st.subheader(f"{selected_metric} by Store")

    store_data = aggregate_data(filtered, "Store")
    store_data = store_data.sort_values("Value", ascending=False)

    fig = px.bar(
        store_data,
        x="Store",
        y="Value",
        color="Store",
        title=f"{selected_metric} by Store",
        text_auto=".2s"
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        category_data = aggregate_data(filtered, "Category")

        fig = px.pie(
            category_data,
            names="Category",
            values="Value",
            title=f"{selected_metric} by Category",
            hole=0.35
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        product_data = aggregate_data(filtered, "Product")
        product_data = product_data.sort_values(
            "Value", ascending=False
        ).head(10)

        fig = px.bar(
            product_data,
            x="Value",
            y="Product",
            orientation="h",
            title=f"Top 10 Products by {selected_metric}"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader(f"{selected_metric} Over Time")

    time_period = st.radio(
        "Group by",
        ["Daily", "Monthly"],
        horizontal=True
    )

    group_col = "Day" if time_period == "Daily" else "Month"

    trend_data = aggregate_data(filtered, group_col)
    trend_data = trend_data.sort_values(group_col)

    fig = px.line(
        trend_data,
        x=group_col,
        y="Value",
        markers=True,
        title=f"{selected_metric} - {time_period} Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Promotion Performance")

    promotion_data = aggregate_data(filtered, "Promotion")

    fig = px.bar(
        promotion_data,
        x="Promotion",
        y="Value",
        color="Promotion",
        title=f"{selected_metric}: Promotion vs No Promotion"
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# 6. Custom chart builder
# --------------------------------------------------

st.header("🛠️ Build Your Own Chart")

col1, col2, col3 = st.columns(3)

with col1:
    x_axis = st.selectbox(
        "Group Data By",
        ["Store", "Product", "Category", "Promotion", "Month"]
    )

with col2:
    chart_type = st.selectbox(
        "Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart"]
    )

with col3:
    custom_metric = st.selectbox(
        "Measure",
        list(metric_options.keys()),
        key="custom_metric"
    )

custom_col = metric_options[custom_metric]

if custom_col == "Transaction_ID":
    chart_data = (
        filtered.groupby(x_axis, as_index=False)
        .agg(Value=("Transaction_ID", "nunique"))
    )
else:
    chart_data = (
        filtered.groupby(x_axis, as_index=False)
        .agg(Value=(custom_col, "sum"))
    )

chart_data = chart_data.sort_values(x_axis)

if chart_type == "Bar Chart":
    fig = px.bar(
        chart_data,
        x=x_axis,
        y="Value",
        color=x_axis
    )
elif chart_type == "Line Chart":
    fig = px.line(
        chart_data,
        x=x_axis,
        y="Value",
        markers=True
    )
else:
    fig = px.pie(
        chart_data,
        names=x_axis,
        values="Value"
    )

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# 7. Data explorer with sorting
# --------------------------------------------------

st.header("📋 Explore Transaction Data")

sort_column = st.selectbox(
    "Sort By",
    [
        "Date", "Revenue_ZAR", "Profit_ZAR",
        "Quantity", "Store", "Product", "Category"
    ]
)

sort_order = st.radio(
    "Sort Order",
    ["Descending", "Ascending"],
    horizontal=True
)

filtered = filtered.sort_values(
    by=sort_column,
    ascending=(sort_order == "Ascending")
)

st.write(f"Showing {len(filtered):,} transaction rows")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# 8. Descriptive statistics
# --------------------------------------------------

with st.expander("📐 View Descriptive Statistics"):
    st.dataframe(
        filtered[numeric_columns + [
            "Total_Cost_ZAR", "Profit_ZAR"
        ]].describe(),
        use_container_width=True
    )

# --------------------------------------------------
# 9. Download filtered data
# --------------------------------------------------

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Filtered Dataset",
    data=csv,
    file_name="filtered_retail_data.csv",
    mime="text/csv"
)

st.caption(
    "Regent Business School | "
    "Masterclass 4 - Exploratory Data Analysis"
)
