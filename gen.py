import argparse
import string
import secrets

# Argument parsing

parser = argparse.ArgumentParser(description='Generates a password of a given length')

parser.add_argument('-l', '--length')

args = parser.parse_args()

# Password generation

characters = string.ascii_letters + string.digits + string.punctuation
length=int(args.length)

password = ''.join(secrets.choice(characters) for i in range(length))

print(password)