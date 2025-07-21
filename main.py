
import os
import json
from extractors.pdf_extractor import extract_text_from_pdf
from extractors.docx_extractor import extract_text_from_docx
from parsers.ollama_parser import ollama_parse_resume

def process_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Please use PDF or DOCX.")

    print("[INFO] Parsing resume with Ollama...")
    parsed_data = ollama_parse_resume(text)

    resume_json = {
        "resumeData": {
            "basicDetails": parsed_data.get("basicDetails", {}),
            "workExperience": parsed_data.get("workExperience", []),
            "education": parsed_data.get("education", []),
            "skills": parsed_data.get("skills", []),
            "titles": parsed_data.get("titles", []),
            "certifications": parsed_data.get("certifications", [])
        },
        "summary": {"value": "", "confidence": 0.0},
        "htmlContent": "",
        "pdfText": text
    }

    print("\n===== RESUME PARSE RESULT =====")
    print("Top 500 Characters of Extracted Text:\n", text[:500], "\n")
    print(json.dumps(resume_json, indent=2))
    return resume_json

if __name__ == "__main__":
    file_path_pdf = r"C:\amrita_uni\Projects\asmacs internship\Imgdownload2.pdf"
    file_path_docx = r"C:\Users\velam\OneDrive\Documents\pavan's resume.docx"

    print("\n--- Processing PDF Resume ---")
    process_resume(file_path_pdf)

    print("\n--- Processing DOCX Resume ---")
    process_resume(file_path_docx)
