# extractors/pdf_extractor.py
from pdf2image import convert_from_path
import pytesseract
from config import TESSERACT_PATH, POPLER_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path):
    print("[INFO] Converting PDF pages to images...")
    images = convert_from_path(pdf_path, poppler_path=POPLER_PATH)
    text = ""
    for i, img in enumerate(images):
        print(f"[INFO] Running OCR on page {i+1}")
        text += pytesseract.image_to_string(img)
    return text
