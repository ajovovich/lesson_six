#Task 1: Input Length Validator
import re
while True:
    user_first_name = input("Enter your first name")
    user_last_name = input("Enter your last name")

    if len(user_first_name) < 2:
        print("Error: First name not long enough")

    if len(user_last_name) < 2:
        print("Error: Last name not long enough")

    retry_name = input("Do you want to re-enter your name? (yes/no)").lower()
    if retry_name != "yes":
        break

#Task 2: Password Complexity Checker

def password_checker(password):
    if len(password) < 8:
        return "Your password must contain at least 8 characters"
    if not re.match('.*[0-9]', password):
        return "Your password must contain a number"
    if not re.match('.*[A-Z]', password):
        return "Your password must contain 1 UPPER case letter"
    if not re.match(".*[a-z]", password):
        return "Your password must contain 1 lower case letter"
    return ("Your password is accepted")

password = input("Enter your password here")
message = password_checker(password)
print(message)

#Task 3: Email Formatter

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

def email_validator(email):
    if re.fullmatch(regex, email):
        return True

    else:
        return False

email = input("Type in your email address here")
user_email = email_validator(email)

if user_email:
    print("Valid email Format")
else:
    print("Invalid Email Format")

    
        