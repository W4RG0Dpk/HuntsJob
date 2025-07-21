# HuntsJob
Internship project
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tesseract OCR](https://img.shields.io/badge/OCR-Tesseract-green)
![Poppler](https://img.shields.io/badge/PDF-Poppler-orange)
![Ollama](https://img.shields.io/badge/LLM-Ollama--LLaMA_3-black)
![AI Parsing](https://img.shields.io/badge/Parsing-LLM_Automated-purple)
![File Support](https://img.shields.io/badge/Supports-PDF%20%26%20DOCX-blueviolet)
![No Cloud Required](https://img.shields.io/badge/Privacy-Local--Only-lightgrey)
![Modular](https://img.shields.io/badge/Design-Modular-informational)
![Extensible](https://img.shields.io/badge/Extensible-Yes-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-ff69b4)

--- 
📝 Resume Parser — Intelligent Modular Resume Extraction
Welcome to Resume Parser, a robust, modular Python utility to rapidly extract, structure, and empower your resume data pipeline. Power through heaps of CVs with clean OCR, versatile file support, and bleeding-edge AI parsing — all right on your local machine!
---
✨ Features
Blazing-Fast Extraction: Handle PDF (including scanned, image-based) and DOCX resumes with precision.

State-of-the-Art OCR: Leverage Tesseract + Poppler for image-based PDFs. No text? No problem.

AI-Powered Parsing: Employs LLaMA 3 (via local Ollama server) for smart, structured JSON outputs.

Beautifully Modular: Easily extend or swap out extractors and parsers to meet your evolving needs.

Privacy-First: All parsing and AI happens locally—no third-party cloud upload!

Custom Prompting: Tailor the LLM instructions for your domain-specific parsing challenges.
---
📁 Project Structure

    resume_parser/
    │
    ├── main.py                # Entrypoint; orchestrates extraction & parsing
    ├── config.py              # Paths for OCR, Poppler, Ollama, model config
    │
    ├── extractors/
    │   ├── pdf_extractor.py   # PDF (with OCR) extraction logic
    │   └── docx_extractor.py  # Docx (Word) file extraction logic
    │
    ├── parsers/
    │   └── ollama_parser.py   # AI resume structuring logic
    │
    ├── requirements.txt
    └── README.md

---
---
🚀 Quickstart
1. Prerequisites
Python 3.8+

Ollama ([install guide]: ollama.com) + LLaMA 3 model pulled (ollama run llama3)

Tesseract OCR ([download])

Poppler ([download])

Confirm all tool paths in config.py and pdf / docx paths in main.py
---
2. Clone & Install
text
git clone <[YOUR_REPO_URL](https://github.com/W4RG0Dpk/HuntsJob)>
cd resume_parser
pip install -r requirements.txt
---
3. Configure
Edit config.py and fill in absolute paths for:

TESSERACT_PATH

POPLER_PATH

Ollama host/model if needed
---
4. Run!
text
python main.py

Rest all ipynb files are my personal workings of this project over time .
---
Contact : velamalapavankrishna@gmail.com
