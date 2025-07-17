import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ Gemini API Key not found! Please set it in .env file")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro") 

def generate_summary(report_text):
    prompt = f"""
You are a medical assistant. Analyze the following medical report and return:
1. Diagnosis (what is the issue)
2. Cause (why it may have occurred)
3. Suggestion (recommended action)

Report:
\"\"\"{report_text}\"\"\"
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        if "429" in str(e):
            return "⚠️ Gemini API quota exceeded. Please check your plan."
        return f"⚠️ Error generating summary: {str(e)}"

def gemini_generate_text(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        if "429" in str(e):
            return "⚠️ Gemini API quota exceeded. Please check your plan."
        return f"⚠️ Error generating quiz: {str(e)}"