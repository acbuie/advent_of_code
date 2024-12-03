import pathlib
import itertools


def is_safe(values: list[int]) -> bool:
    diff = [y - x for (x, y) in itertools.pairwise(values)]

    # decreasing = [x < 0 for x in diff]
    increasing = [x > 0 for x in diff]

    # If not all False or all True
    all_negative = sum(increasing) == 0
    all_positive = sum(increasing) == len(increasing)
    if not all_negative and not all_positive:
        return False

    for x in diff:
        if abs(x) < 1 or abs(x) > 3:
            return False

    return True


# Part two
def is_dampened(values: list[int]) -> bool:
    for i, _ in enumerate(values):
        dampened_values = values.copy()
        dampened_values.pop(i)

        if is_safe(dampened_values):
            return True

    return False


def main():
    path = pathlib.Path("2024/02/input.txt")

    safe_count = 0
    dampened_count = 0

    with open(path, "r") as f:
        for line in f:
            data = [int(x.strip()) for x in line.split()]

            if is_safe(data):
                safe_count += 1
                continue

            if is_dampened(data):
                dampened_count += 1

    print(safe_count)
    print(dampened_count)

    print(safe_count + dampened_count)


if __name__ == "__main__":
    main()
