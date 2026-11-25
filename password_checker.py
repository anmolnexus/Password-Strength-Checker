import string

print("=" * 40)
print("       ANMOLNEXUS | PASSWORD CHECKER")
print("=" * 40)

password = input("\nEnter your password: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add an uppercase letter.")

if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add a lowercase letter.")

if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add a number.")

if any(char in string.punctuation for char in password):
    score += 1
else:
    feedback.append("Add a special character.")

print("\n--- SECURITY ANALYSIS ---")

if score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MODERATE")
else:
    print("Password Strength: STRONG")

print(f"Security Score: {score}/5")

if feedback:
    print("\nSuggestions:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("\nGreat! All basic security checks passed.")

print("\nThank you for using AnmolNexus.")