#!/usr/bin/env python3
#!/bin/bash

num1 = float(input("Insira o primeiro número:\n"))
num2 = float(input("Insira o segundo número:\n"))

result = num1 * num2

print(f"{num1:g} x {num2:g} = {result:g}")
if result > 0:
	print("O resultado é positivo.")
elif result < 0:
	print("O resultado é negativo.")
else:
	print("O resultado é positivo e negativo.")
