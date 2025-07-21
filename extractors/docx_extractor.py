# extractors/docx_extractor.py
from docx import Document

def extract_text_from_docx(docx_path):
    print("[INFO] Reading DOCX file...")
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])
