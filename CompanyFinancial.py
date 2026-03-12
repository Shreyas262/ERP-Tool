from Validator import *


def print_report(entity_list):
    print("="*50)
    print("Generating Comprehensive Report...")
    print("="*50)
    print()

    for item in entity_list:
        print(item.get_details())

    print("-----End of report-----")
    print()

def manage_financials(emp_dic, asset_dic):
    while True:
        print("="*50)
        print("-------------Company Financials Menu--------------")
        print("="*50)
        print()
        print("1. Total Salary Expenditure")
        print("2. Total Assets Value")
        print("3. Generate Full Report")
        print("4. Back to Main Menu")
        print('-'*50)

        choice = get_choice_validation("Enter Choice: ")
        if choice == '1':
            print('=' * 50)
            print('-------------Total Salary Expenditure---------------')
            print('=' * 50)
            total_salary = sum(emp.salary for emp in emp_dic.values())
            total_bonus = sum(emp.bonus for emp in emp_dic.values() if emp.role == 'Manager')
            total_pay = total_bonus + total_salary

            print(f'Total Monthly Salary Expenditure: Rs.{total_pay:,.2f}')
            print('-' * 50)
            input("Press Enter to continue...")
        elif choice == '2':
            print('=' * 50)
            print('----------------Total Assets Value-----------------')
            print('=' * 50)
            total_value = sum(asset.value for asset in asset_dic.values())
            print(f'Total Assets Value: Rs.{total_value:,.2f}')
            input("Press Enter to continue...")
        elif choice == '3':
            print('=' * 50)
            print('--------------------Full Report--------------------')
            print('=' * 50)
            all_entities = list(emp_dic.values()) + list(asset_dic.values())
            print_report(all_entities)
            input("Press Enter to continue...")
        elif choice == '4':
            print("-------------Going Back to Main Menu--------------")
            break
        else:
            print("Enter a valid choice.")
            input("Press Enter to continue...")

