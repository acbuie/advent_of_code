import pathlib
import numpy as np


def part_one():
    file = pathlib.Path("2024/01/input.txt")
    data = np.genfromtxt(file, dtype=np.int_)

    # Split into columns
    x, y = data.T

    # Sort
    sorted_x = np.sort(x)
    sorted_y = np.sort(y)

    diff = np.abs(sorted_x - sorted_y)

    print(np.sum(diff))

    return sorted_x, sorted_y


def part_two(x, y):
    x_data = np.unique(x).tolist()  # Not necessary for this input, all unique
    unique_y, count_y = np.unique(y, return_counts=True)

    y_data = np.asarray((unique_y, count_y)).T.tolist()

    similarity = 0

    # Probably slow for very large lists
    for x in x_data:
        for y in y_data:
            if x == y[0]:
                similarity += x * y[1]
                continue

    print(similarity)


def main():
    x, y = part_one()
    part_two(x, y)


if __name__ == "__main__":
    main()
