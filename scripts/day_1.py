"""
Both Tasks Solved successfully
"""
from src.utils import PathUtils

DAY = 1

digit_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def task_1(input_list: list):
    calibration_list = []

    for line in input_list:
        first_digit = None
        second_digit = None
        for character in line:
            if character.isdigit():
                if first_digit is None:
                    first_digit = character
                second_digit = character
        calibration_list.append(int(f"{first_digit}{second_digit}"))
    print(f"Solution Task 1; Day {DAY}: {sum(calibration_list)}")


def task_2(input_list: list):
    calibration_list = []
    for line in input_list:
        first_digit = None
        second_digit = None
        for left_pointer in range(len(line)):
            if line[left_pointer].isdigit():
                if first_digit is None:
                    first_digit = line[left_pointer]
                second_digit = line[left_pointer]
            else:
                digit = check_hidden_string_digit(line, left_pointer)
                if digit != 0:
                    if first_digit is None:
                        first_digit = digit
                    second_digit = digit
            left_pointer += 1

        calibration_list.append(int(f"{first_digit}{second_digit}"))
    print(f"Solution Task 2; Day {DAY}: {sum(calibration_list)}")


def check_hidden_string_digit(line: str, left_pointer: int) -> int:
    """
    Checks for a hidden digit written with the strings
    :param line: string line to check
    :param left_pointer: left array pointer
    :return: hidden digit, 0 if there is no hidden digit
    """
    for string_length in range(3, 6):
        right_pointer = left_pointer + string_length
        if right_pointer > len(line):
            return 0
        key_string = line[left_pointer:right_pointer]
        if key_string in digit_dict:
            return digit_dict[key_string]
    return 0


if __name__ == '__main__':
    path_utils = PathUtils()
    daily_input = path_utils.get_input_list(DAY)

    task_1(daily_input)
    task_2(daily_input)
