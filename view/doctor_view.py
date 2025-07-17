from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from view.patient_view import clean_ai_summary

console = Console()

def show_doctor_menu():
    print("\n🩺 Doctor Menu:")
    print("1. View All Reports")
    print("2. Add Comment to Report")
    print("3. Back to Main Menu")

def display_report(report):
    report_id, username, image_path, ocr_text, ai_summary, doctor_comment = report

    table = Table(title="Report Details", show_lines=True, title_style="bold cyan")
    table.add_column("Field", style="bold magenta", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("Report ID", str(report_id))
    table.add_row("Patient Username", username)
    table.add_row("Image Path", image_path)
    table.add_row("OCR Text", ocr_text.strip() or "N/A")
    table.add_row("Doctor Comment", doctor_comment or "[italic grey]None[/italic grey]")

    console.print(table)

    cleaned_summary = clean_ai_summary(ai_summary)
    if cleaned_summary:
        console.print(Panel.fit(cleaned_summary, title="AI Summary", style="bold green"))
    else:
        console.print(Panel.fit("No AI summary available.", title="AI Summary", style="red"))

def get_comment_input():
    report_id = input("Enter Report ID to comment on: ")
    comment = input("Enter your comment: ")
    return int(report_id), comment