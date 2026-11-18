import streamlit as st
from pypdf import PdfReader
import base64
import io



st.set_page_config(
    page_title="PDF viewer | Regent Business School",
    page_icon="📈",
    layout="wide"
)



st.title("📄 PDF Reader and Viewer")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    # Display PDF
    st.subheader("📖 PDF Viewer")

    pdf_bytes = uploaded_file.getvalue()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="600"
        type="application/pdf">
    </iframe>
    """

    st.components.v1.html(pdf_display, height=620)

    # Read PDF
    pdf = PdfReader(io.BytesIO(pdf_bytes))

    st.subheader("📊 PDF Information")
    st.write("Filename:", uploaded_file.name)
    st.write("Number of pages:", len(pdf.pages))

    # Extract text
    st.subheader("📝 Extracted Text")

    page_number = st.selectbox(
        "Select page",
        range(1, len(pdf.pages) + 1)
    )

    text = pdf.pages[page_number - 1].extract_text()

    st.text_area("Page Text", text or "No text found", height=300)
