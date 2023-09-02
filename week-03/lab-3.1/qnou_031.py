#!/usr/bin/env python3

import sys

qnou = []

for line in sys.stdin:
    s = line.strip()
    slow = s.lower().replace("qu", "")
    if "q" in slow:
        qnou.append(s)
print(f"Words with q but no u: {qnou}")
