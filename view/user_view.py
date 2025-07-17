def show_welcome():
    print("\nMediScan AI ")
    print("1. Register")
    print("2. Login")

def get_user_input(prompt):
    return input(prompt)

def show_registration_success(role):
    print(f"Registered successfully as '{role}'!")

def show_registration_failure():
    print("Username already exists. Try a different one.")

def show_login_success(role):
    print(f"Logged in successfully as '{role}'")

def show_login_failure():
    print("Invalid credentials. Please try again.")