import re

def main():
    print(mul_impl("day3_input.txt"))

def mul_impl(file_name: str) -> int:
    sum = 0
    with open(file_name, "r") as file:
        for line in file:
            numbers = re.findall(r"mul\((\d+),\s?(\d+)\)", line)
            for x, y in numbers:
                sum += int(x) * int(y)

    return sum


if __name__ == "__main__":
    main()