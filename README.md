# cwe-toolkit

## Purpose

There are many cases where an individual security flaw may have an insignificant impact.
However, when conditions allow several of these flaws to be used together, the impact of these weaknesses can multiply together and become a significant security vulnerability.
The current state of CWEs across the industry only allows tracking of a single root cause, which for Red Hat's needs was insufficient.
When conditions are just right even the smallest of timing differences lead to big vulnerabilities like was the case for
[Microarchitectural Data Sampling](https://access.redhat.com/security/vulnerabilities/mds).
Red Hat's CWE metrics are an essential statistic to make proactive improvements to the security of our products.
We recognized this need and introduced the first CWE chaining features into our internal tooling in 2012.

This repository exists to explain some of the use cases and benefits that Red Hat finds in chaining multiple CWEs together for root cause analysis of security flaws.
Additionally, there is a basic implementation of parsing a CWE chain in [tools](tools).


## Combining CWEs

### Causation: "leads to"

Sometimes, one weakness can lead to another.
For example, "Integer Overflow (CWE-190)" is often the cause of a "Heap Buffer Overflow" (CWE-122).
We represent this with the "leads-to" (`->`) operator:

- `CWE-190->CWE-122`: _Integer Overflow_ leads to _Heap Buffer Overflow_


### Alternative: "or"

Another operator is the "or" (`|`) operator, which can be used when multiple independent weaknesses can occur:

- `CWE-125|CWE-787`: _Out-of-bounds Read_ or _Out-of-bounds Write_


### Chaining multiple operators

These operators can be chained to give very precise descriptions:

- `CWE-20->CWE-805->(CWE-125|CWE-787)`: _Improper Input Validation_ leads to _Buffer Access with Incorrect Index_ leads to either _Out-of-bounds Read_ or _Out-of-bounds Write_

Parentheses are limited to a single pair deep, so there is no complex nesting to be parsed.

## Statistics

These numbers are a snapshot of what Red Hat's CWE data looks like.
Out of all CVEs created between July 2012 and July 2020:

- 8% use `->`
- 2% use `|`


## Some complex examples

- `CWE-20->CWE-805->(CWE-125|CWE-787)` in [CVE-2014-8098](https://access.redhat.com/security/cve/CVE-2014-8098)
- `CWE-20->(CWE-59|CWE-270|CWE-552)->CWE-284` in [CVE-2018-18495](https://access.redhat.com/security/cve/CVE-2018-18495)


## Possible future research

- Would frequent use of two CWEs between a `|` indicate these could be merged?
- CWEs which often get linked together with a `->` could be include a section titled "Commonly related CWEs"

---

[CWE](https://cwe.mitre.org/) is a trademark of The MITRE Corporation.
