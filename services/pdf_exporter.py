from fpdf import FPDF
import os
import re
import zipfile
from model.report_model import ReportModel

from rich import print
from rich.panel import Panel

def clean_text(text):
    if text is None:
        return "N/A"
    return text.encode('latin-1', 'replace').decode('latin-1')

def sanitize_filename(name):
    """Remove invalid characters from filenames (especially Windows)."""
    return "".join(c for c in name if c.isalnum() or c in ('_', '-'))

def clean_ai_summary(summary):
    if not summary or not isinstance(summary, str):
        return "No valid AI summary available."

    summary = re.sub(r"(?i)disclaimer:.*?doctor\.", "", summary, flags=re.DOTALL)
    summary = re.sub(r"(?i)(based on an analysis|as a medical assistant|here is an analysis|first, it appears).*?(?=diagnosis|impression)", "", summary, flags=re.DOTALL)
    summary = re.sub(r"(?i)(['\"]?[a-zA-Z0-9 ,.’-]+['\"]? is likely [a-zA-Z0-9 ,.’-]+\.*\n*)+", "", summary, flags=re.DOTALL)

    summary = re.sub(r"\*+", "", summary)
    summary = re.sub(r"#", "", summary)

    summary = re.sub(r"\b[Dd]iagnosis.*?:", "\n\nDIAGNOSIS", summary)
    summary = re.sub(r"\b[Cc]ause.*?:", "\n\nCAUSE", summary)
    summary = re.sub(r"\b[Ss]uggestion.*?:", "\n\nSUGGESTION", summary)
    summary = re.sub(r"\b[Rr]ecommended [Aa]ction.*?:", "\n\nSUGGESTION", summary)

    summary = re.sub(r'\n{3,}', '\n\n', summary.strip())
    return summary.strip()

def export_report_to_pdf(username, report_id):
    report = ReportModel.get_report_by_id(report_id)

    if not report:
        print("[bold red]Report not found.[/bold red]")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="MediScan AI - Patient Medical Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Patient: {username}", ln=True)
    pdf.cell(200, 10, txt=f"Report ID: {report_id}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="AI Summary Suggestion:", ln=True)
    pdf.set_font("Arial", size=12)
    cleaned_summary = clean_ai_summary(report[4])
    pdf.multi_cell(0, 10, txt=clean_text(cleaned_summary))
    pdf.ln(5)

    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Doctor's Comment:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=clean_text(report[5]))

    output_dir = os.path.join("data", "pdf_exports")
    os.makedirs(output_dir, exist_ok=True)

    safe_username = sanitize_filename(username)
    output_path = os.path.join(output_dir, f"{safe_username}_report_{report_id}.pdf")

    pdf.output(output_path)
    print(Panel.fit(f"[blue]Report exported successfully![/blue]\n[bold]Saved to:[/bold] {output_path}", title="PDF Export", style="bold white"))

def batch_export_reports_as_zip(username):
    reports = ReportModel.get_reports_by_patient(username)
    if not reports:
        print(Panel.fit("[red]No reports found for this user.[/red]", title="Batch Export", style="red"))
        return

    output_dir = os.path.join("data", "pdf_exports")
    os.makedirs(output_dir, exist_ok=True)

    zip_filename = f"{sanitize_filename(username)}_all_reports.zip"
    zip_path = os.path.join(output_dir, zip_filename)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for report in reports:
            report_id = report[0]
            export_report_to_pdf(username, report_id)

            pdf_filename = f"{sanitize_filename(username)}_report_{report_id}.pdf"
            pdf_path = os.path.join(output_dir, pdf_filename)

            if os.path.exists(pdf_path):
                zipf.write(pdf_path, arcname=pdf_filename)

    print(Panel.fit(f"[bold blue]All reports zipped successfully![/bold blue]\n[bold]ZIP File:[/bold] {zip_path}", title="Batch Export", style="white"))