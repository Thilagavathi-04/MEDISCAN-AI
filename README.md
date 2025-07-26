# MEDISCAN-AI 🧠🩺  
**AI-Powered Medical Report Analyzer and Summarizer**

MEDISCAN-AI is a smart, Flask-based console application that automates the extraction, analysis, and summarization of medical records using OCR and LLMs. Designed for healthcare professionals, patients, and interns, this system streamlines diagnosis, first aid, medicine suggestions, training modules, and more.

---

## 🚀 Key Features

- 🔍 **OCR & AI Analysis**: Extracts and analyzes scanned reports or MRI images.
- 🧾 **Medical Summarization**: Generates condition, cause, and treatment summaries via Gemini.
- 🩹 **First-Aid Suggestions**: Offers AI-generated first-aid guidance for common symptoms.
- 💊 **Medicine Recommendations**: Suggests medicines based on diagnosis.
- 📄 **PDF Export**: Converts patient medical history into downloadable reports.
- 🎙️ **Voice Input**: Allows patients to speak symptoms for diagnosis.
- 📚 **Intern Training Module**: Includes MCQ quizzes on real case histories.

---

## 🛠️ Tech Stack

| Layer         | Technology                   |
|---------------|------------------------------|
| Language      | Python 3.10                  |
| Framework     | Flask                        |
| AI Integration| Gemini / Local LLM (optional)|
| OCR Engine    | Tesseract OCR                |
| UI            | CLI (Console-Based)          |
| Storage       | SQLite                       |
| File Handling | PyMuPDF, pytesseract         |
| PDF Export    | ReportLab / FPDF             |

---

## 📁 Folder Structure

MEDISCAN-AI/

├── app.py # Main controller

├── database/ # SQLite setup

├── models/ # User, patient, medicine models

├── services/ # AI services (OCR, Gemini, PDF, Quiz)

├── templates/ # CLI/console UI (if HTML added later)

├── static/ # Assets (if needed)

├── mcq.json # Intern quiz data


## 🧠 Future Enhancements
Web-based UI for broader accessibility

Role-based login authentication

Deployment on Render / Replit / Railway

Analytics dashboard for health trends
