from view.staff_view import show_staff_menu
from view.patient_view import display_my_report
from model.report_model import ReportModel
from services.ocr_service import extract_text_from_image
from services.gemini_service import generate_summary
from services.pdf_exporter import export_report_to_pdf, batch_export_reports_as_zip

from rich import print
from rich.console import Console
from rich.panel import Panel
import re

console = Console()

def clean_ai_summary(summary):
    if not summary or not isinstance(summary, str):
        return ""

    summary = re.sub(r"\*+", "", summary)
    summary = re.sub(r"#", "", summary)
    summary = re.sub(r"\b[Dd]iagnosis.*?:", "\n\n[bold]DIAGNOSIS[/bold]", summary)
    summary = re.sub(r"\b[Cc]ause.*?:", "\n\n[bold]CAUSE[/bold]", summary)
    summary = re.sub(r"\b[Ss]uggestion.*?:", "\n\n[bold]SUGGESTION[/bold]", summary)
    summary = re.sub(r'\n{3,}', '\n\n', summary.strip())
    return summary.strip()

def staff_menu(staff_username):
    while True:
        console.print(Panel.fit(f"[bold cyan]Welcome {staff_username}[/bold cyan]", style="bold blue"))

        console.print("[bold purple]1.[/bold purple] Upload & Analyze Report")
        console.print("[bold purple]2.[/bold purple] View Patient Reports")
        console.print("[bold purple]3.[/bold purple] Export Reports to PDF")
        console.print("[bold purple]4.[/bold purple] Batch Export Patient Reports as ZIP")  # <- moved up
        console.print("[bold purple]5.[/bold purple] Back to Main Menu")  # <- moved down

        choice = console.input("[bold cyan]Enter choice: [/bold cyan]").strip()

        if choice == "1":
            patient_username = input("Enter patient username: ").strip()
            image_path = input("Enter report image file path (e.g., data/reports/image1.jpg): ").strip('"')

            ocr_text = extract_text_from_image(image_path)
            console.print(f"\n[bold underline]File:[/bold underline] {image_path}")
            console.print(Panel.fit(ocr_text, title="[bold cyan]OCR Text[/bold cyan]", style="white"))

            ai_summary_raw = generate_summary(ocr_text)
            ai_summary_clean = clean_ai_summary(ai_summary_raw)
            console.print(Panel.fit(ai_summary_clean, title="[bold cyan]AI Summary[/bold cyan]", style="white"))

            ReportModel.save_report(patient_username, image_path, ocr_text, ai_summary_raw)
            console.print("[bold green]Report uploaded and analyzed successfully![/bold green]")

        elif choice == "2":
            patient = input("Enter patient username to view reports: ").strip()
            reports = ReportModel.get_reports_by_patient(patient)
            if reports:
                latest_report = reports[-1]
                report_id = latest_report[0]
                file_path = latest_report[2]

                console.print(Panel.fit(f"[bold]Report ID:[/bold] {report_id}\n[bold]File:[/bold] {file_path}",
                                        title="[bold green]Latest Report[/bold green]", style="cyan"))
            else:
                console.print("[bold red]No reports found for this patient.[/bold red]")

        elif choice == "3":
            patient = input("Enter patient username to export reports: ").strip()
            reports = ReportModel.get_reports_by_patient(patient)
            if reports:
                for report in reports:
                    report_id = report[0]
                    patient_username = report[1]
                    export_report_to_pdf(patient_username, report_id)
                console.print("[bold green]All reports exported as PDF successfully.[/bold green]")
            else:
                console.print("[bold red]No reports found to export.[/bold red]")

        elif choice == "4":
            patient = input("Enter patient username for ZIP export: ").strip()
            batch_export_reports_as_zip(patient)

        elif choice == "5":
            console.print("[yellow]Returning to main menu...[/yellow]")
            break

        else:
            console.print("[bold red]Invalid choice. Please select a valid option.[/bold red]")