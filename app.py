
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Masterclass 4 | Regent Business School",
    page_icon="📊",
    layout="centered"
)

# Header
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
    "Excel exercises and useful learning resources below."
)

# Course resources
st.header("📚 Course Resources")

st.markdown("### 1. Datasets & Excel Files")
st.write(
    "Download datasets, Excel workbooks and practical "
    "exercise files used during the masterclass."
)

st.link_button(
    "📂 Open Datasets & Excel Files",
    "https://drive.google.com/drive/folders/"
    "1CcdCCzo1oOxhlnUfVhiVQfM6eBUycUYQ?usp=drive_link",
    use_container_width=True
)

st.divider()

# Additional resources
st.header("🔗 Additional Resources")

resources = [
    # Add future links here:
    # ("Course Notes", "https://example.com"),
    # ("Python Notebooks", "https://example.com"),
]

if resources:
    for name, url in resources:
        st.link_button(name, url, use_container_width=True)
else:
    st.info("Additional course resources will be added here.")

st.divider()

st.caption(
    "Regent Business School | "
    "Masterclass 4 – Big Data Analytics & Consumer Behaviour"
)
