import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).

    Args:
        uploaded_file: The uploaded PDF file object.

    Returns:
        str: The extracted text from the PDF.
    """
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    pdf_document.close()
    return text