import re
from pathlib import Path

import numpy as np

DIR_CURRENT = Path(__file__).parent.absolute()


def part_1(data: np.ndarray) -> int:
    count = 0
    templates = [np.array(["X", "M", "A", "S"]), np.array(["S", "A", "M", "X"])]

    # Horizontal and vertical matches
    for template in templates:
        for i in range(data.shape[0]):
            for j in range(data.shape[1] - 3):
                if np.array_equal(data[i, j : j + 4], template):
                    count += 1
        for i in range(data.shape[0] - 3):
            for j in range(data.shape[1]):
                if np.array_equal(data[i : i + 4, j], template):
                    count += 1

    # Diagonal matches
    for i in range(data.shape[0] - 3):
        for j in range(data.shape[1] - 3):
            if (
                data[i, j] == "X"
                and data[i + 1, j + 1] == "M"
                and data[i + 2, j + 2] == "A"
                and data[i + 3, j + 3] == "S"
            ) or (
                data[i, j] == "S"
                and data[i + 1, j + 1] == "A"
                and data[i + 2, j + 2] == "M"
                and data[i + 3, j + 3] == "X"
            ):
                count += 1
        for j in range(3, data.shape[1]):
            if (
                data[i, j] == "X"
                and data[i + 1, j - 1] == "M"
                and data[i + 2, j - 2] == "A"
                and data[i + 3, j - 3] == "S"
            ) or (
                data[i, j] == "S"
                and data[i + 1, j - 1] == "A"
                and data[i + 2, j - 2] == "M"
                and data[i + 3, j - 3] == "X"
            ):
                count += 1

    return count


def check_template(sub_data: np.ndarray, template: np.ndarray) -> bool:
    assert sub_data.shape == template.shape
    for i in range(sub_data.shape[0]):
        for j in range(sub_data.shape[1]):
            if template[i, j] != "." and sub_data[i, j] != template[i, j]:
                return False
    return True


def part_2(data: np.ndarray) -> int:
    template_1 = np.array([["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]])
    template_2 = np.array([["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]])
    template_3 = np.array([["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]])
    template_4 = np.array([["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]])

    templates = [template_1, template_2, template_3, template_4]

    count = 0
    for i in range(data.shape[0] - 2):
        for j in range(data.shape[1] - 2):
            for template in templates:
                if check_template(data[i : i + 3, j : j + 3], template):
                    count += 1

    return count


def parse_input(x: str) -> np.ndarray:
    lines = x.splitlines()
    array = [list(line) for line in lines]
    np_array = np.array(array)
    return np_array


if __name__ == "__main__":
    fp_input = DIR_CURRENT / "input.txt"
    input_txt = fp_input.read_text().strip()

    data = parse_input(input_txt)

    part_1_res = part_1(data)
    print(f"Part 1: {part_1_res}")

    part_2_res = part_2(data)
    print(f"Part 2: {part_2_res}")
