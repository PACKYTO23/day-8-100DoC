# # # Simple Function
# def greet():
#     print("See ya' later,")
#     print("Alli-")
#     print("-gator.")
#
#
# greet()


# # # Function that allows for input.

# def greet_with_name(name):
#     print(f"Hello, {name}.")
#     print(f"How de you do, {name}?")


# greet_with_name("Juan")

# # # Functions with more than 1 input.

# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}?")


# greet_with(name="Juan", location="Nogales")

# / # / # EXERCISE # / # / #

# import math


# def paint_calc(height, width, cover):
#     area = height * width
#     result = math.ceil(area / cover)
#     print(f"You'll need {result} cans of paint.")


# test_h = int(input("Height of wall (m)\n"))
# test_w = int(input("Width of wall (m)\n"))
# coverage = 5

# paint_calc(height=test_h, width=test_w, cover=coverage)

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# def prime_checker(number):
#     if number == 2 or number == 3 or number == 5 or number == 7:
#         print("It's a prime number.")
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")


# n = int(input("Check this number: "))

# prime_checker(number=n)

# / # / # / # / # / #

# / # / # PROJECT OF DAY 8 # / # / #

from art import logo

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def caesar(process, message, code):
    ciphered_message = ""
    if process == "decode":
        code *= -1
    for ch in message:
        if ch in alphabet:
            old_index = alphabet.index(ch)
            new_index = old_index + code
            ciphered_message += alphabet[new_index]
        else:
            ciphered_message += ch

    print(f"The {direction}d text is {ciphered_message}.")


print(logo)

should_continue = False
while not should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(process=direction, message=text, code=shift)
    encrypt_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if encrypt_again == "no":
        should_continue = True
        print("Let's encrypt again soon!")

# def encrypt(message=text, code=shift):
#     encrypted_message = ""
#     for ch in message:
#         old_index = alphabet.index(ch)
#         new_index = old_index + code
#         encrypted_message += alphabet[new_index]
#     print(f"The encoded text is {encrypted_message}.")


# def decrypt(message=text, code=shift):
#     decrypted_message = ""
#     for ch in message:
#         old_index = alphabet.index(ch)
#         new_index = old_index - code
#         decrypted_message += alphabet[new_index]
#     print(f"The decoded text is {decrypted_message}.")


# if direction == "encode":
#     encrypt()
# elif direction == "decode":
#     decrypt()
