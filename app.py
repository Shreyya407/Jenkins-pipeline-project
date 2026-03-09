import re

def check_password_strength(password):

    length = len(password) >= 8
    upper = re.search("[A-Z]", password)
    lower = re.search("[a-z]", password)
    digit = re.search("[0-9]", password)
    special = re.search("[@#$%^&*!]", password)

    if length and upper and lower and digit and special:
        return "Strong Password"
    elif length and (upper or lower) and digit:
        return "Medium Password"
    else:
        return "Weak Password"


def main():
    print("Password Strength Checker")

    password = "D123!"

    strength = check_password_strength(password)

    print("Password:", password)
    print("Strength:", strength)


if __name__ == "__main__":
    main()