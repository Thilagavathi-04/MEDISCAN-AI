from view.patient_view import *
from model.report_model import ReportModel
from services.pdf_exporter import export_report_to_pdf
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def patient_menu(patient_username):
    while True:
        console.print(Panel.fit(f" [bold cyan]Welcome {patient_username}[/bold cyan]", style="bold white"))
        show_patient_menu()
        console.print("[bold purple]1.[/bold purple] View My Reports")
        console.print("[bold purple]2.[/bold purple] Export a Report to PDF")
        console.print("[bold purple]3.[/bold purple] Back to Main Menu")
        
        choice =console.input("[bold yellow]Enter choice: [/bold yellow]").strip()

        if choice == "1":
            reports = ReportModel.get_reports_by_patient(patient_username)
            if reports:
                for report in reports:
                    display_my_report(report)
            else:
                console.print("[bold red]No reports found.[/bold red]")

        elif choice == "2":
            report_id_str = ask_report_id_for_pdf()

            if not report_id_str.isdigit():
                console.print("[red]Invalid Report ID.[/red]")
                continue

            report_id = int(report_id_str)
            export_report_to_pdf(patient_username, report_id)
            console.print("[bold green]Report exported to PDF successfully![/bold green]")

        elif choice == "3":
            console.print("[magenta]Returning to Main Menu...[/magenta]")
            break

        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")