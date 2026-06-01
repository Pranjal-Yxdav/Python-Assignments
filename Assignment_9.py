import re

username = input("Enter Username: ")
mobile = input("Enter Mobile Number: ")
email = input("Enter Email Address: ")
password = input("Enter Password: ")

username_pattern = r'^[A-Za-z0-9_]{5,15}$'
mobile_pattern = r'^[6-9]\d{9}$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

if re.match(username_pattern, username):
    print("Valid Username")
else:
    print("Invalid Username")

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")


text = "My marks are 85, 90 and 95"

numbers = re.findall(r'\d+', text)

print(numbers)

date = "27-05-2026"

pattern = r'^\d{2}-\d{2}-\d{4}$'

if re.match(pattern, date):
    print("Valid Format")

