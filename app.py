import sys
from EmployeesMenu import *
from AssetsMenu import *
from CompanyFinancial import *

def save_data(emp_dict, asset_dict):
    try:
        with open("employees.txt", "w") as file:
            for emp in emp_dict.values():
                if emp.role == 'Manager':
                    line = f"{emp.emp_id}|{emp.name}|{emp.role}|{emp.salary}|{emp.bonus}"
                else:
                    line = f"{emp.emp_id}|{emp.name}|{emp.role}|{emp.salary}"
                file.write(line + "\n")
        with open("assets.txt", "w") as file:
            for asset in asset_dict.values():
                line = f"{asset.asset_id}|{asset.asset_type}|{asset.name}|{asset.value}"

                if isinstance(asset, Hardware):
                    line += f"|{asset.condition}|{asset.depreciation}"
                else:
                    line += f"|{asset.expiry_date}"
                file.write(line + "\n")
    except Exception as e:
        print(f"Critical Error During Save: {e}")

def load_data():
    assets = {}
    employees = {}
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if data[2] == "Manager":
                    emp = Manager(data[0], data[1], data[2], float(data[3]), float(data[4]))
                else:
                    emp = Employee(data[0], data[1], data[2], float(data[3]))
                employees[data[0]] = emp

        with open("assets.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if data[1] == "Hardware":
                    asset = Hardware(data[0], data[1], data[2], float(data[3]), data[4])
                else:
                    asset = Software(data[0], data[1], data[2], float(data[3]), data[4])
                assets[data[0]] = asset
    except FileNotFoundError:
        print(f"NO previous data found. Starting Fresh...")
    return employees, assets

def run_system():
    #1. storage
    # using dictionary
    (employees, assets) = load_data()

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
        print("4. Save Data")
        print("5. Save and Exit")
        print("6. Exit without Saving")

        choice = get_choice_validation("Enter your choice: ").strip()
        if choice == '1':
            print("-----------Employee Management Loading----------")
            print()
            manage_employees(employees)
            input("Press Enter to continue").strip()

        elif choice == '2':
            print("-------------Asset Management Loading-------------")
            print()
            manage_assets(assets, employees)
            input("Press Enter to continue").strip()

        elif choice == '3':
            print("------------Company Financials Loading------------")
            print()
            manage_financials(employees, assets)
            input("Press Enter to continue").strip()

        elif choice == '4':
            print("--------------------Save Data---------------------")
            save_data(employees, assets)
            print("Data saved successfully.")
            input("Press Enter to continue")
            continue
        elif choice == '5':
            print("--------------Saving Data and Exit----------------")
            save_data(employees, assets)
            sys.exit()
        elif choice == '6':
            print("-----------------Exiting System-------------------")
            sys.exit()
        else:
            print("Enter a valid choice from 1 to 4.")
            continue

run_system()