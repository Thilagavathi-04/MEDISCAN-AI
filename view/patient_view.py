import re
from rich import print
from rich.panel import Panel

def show_patient_menu():
    print("\n[bold]Patient Menu:[/bold]")

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

def display_my_report(report):
    print(f"\nReport ID: {report[0]}")
    print(f"File: {report[1]}")

    cleaned_summary = clean_ai_summary(report[3])
    if cleaned_summary:
        print(Panel.fit(cleaned_summary, title="AI Summary", style="bold cyan"))
    else:
        print("[bold red]No AI summary available for this report.[/bold red]")

def ask_report_id_for_pdf():
    return input("Enter Report ID to export as PDF: ")