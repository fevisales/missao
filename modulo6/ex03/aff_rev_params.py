#!/usr/bin/env python3

import sys

param_count = len(sys.argv)-1

if param_count < 2:
    print("none")
else:
    parameters_list = sys.argv[1:]
    reversed_list = parameters_list[::-1]
    for param in reversed_list:
        print(param)
