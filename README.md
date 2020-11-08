# cwe-toolkit

## Purpose

There are many cases where an individual security flaw may have an insignificant impact. However, when conditions allow several of these flaws to be used together, the impact of these weaknesses can multiply together and become a signficiant security vulnerability. The current state of CWEs across the industry only allows tracking of a single root cause, which for Red Hat's needs was insufficient.

This repository exists to explain some of the use cases and benefits that Red Hat finds in chaining multiple CWEs together for root cause analysis of security flaws. Additionally there is a basic implementation in Python.


## Combining CWEs

### Causation "leads to"

Sometimes, one weakness can lead to another.  For example, "Integer Overflow (CWE-190)" is often the cause of a "Heap Buffer Overflow" (CWE-122).  We represent this with the -> "leads-to" operator:

    CWE-190->CWE-122:  Integer Overflow leading to Heap Buffer Overflow


### Alternantive "or"

Another operator is | "or", which can be used when multiple independent weaknesses can occur.

    CWE-125|CWE-787:  Out-of-bounds Read or Out-of-bounds Write


### Chaining multiple operators together

These operators can be chained to give very precise descriptions:

    CWE-20->CWE-805->(CWE-125|CWE-787):  Improper Input Validation, leading to Buffer Access with Incorrect Index, leading to either Out-of-bounds Read or Out-of-bounds Write

Parentheses are limited to a single pair deep, so there is no complex nesting to be parsed.

## Statistics
These numbers are a snapshot of what Red Hat's CWE data looks like. Out of all CVEs created between July 2012 and July 2020:

  - 20% use “->” 
  - 3% use “|”


## Some complex examples

 - CWE-20->CWE-805->(CWE-125|CWE-787) https://access.redhat.com/security/cve/CVE-2014-8098
 - CWE-20->(CWE-59|CWE-270|CWE-552)->CWE-284 https://access.redhat.com/security/cve/CVE-2018-18495


## Possible future research

 - Would frequent use of two CWEs between a “|” indicate these could be merged?
 - CWEs which often get linked together with a “->” could be include a section titled “Commonly related CWEs”
