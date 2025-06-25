import os
from PyPDF2 import PdfReader
import docx

def extract_text(file_path):
    """
    Extracts text from supported document formats.
    Supported: .pdf, .docx, .txt
    Returns plain text or error message string.
    """
    if not os.path.exists(file_path):
        return f"Error: File does not exist - {file_path}"

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == '.pdf':
            return extract_from_pdf(file_path)
        elif ext in ['.docx', '.doc']:
            return extract_from_docx(file_path)
        elif ext == '.txt':
            return extract_from_txt(file_path)
        else:
            return f"❌ Unsupported file format: {ext}"
    except Exception as e:
        return f"❌ Error reading {file_path}: {str(e)}"

def extract_from_pdf(pdf_path):
    """Extract text from PDF using PyPDF2."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    except Exception as e:
        return f"❌ Failed to read PDF: {str(e)}"

    return text.strip()

def extract_from_docx(docx_path):
    """Extract text from DOCX using python-docx."""
    try:
        doc = docx.Document(docx_path)
        return '\n'.join(para.text for para in doc.paragraphs).strip()
    except Exception as e:
        return f"❌ Failed to read DOCX: {str(e)}"

def extract_from_txt(txt_path):
    """Read plain text from TXT file."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        return f"❌ Failed to read TXT: {str(e)}"
