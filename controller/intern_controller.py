from view.intern_view import *
from model.quiz_model import QuizModel
from model.report_model import ReportModel
from services.gemini_quiz_service import generate_quiz_from_text
import json

from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def intern_menu(intern_username):
    while True:
        console.print(Panel.fit("[bold blue]Intern Menu[/bold blue]", style="white"))
        console.print("[bold purple]1.[/bold purple] View Previous Scores")
        console.print("[bold purple]2.[/bold purple] Generate Quiz from Patient Report (Gemini)")
        console.print("[bold purple]3.[/bold purple] Back to Main Menu")
        choice = console.input("[bold yellow]Enter choice: [/bold yellow]").strip()

        if choice == "1":
            scores = QuizModel.get_scores(intern_username)
            show_score_list(scores)

        elif choice == "2":
            generate_quiz_for_report(intern_username)

        elif choice == "3":
            console.print("[bold magenta]Returning to Main Menu...[/bold magenta]")
            break

        else:
            console.print("[bold red]Invalid choice.[/bold red]")

def generate_quiz_for_report(intern_username):
    report_id = console.input("[bold yellow]Enter Report ID to generate quiz from:[/bold yellow] ")
    report = ReportModel.get_report_by_id(report_id)

    if not report:
        console.print("[bold red]Report not found.[/bold red]")
        return

    ocr_text = report[3]

    if not ocr_text or ocr_text.strip() == "":
        console.print("[yellow]OCR text is empty. Please analyze a report first.[/yellow]")
        return

    console.print("\n[bold cyan]Generating quiz from Gemini...[/bold cyan]\n")

    quiz = generate_quiz_from_text(ocr_text)

    if quiz and isinstance(quiz, list):
        score = 0
        for i, q in enumerate(quiz):
            console.print(f"\n[bold blue]Q{i+1}: {q['question']}[/bold blue]")
            for idx, opt in enumerate(q["options"], 1):
                console.print(f"[bold white]{idx}. {opt}[/bold white]")

            ans = console.input("[bold yellow]Your answer (1-4 or text): [/bold yellow]").strip().lower()
            correct_text = q["answer"].strip().lower()

            if ans.isdigit():
                idx = int(ans)
                if 1 <= idx <= len(q["options"]):
                    selected = q["options"][idx - 1].strip().lower()
                    if selected == correct_text:
                        score += 1
                    else:
                        console.print(f"[red]Wrong! Correct answer: {q['answer']}[/red]")
                else:
                    console.print(f"[red]Invalid number! Correct answer: {q['answer']}[/red]")

            elif ans == correct_text:
                score += 1
            else:
                console.print(f"[red]Invalid input! Correct answer was: {q['answer']}[/red]")

        show_score(score, len(quiz))
        QuizModel.save_score(intern_username, score, quiz_type="gemini")
    else:
        console.print("[yellow]Could not generate quiz from this report.[/yellow]")
