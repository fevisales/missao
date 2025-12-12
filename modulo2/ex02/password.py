#!/usr/bin/env python3
#!/bin/bash

password = "Python is awesome"

digit_password = str(input("Insira uma senha\n"))

if password == digit_password:
	print("ACESSO CONCEDIDO")
else:
	print("ACESSO NEGADO")

