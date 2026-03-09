from Employees import Manager, Employee
from Validator import *


def manage_employees(employees_dict):
    while True:
        print("=" * 50)
        print('-------------Employee Management-------------')
        print("=" * 50)
        print()

        #menu
        print("1.1 Add New Employee")
        print("1.2 View All Employees")
        print("1.3 Update Employee")
        print("1.4 Delete Employee")
        print("1.5 Back to Main Menu")

        choice = get_choice_validation("Please enter your choice: ", int)
        if choice == '1':
            print("="*50)
            print("-------------Add New Employee----------------")
            print("="*50)
            name = get_validation("Enter Employee Name: ", str)
            role = get_validation("Enter Employee Role: ", str).capitalize()
            salary = get_validation("Enter Employee Salary: ", float)

            if role not in ['Manager', 'Staff']:
                print("Wrong role. Entering 'Staff' as default.")
                role = 'Staff'
            #generate unique id
            if not employees_dict:
                new_id = 'E101'
            else:
                last_id = max(int(eid[1:]) for eid in employees_dict.keys())
                new_id = f'E{last_id + 1}'

            if role == 'Manager':
                new_emp = Manager(new_id, name, role, salary, bonus = 1000.0)
            else:
                new_emp = Employee(new_id, name, role, salary)

            employees_dict[new_id] = new_emp
            print(f"{name} added with Id {new_id}")

            input("Press Enter to continue...")

        elif choice == '2':
            print("=" * 50)
            print(" --------------View All Employees----------------")
            print("=" * 50)

            for emp in employees_dict.values():
                print(emp.get_details())
                print('-' * 50)

            input("Press Enter to continue...")
            print()

        elif choice == '3':
            if not employees_dict:
                print("No employees found. Add some employees first.")
                print()
                input("Press Enter to continue...")
                continue
            print("=" * 50)
            print("-------------Update Employee----------------")
            print("=" * 50)

            emp_id_to_update = get_validation("Enter Employee ID to update: ", str)
            if emp_id_to_update in employees_dict.keys():
                emp_data = employees_dict[emp_id_to_update]

                print('Employee to Update: ')
                while True:
                    print('1. Update Employee Name')
                    print('2. Update Employee Salary')
                    if emp_data['role'] == 'Manager':
                        print('3. Update Employee Bonus')
                    print('4. Back to Employee Management Menu')
                    get_choice_validation("Please enter your choice: ", int)

                    if choice == '1':
                        new_name = get_validation('Enter Employee Name: ', str)
                        emp_data['name'] = new_name
                    elif choice == '2':
                        new_salary = get_validation('Enter Employee Salary: ', float)
                        emp_data['salary'] = new_salary
                    elif choice == '3':
                        new_bonus = get_validation('Enter Employee Bonus: ', float)
                        emp_data['bonus'] = new_bonus
                    elif choice == '4':
                        print(emp_data.get_details())
                        employees_dict[emp_id_to_update] = emp_data
                        print('Going back to Employee Management Menu')
                        input("Press Enter to continue...")
                    else:
                        print('Wrong choice. Please enter a valid choice.')

            else:
                print("Wrong employee ID.")
                input("Press Enter to continue...")

            input("Press Enter to continue...")
            print()

        elif choice == '4':
            print("=" * 50)
            print("-------------Delete Employee----------------")
            print("=" * 50)



            input("Press Enter to continue...")

        elif choice == '5':
            print("-------------Going Back to Main Menu----------------")
            break
        else:
            print("Please enter a valid choice from 1 to 4.")