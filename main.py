from controller.staff_controller import staff_menu
from controller.doctor_controller import doctor_menu
from controller.patient_controller import patient_menu
from controller.intern_controller import intern_menu
from model.user_model import UserModel
from db.database import create_tables

from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def welcome_screen():
    console.print("\n")
    title_panel = Panel.fit(
        "[bold cyan]MediScan AI[/bold cyan]",
        style="bold white",
        padding=(0, 3)
    )
    console.print(title_panel)  # LEFT aligned (removed Align.center)

    console.print("[bold purple]1.[/bold purple] Register")
    console.print("[bold purple]2.[/bold purple] Login")
    console.print("[bold purple]3.[/bold purple] Exit")

def register():
    console.print(Panel.fit("[cyan]Register New User[/cyan]", style="white"))
    username = input("Enter new username: ").strip()
    password = input("Enter password: ").strip()
    role = input("Enter role (staff/patient/doctor/intern): ").strip().lower()

    if role not in ["staff", "patient", "doctor", "intern"]:
        console.print("[red] Invalid role![/red]")
        return

    success = UserModel.register_user(username, password, role)
    if success:
        console.print(f"[green] Registered successfully as '{role}'![/green]")
    else:
        console.print("[bold red] Username already exists.[/bold red]")

def login():
    console.print(Panel.fit("[cyan]Login to Your Account[/cyan]", style="white"))
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    role = UserModel.validate_user(username, password)

    if role:
        console.print(f"[green] Logged in as [bold]{role}[/bold]![/green]")
        if role == "staff":
            staff_menu(username)
        elif role == "doctor":
            doctor_menu(username)
        elif role == "patient":
            patient_menu(username)
        elif role == "intern":
            intern_menu(username)
    else:
        console.print("[red] Invalid credentials. Please try again.[/red]")

if __name__ == "__main__":
    create_tables()

    while True:
        welcome_screen()
        choice = console.input("[bold yellow] Select option:[/]").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            console.print("[bold magenta] Exiting MediScan AI. Stay healthy![/bold magenta]")
            break
        else:
            console.print("[bold red] Invalid choice. Please try again.[/bold red]")