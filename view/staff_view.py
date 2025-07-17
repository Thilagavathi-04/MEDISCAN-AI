def show_staff_menu():
    print("\n📋 Staff Menu:")
    print("1. Upload & Analyze Report")
    print("2. View Patient Reports")
    print("3. Export Reports to PDF")
    print("4. Back to Main Menu")

def ask_report_details():
    patient_username = input("Enter patient username: ").strip()
    image_path = input("Enter report image file path (e.g., data/reports/image1.jpg): ").strip('"')
    return patient_username, image_path

def show_upload_success():
    print("Report uploaded and analyzed successfully!")

def show_no_reports_found():
    print("No reports found for this patient.")

def show_export_success():
    print("Reports exported to PDF successfully!")

def show_invalid_choice():
    print("Invalid choice. Please select a valid option.")