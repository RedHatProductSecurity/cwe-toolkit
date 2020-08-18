cwe_definitions = {}


def fetch_cwe_definitions():
    pass


def cwe_text(cwe_string):
    """Create a text representation of a CWE string along with a verbose translation.

    For example, "CWE-190->CWE-122" becomes: "CWE-190->CWE-122: Integer Overflow or
    Wraparound leads to Heap-based Buffer Overflow".
    """
    cwe_parts = cwe_string.split("->")
    final_parts = []
    for part in cwe_parts:
        try:
            if "|" in part:
                # Only one level of nesting (using parens) is allowed so strip them all and split
                # to get all individual CWEs that need to be ORed.
                cwe_or = part.strip("()").split("|")
                cwe_or = " or ".join(cwe_definitions[cwe] for cwe in cwe_or)
                final_parts.append(cwe_or)
            else:
                cwe = cwe_definitions[part.strip("()")]
                final_parts.append(cwe)

        except KeyError:
            # If a CWE does not exist, return only the CWE string since showing an incomplete
            # CWE description text is worse than showing none at all.
            return cwe_string

    desc = " leads to ".join(final_parts)
    return f"{self.cwe}: {desc}"
