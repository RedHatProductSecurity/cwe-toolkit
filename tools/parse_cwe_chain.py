import argparse
import json


def load_cwe_definitions():
    """Load CWE definitions from a local JSON file.

    This data can be fetched with get_cwe_defs.py.
    """
    with open("./cwe_full_defs.json") as f:
        data = json.load(f)
    return data


def create_cwe_text(cwe_string):
    """Create a text representation of a CWE string along with a verbose translation.

    For example, "CWE-190->CWE-122" becomes: "CWE-190->CWE-122: Integer Overflow or
    Wraparound leads to Heap-based Buffer Overflow".
    """
    cwe_defs = load_cwe_definitions()
    cwe_parts = cwe_string.split("->")
    final_parts = []
    for part in cwe_parts:
        try:
            if "|" in part:
                # Only one level of nesting (using parens) is allowed so strip them all and split
                # to get all individual CWEs that need to be ORed.
                cwe_or = part.strip("()").split("|")
                cwe_or = " or ".join(cwe_defs[cwe] for cwe in cwe_or)
                final_parts.append(cwe_or)
            else:
                cwe = cwe_defs[part.strip("()")]
                final_parts.append(cwe)

        except KeyError:
            # If a CWE does not exist, return only the CWE string since showing an incomplete
            # CWE description text is worse than showing none at all.
            print(f"CWE(s) not found in: {part}")
            return

    desc = " leads to ".join(final_parts)
    return f"{cwe_string}: {desc}"


def main():
    p = argparse.ArgumentParser(description="Display CWE text ")
    p.add_argument("cwe_string", help="print CWE definitions")
    args = p.parse_args()

    if args.cwe_string:
        cwe_text = create_cwe_text(args.cwe_string)
        if cwe_text:
            print(cwe_text)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
