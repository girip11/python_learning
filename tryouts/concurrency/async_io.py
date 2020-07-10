import asyncio
import time
from typing import List

import aiofiles

from tryouts.concurrency.sync_io import get_input_files


async def get_lines(file_name: str) -> int:
    async with aiofiles.open(file_name, mode="r") as input_file:
        return len(await input_file.readlines())


async def get_total_lines(files: List[str]) -> int:
    tasks = []
    for file in files:
        task = asyncio.ensure_future(get_lines(file))
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    return sum(results)


if __name__ == "__main__":
    files = get_input_files()

    print("Execution started")
    start_time = time.time()
    for _ in range(10):
        line_count = asyncio.run(get_total_lines(files))
    time_taken = time.time() - start_time

    print(f"Execution completed. Total line count: {line_count}")
    print(f"Time taken: {time_taken:.3f} seconds")
