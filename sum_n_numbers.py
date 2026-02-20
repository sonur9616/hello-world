"""Print the sum of n numbers provided by the user."""


def read_positive_count() -> int:
    """Read and return a positive integer count from stdin."""
    while True:
        raw = input("Enter how many numbers you want to sum: ").strip()
        try:
            count = int(raw)
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid count. Please enter a valid integer.")


def read_number(index: int) -> float:
    """Read and return one numeric value from stdin."""
    while True:
        raw = input(f"Enter number {index}: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def main() -> None:
    n = read_positive_count()
    total = 0.0

    for i in range(1, n + 1):
        total += read_number(i)

    if total.is_integer():
        print(f"Sum: {int(total)}")
    else:
        print(f"Sum: {total}")


if __name__ == "__main__":
    main()
