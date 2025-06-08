# fetch/pdf_reader.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts full text from a PDF using PyMuPDF.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        return f"[Error extracting PDF text] {e}"
