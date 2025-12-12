#!/usr/bin/env python3

import sys

parameters = sys.argv

if len(parameters) == 1:
    print("none")
else:
    fst_par = parameters[1]
    print(fst_par)
