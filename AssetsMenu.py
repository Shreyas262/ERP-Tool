from Assets import *
from Validator import *
import datetime


def manage_assets(assets_dict, employee_dict):
    while True:
        print()
        print('=' * 50)
        print('--------------Asset Management Menu---------------')
        print('=' * 50)
        print('1. Add Asset')
        print('2. View All Assets')
        print('3. Assign Asset')
        print('4. Calculate Depreciation')
        print('5. Back to Main Menu')
        print('-' * 50)

        choice = get_validation("Select an option: ")
        if choice == '1':
            print()
            print('=' * 50)
            print('----------------Add Asset Details-----------------')
            print('=' * 50)

            while True:
                asst_type = get_validation("Asset type (Hardware/Software): ").capitalize()
                if asst_type not in ['Hardware', 'Software']:
                    print(f'Invalid asset type.')
                    continue
                else:
                    break

            name = get_validation("Asset Name: ", str)
            value = get_validation("Asset Value: ", float)

            if not assets_dict:
                new_id = 'A101'
            else:
                last_id = max(int(aid[1:]) for aid in assets_dict.keys())
                new_id = f"A{last_id + 1}"

            if asst_type == 'Hardware':
                condition = get_validation("Physical Condition: ", str).capitalize()
                new_assets = Hardware(new_id, asst_type, name, value, condition)
            else:
                print()
                print('Enter Expiry Date of the Software(YYYY/MM/DD): ')
                year = get_validation("Year: ", int)
                month = get_validation("Month: ", int)
                day = get_validation("Day: ", int)
                expiry_date = datetime.date(year, month, day)
                new_assets = Software(new_id, asst_type, name, value, expiry_date)

            assets_dict[new_id] = new_assets
            print(f'Asset {name} added with Id {new_id}.')
            input('Press Enter to continue.')

        elif choice == '2':
            print()
            print('=' * 50)
            print('--------------Viewing Asset Details---------------')
            print('=' * 50)

            if not assets_dict:
                print('No assets found. Add assets first.')
                input('Press Enter to continue.')
                continue

            for assets in assets_dict.values():
                print(assets.get_details())
                print('-' * 60)
            print()
            input('Press Enter to continue.')

        elif choice == '3':
            print()
            print('=' * 50)
            print('------------Assign Asset To Employee-------------')
            print('=' * 50)

            if not assets_dict:
                print('No assets found. Add assets first.')
                input('Press Enter to continue.')
                continue

            if not employee_dict:
                print('No employees found. Add employees first.')
                input('Press Enter to continue.')
                continue

            e_id = get_validation("Employee ID to assign Assets: ").capitalize()
            if e_id not in employee_dict:
                print('Invalid employee ID.')
                input('Press Enter to continue.')
                continue

            a_id = get_validation("Asset ID to assign: ").capitalize()
            if a_id not in assets_dict:
                print('Invalid asset ID.')
                input('Press Enter to continue.')
                continue

            asset_data = assets_dict[a_id]
            emp_data = employee_dict[e_id]

            emp_data.assign_asset(asset_data)
            print(f'Asset {a_id} assigned to {emp_data.name}.')
            employee_dict[e_id] = emp_data
            input('Press Enter to continue.')

        elif choice == '4':
            print()
            print('=' * 50)
            print('--------Calculating Depreciation for Asset----------')
            print('=' * 50)

            if not assets_dict:
                print('No assets found. Add assets first.')
                input('Press Enter to continue.')
                continue

            while True:
                ass_id = get_validation("Asset ID: ").capitalize().strip()

                if ass_id not in assets_dict:
                    print('Invalid asset ID. Please enter a valid asset ID.')
                    input('Press Enter to continue.')
                    continue

                if assets_dict[ass_id].asset_type == 'Hardware':
                    asset_age = get_validation("Enter Asset Age(years): ", int)
                    depreciation = assets_dict[ass_id].calculate_depreciation(asset_age)
                    print(f"'{ass_id}' Asset Age: {asset_age} | Depreciated Value: {depreciation}.")
                    input('Press Enter to continue.')
                    break
                else:
                    print("Entered Asset is a Software, therefore cannot calculate depreciation.")
                    input('Press Enter to continue.')
                    break

        elif choice == '5':
            print()
            print('-------------Going Back to Main Menu--------------')
            break

        else:
            print('Invalid choice. Please enter a valid choice.')
            input('Press Enter to continue.')
            continue

