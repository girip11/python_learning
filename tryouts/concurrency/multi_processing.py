import multiprocessing
import time
from typing import List

from tryouts.concurrency.sync_io import get_input_files, get_lines


def get_total_line_count(files: List[str]):
    with multiprocessing.Pool(processes=5) as process_pool:
        return sum(process_pool.map(get_lines, files))


if __name__ == "__main__":
    files = get_input_files()

    print("Execution started")
    start_time = time.time()
    for _ in range(10):
        line_count = get_total_line_count(files)
    time_taken = time.time() - start_time

    print(f"Execution completed. Total line count: {line_count}")
    print(f"Time taken: {time_taken:.3f} seconds")
