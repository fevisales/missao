#!/usr/bin/env python3

number = float(input("Enter a number less than 25\n"))

if number < 25:
    while number <= 25:
        print(f"Inside the loop, my variable is {number:g}")
        number += 1
else:
    print("Error")
