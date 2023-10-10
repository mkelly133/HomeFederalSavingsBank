
'''
Implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''

# Get input from the user
greeting = input("Greeting: ")

# TODO work out if the greeting starts with an H or a Hello
if greeting.upper() == 'HELLO':
    payment = "$0"
elif greeting[0].upper() == 'H':
    payment = "$20"
else:
    payment= "$100"

# Outline payout
print(payment)
