
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

st.markdown("**Regent Business School**")

st.divider()

st.write(
    "Welcome to the Masterclass 4 resource portal. "
    "Access course materials, practical datasets, "
    "Excel exercises and interactive data analytics tools."
)

# --------------------------------------------------
# Course resources
# --------------------------------------------------

st.header("📚 Course Resources")

st.markdown("### 1. Datasets & Excel Files")

st.write(
    "Download datasets, Excel workbooks and practical "
    "exercise files used during the masterclass."
)

st.link_button(
    "📂 Open Datasets & Excel Files",
    "https://drive.google.com/drive/folders/1OwNcr-S-oPfuuxNjBgiUAdVxvL2QBl0Y?usp=sharing",
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Interactive analytics
# --------------------------------------------------

st.header("📈 Interactive Data Analytics")

st.write(
    "Explore retail transaction datasets using our "
    "interactive Exploratory Data Analysis (EDA) dashboard."
)

st.markdown(
    """
    With the EDA dashboard you can:

    - Upload your own retail CSV dataset
    - Filter transactions by store, product, category and date
    - Explore sales, revenue, costs and profit
    - Generate interactive charts and graphs
    - View summary statistics
    - Sort, explore and download filtered datasets
    """
)

st.page_link(
    "pages/eda.py",
    label="📊 Open Retail Data Analytics Dashboard",
    icon="📈",
    use_container_width=True
)

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
