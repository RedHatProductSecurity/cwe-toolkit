# Tools

This directory contains two rudimentary scripts that allow for easier experimentation with CWE data:

- `get_cwe_defs.py`: Downloads and either prints or saves CWE IDs along with their descriptions.

- `parse_cwe_chain.py`: Parses a CWE string containing one or more (chained) CWE IDs and displays its textual representation.

Example:

```bash
tools $ python3 get_cwe_defs.py -p | grep 'Cross-'
CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
CWE-352 Cross-Site Request Forgery (CSRF)
CWE-692 Incomplete Denylist to Cross-Site Scripting
CWE-942 Permissive Cross-domain Policy with Untrusted Domains
tools $ python3 get_cwe_defs.py -s
Saved to: ./cwe_full_defs.json
tools $ python3 parse_cwe_chain.py CWE-79
CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
tools $ python3 parse_cwe_chain.py 'CWE-20->CWE-805->(CWE-125|CWE-787)'
CWE-20->CWE-805->(CWE-125|CWE-787): Improper Input Validation leads to Buffer Access with Incorrect Length Value leads to Out-of-bounds Read or Out-of-bounds Write
```
