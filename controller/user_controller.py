from model.user_model import UserModel
from view.user_view import *
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def setup_database():
    UserModel.create_tables()

def register_flow():
    console.print(Panel.fit("[bold cyan]Register for MediScan AI[/bold cyan]", style="cyan"))
    username = get_user_input("Enter new username: ")
    password = get_user_input("Enter password: ")
    role = get_user_input("Enter role (staff/patient/doctor/intern): ").lower()

    if UserModel.register_user(username, password, role):
        console.print(f"[green]Registration successful![/green] You are registered as [bold]{role}[/bold].")
        show_registration_success(role)
    else:
        console.print("[bold red]Registration failed. Username may already exist.[/bold red]")
        show_registration_failure()

def login_flow():
    console.print(Panel.fit("[bold blue]Login to MediScan AI[/bold blue]", style="bold blue"))
    username = get_user_input("Username: ").strip()
    password = get_user_input("Password: ").strip()
    role = UserModel.validate_user(username, password)

    if role:
        console.print(f"[green]Logged in successfully as [bold]{role}[/bold]![/green]")
        show_login_success(role)
        return username, role
    else:
        console.print("[bold red]Login failed. Invalid username or password.[/bold red]")
        show_login_failure()
        return None, None