import re
from pathlib import Path

DIR_CURRENT = Path(__file__).parent.absolute()


# RE_PART_1 = r"mul\(\d{1,3}\,\d{1,3}\)"
RE_PART_1 = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)")


def part_1(pm: str) -> int:
    args: list[tuple[int, int]] = []
    for match in RE_PART_1.finditer(pm):
        args.append((int(match.group(1)), int(match.group(2))))
    return sum([a * b for a, b in args])


def part_2(pm: str) -> int:
    locations_do = [m.start() for m in re.finditer(r"do\(\)", pm)]
    locations_dont = [m.start() for m in re.finditer(r"don't\(\)", pm)]

    mult_matches = list(RE_PART_1.finditer(pm))

    mult_matches_filtered = []
    for mult_match in mult_matches:
        mult_match_start = mult_match.start()
        do_locations_less = [loc for loc in locations_do if loc < mult_match_start]
        dont_locations_less = [loc for loc in locations_dont if loc < mult_match_start]

        closest_do = -1 if not do_locations_less else max(do_locations_less)
        closest_dont = None if not dont_locations_less else max(dont_locations_less)

        if closest_dont is None or closest_do > closest_dont:
            mult_matches_filtered.append(mult_match)

    return sum([int(m.group(1)) * int(m.group(2)) for m in mult_matches_filtered])


if __name__ == "__main__":
    fp_input = DIR_CURRENT / "input_small.txt"
    input_txt = fp_input.read_text().strip()

    part_1_res = part_1(input_txt)
    print(f"Part 1: {part_1_res}")

    part_2_res = part_2(input_txt)
    print(f"Part 2: {part_2_res}")
