from pathlib import Path

def get_joltage(bank: str) -> int:
    if not bank or len(bank) < 2:
        return 0

    first_index = None
    first_digit = None
    for d in "987654321":
        idx = bank.find(d)
        if idx != -1 and idx < len(bank) - 1:
            first_index = idx
            first_digit = d
            break

    if first_index is None:
        return 0

    right_slice = bank[first_index + 1:]
    if not right_slice:
        return 0

    second_digit = max(right_slice)

    return int(first_digit) * 10 + int(second_digit)


def main():
    path = Path("input.txt")
    data = path.read_text().strip()
    lines = data.splitlines()

    total = sum(get_joltage(line.strip()) for line in lines if line.strip())
    print(total)


if __name__ == "__main__":
    main()
