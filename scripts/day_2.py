"""
Both Tasks Solved successfully
"""
from src.utils import PathUtils

DAY = 2

bag_dict = {'red': 12, 'green': 13, 'blue': 14}


def task_1(input_list: list):
    valid_game_ids = []
    for line in input_list:
        game_id, line = get_game_id(line)
        if check_valid_games(line):
            valid_game_ids.append(int(game_id))

    print(f"Solution Task 1; Day {DAY}: {sum(valid_game_ids)}")


def task_2(input_list: list):
    power_set = []
    for line in input_list:
        _, line = get_game_id(line)
        power_set.append(get_power_set_games(line))
    print(f"Solution Task 2; Day {DAY}: {sum(power_set)}")


def get_game_id(line: str) -> tuple:
    split_text = line.split(":")
    game_id = split_text[0].split(" ")[1]
    return game_id, split_text[1]


def check_valid_games(line: str) -> bool:
    for game in line.split(';'):
        if not check_valid_game(game):
            return False
    return True


def check_valid_game(game: str) -> bool:
    for draw in game.split(','):
        draw = draw.split(' ')
        if bag_dict[draw[2]] < int(draw[1]):
            return False
    return True


def get_power_set_games(line: str) -> int:
    minimal_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for game in line.split(';'):
        for draw in game.split(','):
            draw = draw.split(' ')
            if minimal_cubes[draw[2]] < int(draw[1]):
                minimal_cubes[draw[2]] = int(draw[1])
    return minimal_cubes['red'] * minimal_cubes['green'] * minimal_cubes['blue']


if __name__ == '__main__':
    path_utils = PathUtils()
    daily_input = path_utils.get_input_list(DAY)

    task_1(daily_input)
    task_2(daily_input)
