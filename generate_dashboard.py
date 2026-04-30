from __future__ import annotations

import argparse
import csv
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_DATA = PROJECT_ROOT / "hr_clean.csv"
DEFAULT_TEMPLATE = PROJECT_ROOT / "dashboard.html"
DEFAULT_OUTPUT = PROJECT_ROOT / "index.html"

REQUIRED_COLUMNS = {
    "Age",
    "MonthlyIncome",
    "Department",
    "JobRole",
    "OverTime",
    "JobSatisfaction",
    "YearsAtCompany",
    "attrition",
}


def validate_csv(path: Path) -> int:
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row.")

        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            missing_text = ", ".join(sorted(missing))
            raise ValueError(f"CSV is missing required columns: {missing_text}")

        row_count = sum(1 for _ in reader)

    if row_count == 0:
        raise ValueError("CSV file has no data rows.")

    return row_count


def generate_dashboard(data_path: Path, template_path: Path, output_path: Path) -> None:
    row_count = validate_csv(data_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    data_output = output_path.parent / data_path.name
    if data_path.resolve() != data_output.resolve():
        shutil.copy2(data_path, data_output)

    html = template_path.read_text(encoding="utf-8")
    html = html.replace('fetch("hr_clean.csv")', f'fetch("{data_output.name}")')
    html = html.replace("Source: hr_clean.csv", f"Source: {data_output.name}")

    output_path.write_text(html, encoding="utf-8")

    print(f"Generated dashboard: {output_path}")
    print(f"Data file: {data_output}")
    print(f"Rows: {row_count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the Employee Attrition dashboard HTML.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="Path to cleaned HR CSV file.")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="Path to dashboard HTML template.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output HTML path.")
    args = parser.parse_args()

    generate_dashboard(
        data_path=args.data.resolve(),
        template_path=args.template.resolve(),
        output_path=args.output.resolve(),
    )


if __name__ == "__main__":
    main()
