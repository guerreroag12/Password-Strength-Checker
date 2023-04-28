import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter"

    # Check for digits
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit"

    # Check for special characters
    if not re.search("[!@#$%^&*()_+=\-{}\[\]:\";'<>?,./]", password):
        return False, "Password must contain at least one special character"

    return True, "Password is strong"

password = input("Enter password: ")
is_strong, message = check_password_strength(password)

if is_strong:
    print("Password is strong!")
else:
    print("Password is weak: ", message)
