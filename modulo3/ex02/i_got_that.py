#!/usr/bin/env python3

user_input = input  ("O que você tem a dizer? : ")

while True:
    if user_input == "STOP":
        break
    else:
        user_input = input("Eu entendi! Mais alguma coisa? : ")
