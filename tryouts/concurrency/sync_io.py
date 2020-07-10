import time
from os import listdir
from os import path
from typing import List


def get_lines(file_name: str) -> int:
    with open(file_name) as input_file:
        return len(input_file.readlines())


def get_input_files() -> List[str]:
    resources_dir: str = path.join(path.dirname(__file__), "resources")
    return [path.join(resources_dir, f) for f in listdir(resources_dir)]


def get_total_line_count(files: List[str]) -> int:
    line_count: int = 0
    for file in files:
        line_count += get_lines(file)
    return line_count


if __name__ == "__main__":
    files = get_input_files()

    print("Execution started")
    start_time = time.time()
    for _ in range(10):
        line_count = get_total_line_count(files)
    time_taken = time.time() - start_time

    print(f"Execution completed. Total line count: {line_count}")
    print(f"Time taken: {time_taken:.3f} seconds")
