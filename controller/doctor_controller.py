from model.report_model import ReportModel
from view.doctor_view import display_report
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def doctor_menu(doctor_username):
    while True:
        console.print(Panel.fit("[bold blue] Doctor Menu[/bold blue]", style="cyan"))
        console.print("[bold purple]1.[/bold purple] View All Reports")
        console.print("[bold purple]2.[/bold purple] Add Comment to Report")
        console.print("[bold purple]3.[/bold purple] Back to Main Menu")
        
        choice = console.input("[bold cyan]Enter choice: [/bold cyan]").strip()

        if choice == "1":
            reports = ReportModel.get_all_reports()
            if reports:
                for report in reports:
                    display_report(report)
            else:
                console.print("[bold red]No reports found.[/bold red]")

        elif choice == "2":
            report_id_str = console.input("[bold yellow]Enter Report ID to comment:[/bold yellow] ").strip()
            comment = console.input("[bold yellow]Enter your comment:[/bold yellow] ").strip()
            
            if report_id_str.isdigit():
                report_id = int(report_id_str)
                ReportModel.add_doctor_comment(report_id, comment, doctor_username)
                console.print("[bold green]Comment added successfully.[/bold green]")
            else:
                console.print("[bold red]Invalid Report ID. Please enter a number.[/bold red]")

        elif choice == "3":
            console.print("[bold magenta]Returning to Main Menu...[/bold magenta]")
            break

        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")