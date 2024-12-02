from collections import Counter
from pathlib import Path

DIR_CURRENT = Path(__file__).parent.absolute()


def parse_input(input_txt: str) -> tuple[list[int], list[int]]:
    lines = input_txt.splitlines()
    left, right = [], []
    for line in lines:
        num_left_txt, num_right_txt = line.split()
        num_left = int(num_left_txt)
        num_right = int(num_right_txt)
        left.append(num_left)
        right.append(num_right)
    return left, right


if __name__ == "__main__":
    fp_input = DIR_CURRENT / "input.txt"
    input_txt = fp_input.read_text().strip()

    list_left, list_right = parse_input(input_txt)

    list_left_sorted = sorted(list_left)
    list_right_sorted = sorted(list_right)

    sum_abs_diff = 0
    for num_left, num_right in zip(list_left_sorted, list_right_sorted):
        sum_abs_diff += abs(num_left - num_right)

    print(f"Part 1: {sum_abs_diff}")

    counter_right = Counter(list_right)

    sim_score = 0
    for num_left in list_left:
        count_right = counter_right[num_left]
        score = num_left * count_right
        sim_score += score

    print(f"Part 2: {sim_score}")
