from typing import List, Optional, Dict

def parse_row(row: str) -> Optional[tuple[str, Optional[int]]]:
    parts = row.split(",")
    if not parts:
        return None

    name = parts[0].strip()
    if not name:
        return None

    age: Optional[int] = None
    if len(parts) >= 2:
        age_str = parts[1].strip().lower()
        if age_str != "unknown":
            try:
                age = int(age_str)
            except ValueError:
                pass

    return name, age

def average(nums: List[int]) -> Optional[float]:
    if not nums:
        return None
    return sum(nums) / len(nums)

def build_report(rows: List[str]) -> Dict[str, object]:
    students: List[str] = []
    ages: Dict[str, Optional[int]] = {}

    for row in rows:
        parsed = parse_row(row)
        if parsed is None:
            continue
        name, age = parsed
        students.append(name)
        ages[name] = age

    valid_ages = [age for age in ages.values() if age is not None]
    avg_age = average(valid_ages)

    return {
        "students": students,
        "ages": ages,
        "average_age": avg_age
    }

def print_report(report: Dict[str, object]) -> None:
    print("Students:", report["students"])
    ages_display = {name: age for name, age in report["ages"].items()}
    print("Ages map:", ages_display)

    avg = report["average_age"]
    if avg is None:
        print("Average age: N/A")
    else:
        print(f"Average age: {avg:.2f}")

# ejemplo de uso
data = [
    "alice, 18",
    "bob,unknown",
    "carla, 0",
    "david, 20",
    "eva, not_a_number",
    "  frank  ,  21 ",
    "badrow"
]

report = build_report(data)
print_report(report)
