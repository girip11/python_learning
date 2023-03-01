@profile
def say_hello(name: str) -> None:
    name_len = len(name)
    print(f"Hello {name}  (length {name_len}")


if __name__ == "__main__":
    say_hello("John")
