import re

password = input("Enter password: ")

pattern = r'^(?!\d)(?!.*(.)\1)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!])[A-Za-z\d@#$%&!]{8,15}$'

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")
