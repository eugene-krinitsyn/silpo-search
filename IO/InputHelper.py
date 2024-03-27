from typing import List


class InputHelper:

    @staticmethod
    def get_valid_input(prompt: str) -> str:
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input cannot be empty. Please try again.")
            elif user_input.lower() == "none":
                print("Input cannot be 'None'. Please try again.")
            else:
                return user_input

    @staticmethod
    def get_products_input() -> List[str]:
        user_inputs = []
        print("Enter product names (press Enter to submit). Type 'Q' to finish.")

        while True:
            user_input = input("")
            stripped_input = user_input.strip().lower()
            if stripped_input == 'q':
                break
            elif stripped_input:
                user_inputs.append(user_input)
            else:
                print("Input cannot be empty. Please enter a value.")

        return user_inputs

    @staticmethod
    def get_boolean_input(prompt: str) -> bool:
        while True:
            user_input = input(prompt + " Yes(y) / No(n): ").strip().lower()
            if user_input in ['yes', 'y']:
                return True
            elif user_input in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please enter 'Yes' or 'No' (or 'y'/'n').")

    @staticmethod
    def pick_from_list(options: List[str]) -> List[str]:
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        choices = input(
            "Pick one or more cities separated by commas (e.g., 1, 2, 3) to search in, or press enter to search globally: ")
        if not choices:
            return options
        choices = choices.strip().split(',')

        try:
            choices = [int(choice.strip()) for choice in choices]
            selected_options = [options[choice - 1] for choice in choices if 1 <= choice <= len(options)]
            return selected_options
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by commas.")
            return []
