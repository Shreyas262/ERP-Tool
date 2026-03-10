from Assets import Hardware, Software
from Validator import *

def manage_assets(assets_dict, employee_dict, asset_ids_set):
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
            print('=' * 50)
            print('----------------Add Asset Details-----------------')
            print('=' * 50)
            print()
            while True:
                asset_type = get_validation("Asset type (Hardware/Software): ").capitalize()
                if asset_type not in ['Hardware', 'Software']:
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

            if asset_type == 'Hardware':
                condition = get_validation("Physical Condition: ", str).capitalize()
                new_assets = Hardware(new_id, name, value, condition)
            else:
                expiry_date = get_validation("Expiration Date: ").capitalize()
                new_assets = Software(new_id, name, value, expiry_date)

            assets_dict[new_id] = new_assets
            print(f'Asset {name} added with Id {new_id}.')
            input('Press Enter to continue.')

        elif choice == '2':
            print('=' * 50)
            print('--------------Viewing Asset Details---------------')
            print('=' * 50)
            print()

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
            print('=' * 50)
            print('------------Assign Asset To Employee-------------')
            print('=' * 50)
            print()

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
            print('=' * 50)
            print('------------Calculating Depreciation for Asset---------------')
            print('=' * 50)
            print()
            if not assets_dict:
                print('No assets found. Add assets first.')
                input('Press Enter to continue.')
                continue



        elif choice == '5':
            print()
            print('-------------Going Back to Main Menu--------------')
            print()
            break

        else:
            print('Invalid choice. Please enter a valid choice.')
            input('Press Enter to continue.')
            continue

