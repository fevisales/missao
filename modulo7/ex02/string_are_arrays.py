#!/usr/bin/env python3

import sys

user_args = sys.argv[1:]

z_count = 0

for arg in user_args:
    if "z" in arg or "Z" in arg:
        z_count += 1
    else:
        print("achou não")

print(z_count * "z")
