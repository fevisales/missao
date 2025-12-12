#!/usr/bin/env python3

import sys

parameters_count = len(sys.argv) -1

if parameters_count != 1:
    print("none")
else:
    one_parameter = sys.argv[1]
    low_case = one_parameter.lower()
    print(low_case)
