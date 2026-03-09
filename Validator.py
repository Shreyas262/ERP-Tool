def get_validation(prompt, expected_type=str):
    while True:
        print()
        user_input = input(prompt).strip()

        #input/data should not be empty
        if not user_input:
            print("Hey! you can't leave this empty...")
            continue

        #type check
        try:
            if expected_type == float:
                return float(user_input)
            elif expected_type == int:
                return int(user_input)
            else:
                return user_input
        except ValueError:
            print(f'Error: Please enter a valid {expected_type.__name__}.')

def get_choice_validation(prompt, expected_type=int):
    while True:
        print()
        user_input = input(prompt).strip()

        #choice should not be empty
        if not user_input:
            print("Please enter a choice.")
            continue

        #type check
        try:
            if expected_type == float:
                return float(user_input)
            elif expected_type == str:
                return str(user_input)
            else:
                return user_input
        except ValueError:
            print(f'Error: Please enter a valid {expected_type.__name__}.')