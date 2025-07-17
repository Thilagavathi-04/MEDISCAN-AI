from rich import print
from rich.console import Console
from rich.panel import Panel
from inputimeout import inputimeout, TimeoutOccurred

console = Console()

def show_intern_menu():
    console.print(Panel.fit("[bold blue]Intern Menu[/bold blue]", style="white"))

def show_question(q, idx):
    console.print(f"\n[bold yellow]Q{idx+1}:[/bold yellow] {q['question']}", style="bold")
    for i, opt in enumerate(q["options"], 1):
        console.print(f"[cyan]{i}.[/cyan] {opt}")
    try:
        # FIXED: use plain input inside inputimeout
        return inputimeout(prompt="Your answer (1-4 or text): ", timeout=15)
    except TimeoutOccurred:
        console.print("[bold red]Time's up! No answer recorded.[/bold red]")
        return None

def show_score(score, total):
    console.print(Panel.fit(f"[bold magenta]You scored {score}/{total}![/bold magenta]", style="white"))

def show_score_list(scores):
    console.print(Panel.fit("[bold purple]Your Previous Quiz Scores[/bold purple]", style="white"))
    if not scores:
        console.print("[red]No scores available.[/red]")
    else:
        for score, taken_at in scores:
            console.print(f"[bold light cyan]{taken_at}[/bold light cyan] — [green]Score:[/green] [yellow]{score}[/yellow]")
