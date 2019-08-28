"""Aivan"""

MIN_LENGTH = 4

password = input("Please enter a password of at least {} characters: ".format(MIN_LENGTH))
while len(password) < MIN_LENGTH:
    password = input("Please enter a password of at least {} characters: ".format(MIN_LENGTH))

print("*" * len(password))