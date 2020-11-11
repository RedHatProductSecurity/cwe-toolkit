import argparse
import csv
import io
import json
from zipfile import ZipFile

import requests

# https://cwe.mitre.org/data/downloads.html
CWE_URLS = [
    "https://cwe.mitre.org/data/csv/1000.csv.zip",  # Research Concepts
    "https://cwe.mitre.org/data/csv/699.csv.zip",  # Development Concepts
    "https://cwe.mitre.org/data/csv/1008.csv.zip",  # Architectural Concepts
]


def get_cwe_definitions():
    """Fetch all CWE definitions from MITRE."""
    defs = {}
    for url in CWE_URLS:
        response = requests.get(url)
        zip_file = ZipFile(io.BytesIO(response.content))

        for file_name in zip_file.namelist():
            contents = zip_file.read(file_name).decode("utf-8")
            reader = csv.reader(io.StringIO(contents))

            next(reader)  # Skip the header line
            for line in reader:
                # Add CWE ID and its definition; prefix ID with "CWE-"
                defs[f"CWE-{line[0]}"] = line[1]

    return defs


def main():
    p = argparse.ArgumentParser(description="Fetch CWE definitions from cwe.mitre.org")
    group = p.add_mutually_exclusive_group()
    group.add_argument(
        "-p",
        "--print",
        dest="print_defs",
        action="store_true",
        help="print CWE definitions.",
    )
    group.add_argument(
        "-s",
        "--save",
        dest="save_defs",
        action="store_true",
        help="save CWE definitions to file.",
    )
    args = p.parse_args()

    if args.print_defs:
        for cwe_id, cwe_def in get_cwe_definitions().items():
            print(cwe_id, cwe_def)
    elif args.save_defs:
        with open("cwe_full_defs.json", "w") as f:
            json.dump(get_cwe_definitions(), f)
        print("Saved to: ./cwe_full_defs.json")
    else:
        p.print_help()


if __name__ == "__main__":
    main()
