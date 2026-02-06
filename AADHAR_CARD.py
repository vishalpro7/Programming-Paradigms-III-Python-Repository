import re

aadhaar = input("Enter Aadhaar number: ")
pattern = r'^[2-9]\d{11}$|^[2-9]\d{3}(?:\s\d{4}){2}$'

if re.fullmatch(pattern, aadhaar):
    print("Valid Aadhaar Number")
else:
    print("Invalid Aadhaar Number")
