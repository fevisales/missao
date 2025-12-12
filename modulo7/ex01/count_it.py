#!/usr/bin/env python3

import sys

user_args = sys.argv[1:]

if not user_args:
    print("none")
else:
    for arg in user_args:
        print(f"{arg.capitalize()}: {len(arg)}")
