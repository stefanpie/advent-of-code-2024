from pathlib import Path

DIR_CURRENT = Path(__file__).parent.absolute()

T_report = list[int]
T_reports = list[T_report]


def parse_data(input_txt: str) -> T_reports:
    reports = []
    for line in input_txt.splitlines():
        report = list(map(int, line.split()))
        reports.append(report)
    return reports


def check_single_report(report: T_report) -> bool:
    diff = [left - right for left, right in zip(report, report[1:])]
    all_positive = all([d > 0 for d in diff])
    all_negative = all([d < 0 for d in diff])
    order_check = all_positive or all_negative

    diff_abs = [abs(d) for d in diff]
    correct_diff_level = True
    for diff_abs_val in diff_abs:
        if not (diff_abs_val >= 1 and diff_abs_val <= 3):
            correct_diff_level = False
            break

    if order_check and correct_diff_level:
        return True
    else:
        return False


def part_1(data: T_reports) -> int:
    num_safe = 0
    for report in data:
        if check_single_report(report):
            num_safe += 1

    return num_safe


def part_2(data: T_reports) -> int:
    num_safe = 0
    for report in data:
        report_varients = [report]
        for i in range(len(report)):
            report_varient = report[:i] + report[i + 1 :]
            report_varients.append(report_varient)

        check_results = [check_single_report(r) for r in report_varients]
        if any(check_results):
            num_safe += 1

    return num_safe


if __name__ == "__main__":
    fp_input = DIR_CURRENT / "input.txt"
    input_txt = fp_input.read_text().strip()

    data = parse_data(input_txt)

    part_1_result = part_1(data)
    print(f"Part 1: {part_1_result}")

    part_2_result = part_2(data)
    print(f"Part 2: {part_2_result}")
