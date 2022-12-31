import argparse
import string
import secrets
import math
from clint.textui import colored

# Argument parsing

parser = argparse.ArgumentParser(description='Generates a password of a given length')
parser.add_argument('-l', '--length')
args = parser.parse_args()

# Password generation

characterSetLength = len(string.ascii_letters + string.digits + string.punctuation)

def generate():
    characters = string.ascii_letters + string.digits + string.punctuation
    length=int(args.length)
    return ''.join(secrets.choice(characters) for i in range(length))

# Entropy calculation

def entropyCalc(passwordLength, characterSetLength):
    possibilities = characterSetLength ** passwordLength
    return math.log2(possibilities)

password = generate()
passwordLength = len(password)
entropy = entropyCalc(passwordLength, characterSetLength)

# Strength based on KeePassXC entropy classification

if entropy<40:strength=colored.red("Bad")
elif entropy<65:strength=colored.yellow("Weak")
elif entropy<100:strength=colored.cyan("Good")
else:strength=colored.green("Excellent")

print(f"Your password is:\n{password}\nEntropy: {round(entropy,2)} bits | Password is {strength}")