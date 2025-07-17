# resume_parser.py

import pdfplumber
from docx import Document
import os

def extract_text_from_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() or '' for page in pdf.pages)
        return text.strip()
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return ""

def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"Error parsing DOCX: {e}")
        return ""

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")

