import os
from pathlib import Path

INPUT_FOLDER = 'input'


class PathUtils:
    @staticmethod
    def get_root_path() -> Path:
        return Path(__file__).parent.parent

    def get_input_folder(self) -> Path:
        input_folder_path = self.get_root_path().joinpath(INPUT_FOLDER)
        if not input_folder_path.is_dir():
            os.mkdir(input_folder_path)
        return input_folder_path

    def get_input_file(self, day: int) -> Path:
        input_name = f"input_day_{day}"
        return self.get_input_folder().joinpath(input_name)

    def get_input_list(self, day: int) -> list:
        with open(self.get_input_file(day)) as f:
            return [line[:-1] for line in f.readlines()]
