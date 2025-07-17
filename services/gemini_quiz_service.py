import json
import re
from services.gemini_service import gemini_generate_text

def extract_json(text):
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError as e:
            print("❌ JSON decode error:", e)
            print("🔎 Raw response:", text)
            return None
    print("❌ No JSON found in Gemini response.")
    return None

def generate_quiz_from_text(report_text):
    prompt = f"""
You are a medical quiz assistant.

Below is a noisy OCR-based medical report. Clean it mentally and generate 3 MCQs related to the findings.

📄 Report:
\"\"\"{report_text}\"\"\"

Respond ONLY with JSON in this format:
[
  {{
    "question": "What is the main diagnosis in the report?",
    "options": ["Pneumonia", "Pneumothorax", "Asthma", "Healthy"],
    "answer": "Pneumothorax"
  }},
  ...
]
"""
    raw = gemini_generate_text(prompt)
    return extract_json(raw)