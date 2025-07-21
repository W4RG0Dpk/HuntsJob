# parsers/ollama_parser.py
import requests
import json
from config import OLLAMA_HOST, OLLAMA_MODEL

def ollama_parse_resume(text):
    prompt = f"""
You are a professional resume parsing assistant. Extract the following fields from the resume text below, using only information explicitly present in the text. Do not guess or hallucinate. If a field is missing, use an empty string or empty list.

Return ONLY a valid JSON object with this structure:
{{
  "basicDetails": {{
    "name": "First name only, as found in text",
    "lastname": "Last name only, as found in text",
    "email": ["all email addresses found, as a list"],
    "phone": "phone number as found"
  }},
  "skills": [
    {{"skill": {{"value": "skill name", "confidence": 10.0}}}}
  ],
  "titles": [
    {{"title": {{"value": "job title", "confidence": 10.0}}}}
  ],
  "workExperience": [
    {{
      "company": "company name",
      "position": "job title",
      "duration": "duration or years"
    }}
  ],
  "education": [
    {{
      "degree": "degree name",
      "institution": "institution name",
      "year": "year or range"
    }}
  ],
  "certifications": ["certification names as list"]
}}

Resume Text:
{text}
"""
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
        
        start = result['response'].find('{')
        end = result['response'].rfind('}') + 1
        parsed = json.loads(result['response'][start:end])
        
    except Exception as e:
        print(f"[ERROR] Ollama parsing failed: {e}")
        parsed = {"error": str(e), "raw_response": result.get('response', '')}
    return parsed
