import re

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[@$!%*?&#]", password):
        score += 1

    if score <= 2:
        return "Weak Password Hai Bhai Thoda Strong"

    elif score <= 4:
        return "Medium Password Thodu Aur Strong"

    else:
        return "Strong Password Ha Yeah Best Hai"


password = input("Enter your password: ")

result = check_password_strength(password)

print("Password Strength:", result)

