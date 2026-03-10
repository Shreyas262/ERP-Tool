import sys
from EmployeesMenu import *
from AssetsMenu import *
from Validator import *

def run_system():
    #1. storage
    # using dictionary
    employees = {}
    assets = {}
    asset_ids = set()

    admin_username = 'admin'
    admin_password = '1234'

    print("=" *50)
    print("------------Welcome to the NextGen ERP------------")
    print("="*50)

    authenticated = False
    attempts = 0
    while attempts < 3:
        user = input("Username: ").strip()
        password = input("Password: ").strip()
        if user == admin_username and password == admin_password:
            print("\n Access granted. Welcome to the NextGen ERP")
            authenticated = True
            break
        else:
            attempts += 1
            print("="*50)
            print("Login Failed. Check your username and password.")

    if not authenticated:
        print("="*50)
        print("Too many attempts. Closing System....")
        sys.exit()

    while True:
        print("="*50)
        print("--------------------MAIN MENU---------------------")
        print("="*50)
        print("1. Manage Employees")
        print("2. Manage Assets")
        print("3. Company Financials")
        print("4. Save & Exit")

        choice = get_choice_validation("Enter your choice: ").strip()
        if choice == '1':
            print("-----------Employee Management Loading----------")
            print()
            manage_employees(employees)
            input("Press Enter to continue").strip()

        elif choice == '2':
            print("-------------Asset Management Loading-------------")
            print()
            manage_assets(assets, employees, asset_ids)
            input("Press Enter to continue").strip()

        elif choice == '3':
            print("------------Company Financials Loading------------")
        elif choice == '4':
            print("-------------------Save & Exit--------------------")
            break
        else:
            print("Enter a valid choice from 1 to 4.")
run_system()