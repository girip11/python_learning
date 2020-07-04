import random
from shutil import copyfile
from typing import List


def get_file_contents(file_name: str) -> List[str]:
    with open(file_name, mode="r") as input_file:
        return [l for l in input_file]


def split_file(input_file_name: str, out_dir: str) -> None:
    counter: int = 0
    lines_read: int = 0
    lines = get_file_contents(input_file_name)

    while lines_read < len(lines):
        lines_to_read = random.randint(25, 100)
        print(lines_read, lines_to_read)
        counter += 1
        out_file_name: str = out_dir.format(file_name=f"movies_{counter:02d}.json")
        with open(out_file_name, "w") as out_file:
            out_file.writelines(lines[lines_read : (lines_read + lines_to_read)])
        lines_read += lines_to_read


def duplicate_file(input_file_name: str, out_dir: str, file_count: int = 1) -> None:
    for i in range(file_count):
        out_file_name: str = out_dir.format(file_name=f"movies_{(i + 1):02d}.json")
        copyfile(input_file_name, out_file_name)


if __name__ == "__main__":
    out_dir: str = "/media/girish/HDD/code_repos/github/repos/learning/python/tryouts/concurrency/resources/{file_name}"
    in_file: str = "/media/girish/HDD/code_repos/github/repos/learning/python/tryouts/concurrency/movies.json"

    # split_file(in_file, out_dir)
    duplicate_file(in_file, out_dir, 1000)
