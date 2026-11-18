
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Masterclass 4 | Regent Business School",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📊 Masterclass 4")
st.sidebar.markdown("**Regent Business School**")

st.sidebar.divider()

st.sidebar.info(
    "Navigate between the course homepage and "
    "the interactive Retail Data Analytics (EDA) page "
    "using the page links above."
)

st.sidebar.divider()

st.sidebar.caption(
    "Introduction to Big Data Analytics "
    "& Consumer Behaviour"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Masterclass 4")

st.subheader(
    "Introduction to Big Data Analytics "
    "and Understanding Consumer Behaviour (ADM)"
)

st.divider()

# --------------------------------------------------
# Course resources
# --------------------------------------------------

st.header("📂 Course Resources")

st.write(
    "Download files"
)

st.link_button(
    "📥 Download sales.xlsx",
    "https://drive.google.com/uc?export=download&id=1sAg6WH2A0CWqXJqk2mmrA27l8FUkLjFY",
    use_container_width=True
)

st.link_button(
    "📥 Download sales_notebook.ipynb",
    "https://drive.google.com/uc?export=download&id=1DJbvxhahDVEUfdIbWrs-t01SZuzIlECr",
    use_container_width=True
)

st.link_button(
    "📥 Download Python_Retail_Intro.ipynb",
    "https://drive.google.com/uc?export=download&id=1gUrIeC6pPhOIE-UksH2ZZQQZd6RNbHt7",
    use_container_width=True
)

st.link_button(
    "📥 Download retail_sales_messy.xlsx",
    "https://drive.google.com/uc?export=download&id=1IP33Q_vjPmHR8VJm0tObE1YS3PnEvQ36",
    use_container_width=True
)

st.link_button(
    "📥 Download retail_sales_cleaned.xlsx",
    "https://drive.google.com/uc?export=download&id=1GLoT5jCYWqXk93M_zt1GDSxps_jXEEaQ",
    use_container_width=True
)

#st.link_button(
#    "📥 Download retail_sales_2026.xlsx",
#    "https://drive.google.com/uc?export=download&id=1IhFQNzk7m9VWd8pcB31aiQtS7D7LDqht",
#    use_container_width=True
#)

st.link_button(
    "📥 Download Retail Sales 2026 (CSV)",
    "https://drive.google.com/uc?export=download&id=1jtvTcmR6bMXjHpmcXyaFjPSHPVJM732r",
    use_container_width=True
)

st.link_button(
    "📂 Open Resources",
    "https://drive.google.com/drive/folders/1OwNcr-S-oPfuuxNjBgiUAdVxvL2QBl0Y?usp=sharing",
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# JupyterLab
# --------------------------------------------------

st.subheader("🐍 Try JupyterLab")

st.write(
    "Use JupyterLab to practise Python programming "
    "and data analysis. Try it directly in your browser "
    "without installing anything, or download it for Windows."
)

st.link_button(
    "🌐 Try JupyterLab Online (No Installation)",
    "https://jupyter.org/try-jupyter/lab/",
    use_container_width=True
)

st.link_button(
    "💻 Download JupyterLab for Windows",
    "https://github.com/jupyterlab/jupyterlab-desktop/releases/download/v4.6.3-1/JupyterLab-Setup-Windows-x64.exe",
    use_container_width=True
)

st.caption(
    "💡 Beginners: Start with the online version. "
    "For offline use, install the Windows desktop version."
)

st.divider()

# --------------------------------------------------
# Streamlit analytics
# --------------------------------------------------

st.header("📈 Streamlit Resources")

st.link_button(
    "🚀 Open Streamlit",
    "https://streamlit.io/",
    use_container_width=True
)

st.link_button(
    "📥 Download Johannesburg Image (jozi.png)",
    "https://drive.google.com/uc?export=download&id=1h_3HUkYgOUTzlmKkxLzDoXycx11S2s9K",
    use_container_width=True
)

# --------------------------------------------------
# Interactive analytics
# --------------------------------------------------

st.header("💻 Retail Analytics Dashboard - Python Code")

st.write("Copy the Python code below to create your own retail dashboard.")

code = '''
import streamlit as st
import pandas as pd

st.title("Retail Analytics Dashboard")

file = st.file_uploader("Upload CSV", type="csv")

if file is None: st.stop()

df = pd.read_csv(file)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Statistics")
st.dataframe(df.describe())


st.subheader("Retail Dashboard")

st.metric("Total Revenue", df["Revenue_ZAR"].sum())

st.metric("Total Transactions", len(df))

st.metric("Items Sold", df["Quantity"].sum())

st.metric("Average Revenue", round(df["Revenue_ZAR"].mean(), 2))


st.subheader("Explore Your Data")

columns = st.multiselect("Select Columns", df.columns, default=df.columns)

category = st.selectbox("Select Category", df["Category"].unique())

filtered = df[df["Category"] == category]

st.dataframe(filtered[columns])


st.subheader("Retail Sales Charts")

# Bar chart - Revenue by Category
st.write("Revenue by Category")
sales = df.groupby("Category")["Revenue_ZAR"].sum()
st.bar_chart(sales)

# Line chart - Revenue by Date
st.write("Revenue Over Time")
sales = df.groupby("Date")["Revenue_ZAR"].sum()
st.line_chart(sales)

# Bar chart - Revenue by Store
st.write("Revenue by Store")
sales = df.groupby("Store")["Revenue_ZAR"].sum()
st.bar_chart(sales)

# Bar chart - Top 5 Products
st.write("Top 5 Products")
sales = df.groupby("Product")["Revenue_ZAR"].sum()
sales = sales.sort_values(ascending=False).head(5)
st.bar_chart(sales)

# Scatter chart - Quantity vs Revenue
st.write("Quantity vs Revenue")
st.scatter_chart(df, x="Quantity", y="Revenue_ZAR")
'''

st.code(code, language="python")


st.divider()

# --------------------------------------------------
# Additional resources
# --------------------------------------------------

st.header("🔗 Additional Resources")

resources = [("Quiz 1", "https://forms.gle/aMPVYc1kWD9Fa4og9")]

if resources:
    for name, url in resources:
        st.link_button(
            name,
            url,
            use_container_width=True
        )
else:
    st.info("Additional course resources will be added here.")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption(
    "Regent Business School | "
    "Masterclass 4 – Big Data Analytics & Consumer Behaviour"
)
