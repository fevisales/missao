#!/usr/bin/env python3

import sys

user_args = sys.argv[1:]

z_count = 0

if len(user_args) == 1:
    words = user_args[0].split()
else:
    words = user_args

for arg in words:
    if "z" in arg.lower():
        z_count += 1

if z_count > 0:
    print(z_count * "z")
else:
    print("Não foi encontrada nenhuma palavra com a letra \"Z\"")

