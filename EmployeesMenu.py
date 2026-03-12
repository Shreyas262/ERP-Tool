from Employees import Manager, Employee
from Validator import *


def manage_employees(employees_dict):
    while True:
        print("=" * 50)
        print('---------------Employee Management----------------')
        print("=" * 50)
        print()

        #menu
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")
        print("-" * 50)

        choice = get_choice_validation("Please enter your choice: ", int)
        if choice == '1':
            print("="*50)
            print("-----------------Add New Employee-----------------")
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
                bonus = get_validation('Enter Employee Bonus: ', float)
                new_emp = Manager(new_id, name, role, salary, bonus)
            else:
                new_emp = Employee(new_id, name, role, salary)

            employees_dict[new_id] = new_emp
            print(f"{name} added with Id {new_id}")

            input("Press Enter to continue...")

        elif choice == '2':
            print("=" * 50)
            print("---------------All Employees Details---------------")
            print("=" * 50)

            if not employees_dict:
                print("No employees found. Add some employees first.")
                print()
                input("Press Enter to continue...")
                continue

            for emp in employees_dict.values():
                print(emp.get_details())
                print('-' * 50)

            input("Press Enter to continue...")

        elif choice == '3':
            if not employees_dict:
                print("No employees found. Add some employees first.")
                print()
                input("Press Enter to continue...")
                continue
            print("=" * 50)
            print("-------------Update Employee Details--------------")
            print("=" * 50)

            empy_id_to_update = get_validation("Enter Employee ID to update: ", str)
            if empy_id_to_update in employees_dict.keys():
                empy_data = employees_dict[empy_id_to_update]

                print('Employee to Update: ')
                print(empy_data.get_details())

                while True:
                    print()
                    print('1. Update Employee Name')
                    print('2. Update Employee Salary')
                    if empy_data.role == 'Manager':
                        print('3. Update Employee Bonus')
                    print('4. Back to Employee Management Menu')


                    choice = get_choice_validation("Please enter your choice: ", int)

                    if choice == '1':
                        new_name = get_validation('Enter New Employee Name: ', str)
                        empy_data.name = new_name
                        print()
                        print(f'Employee "{empy_id_to_update}", Name changed to "{new_name}".')
                        input("Press Enter to continue...")

                    elif choice == '2':
                        new_salary = get_validation('Enter New Employee Salary: ', float)
                        empy_data.salary = new_salary
                        print()
                        print(f'Employee "{empy_id_to_update}", Salary changed to "{new_salary}".')
                        input("Press Enter to continue...")

                    elif choice == '3':
                        new_bonus = get_validation('Enter New Employee Bonus: ', float)
                        empy_data.bonus = new_bonus
                        print()
                        print(f'Employee "{empy_id_to_update}", Bonus changed to "{new_bonus}".')
                        input("Press Enter to continue...")

                    elif choice == '4':
                        print(empy_data.get_details())
                        employees_dict[empy_id_to_update] = empy_data
                        print('Going back to Employee Management Menu...')
                        break
                    else:
                        print("Please enter a valid choice from 1 to 4.")
                        continue

            else:
                print("Wrong employee ID.")
                input("Press Enter to continue...")

            input("Press Enter to continue...")
            print()

        elif choice == '4':
            print("=" * 50)
            print("-----------------Delete Employee------------------")
            print("=" * 50)


            del_emp_id = get_validation("Enter Employee ID to delete: ", str)
            if del_emp_id in employees_dict.keys():
                confirm_del = y_n_validation(f'Are you sure you want to delete employee with ID "{del_emp_id}"? (y/n): ', str).lower()
                if confirm_del == 'y':
                    del employees_dict[del_emp_id]
                    print(f"{del_emp_id} deleted.")
                    input("Press Enter to continue...")
                    continue
                elif confirm_del == 'n':
                    print('Going back to Employee Management Menu...')
                    input("Press Enter to continue...")
                    continue
                else:
                    print("Please enter a valid choice y/n.")
                    continue
            else:
                print("Employee not found.")
                print()
                input("Press Enter to continue...")

        elif choice == '5':
            print("-------------Going Back to Main Menu--------------")
            break
        else:
            print("Please enter a valid choice from 1 to 4.")