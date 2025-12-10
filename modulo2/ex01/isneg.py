#!/usr/bin/env python3
#!/bin/bash

number = float(input("Insira um número\n"))

if number < 0:
        print("Este número é negativo.")
elif number > 0:
	print("Este número é positivo.")
else:
        print("Este número é positivo e negativo.")
