# cwe-toolkit




## CWE coverage

The number of possible CWE IDs listed by Mitre is much bigger than what would be practical for assigning CWE IDs or mining useful statistics. One of the problems is granularity - some CWEs are way too specific (mostly variants), some are way too general (classes). For this reason, PS uses only a subset of Mitre's CWE definitions, internally called CWE coverage.  The CWE coverage subset is a useful level of abstraction and uses a CWE cross-section view with a few added CWEs (mostly of Base type). 


## Combining CWEs

Sometimes, one weakness can lead to another.  For example, "Integer Overflow (CWE-190)" is often the cause of a "Heap Buffer Overflow" (CWE-122).  We represent this with the -> "leads-to" operator:

    CWE-190->CWE-122:  Integer Overflow leading to Heap Buffer Overflow

Another operator is | "or", which can be used when multiple independent weaknesses can occur.

    CWE-125|CWE-787:  Out-of-bounds Read or Out-of-bounds Write

These operators can be chained to give very precise descriptions:

    CWE-20->CWE-805->(CWE-125|CWE-787):  Improper Input Validation, leading to Buffer Access with Incorrect Index, leading to either Out-of-bounds Read or Out-of-bounds Write


## Statistics
20% use “->” 
3% use “|”
Some complex examples
CWE-20->CWE-805->(CWE-125|CWE-787) from CVE-2014-8098
CWE-20->(CWE-59|CWE-270|CWE-552)->CWE-284 from CVE-2018-18495
    Improper Input Validation LEADS TO ( link following OR privilege context switching error  OR Files or Directories Accessible to External Parties ) LEADS TO improper access control
(CWE-A|CWE-B)->CWE-C is pretty common
SFM2 advanced search I’m using

Would frequent use of two CWEs between a “|” indicate these could be merged?
CWEs which often get linked together with a “->” could be include a section titled “Commonly related CWEs”
