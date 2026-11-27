import string
import msvcrt

print("=" * 42)
print("       ANMOLNEXUS PASSWORD CHECKER")
print("=" * 42)

common_passwords = [
    "password", "12345678", "admin",
    "qwerty", "password123", "admin123",
    "welcome", "letmein", "admin@123"
]

patterns = ["123", "234", "345", "abc", "qwerty"]


# Password input with asterisk masking
def get_password():
    print("\nEnter your password: ", end="", flush=True)
    password = ""

    while True:
        char = msvcrt.getwch()

        if char == "\r":
            print()
            break

        elif char == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        elif char in ("\x00", "\xe0"):
            msvcrt.getwch()

        else:
            password += char
            print("*", end="", flush=True)

    return password


# Get password
password = get_password()

print("\nPassword received successfully!")
print("Starting security analysis...\n")

score = 0
suggestions = []
is_weak = False

# Check password length
if len(password) < 8:
    is_weak = True
    suggestions.append("Use at least 8 characters.")

# Check common passwords
if password.lower() in common_passwords:
    is_weak = True
    suggestions.append("Avoid commonly used passwords.")

# Check uppercase letters
if any(c.isupper() for c in password):
    score += 1
else:
    suggestions.append("Add an uppercase letter.")

# Check lowercase letters
if any(c.islower() for c in password):
    score += 1
else:
    suggestions.append("Add a lowercase letter.")

# Check numbers
if any(c.isdigit() for c in password):
    score += 1
else:
    suggestions.append("Add a number.")

# Check special characters
if any(c in string.punctuation for c in password):
    score += 1
else:
    suggestions.append("Add a special character.")

# Check password length
if len(password) >= 12:
    score += 1
else:
    suggestions.append("Try using 12 or more characters.")

# Check repeated characters
for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        is_weak = True
        suggestions.append("Avoid repeating characters.")
        break

# Check predictable patterns
for pattern in patterns:
    if pattern in password.lower():
        is_weak = True
        suggestions.append("Avoid predictable patterns.")
        break

# Final security analysis
score = min(score, 5)

if is_weak or score <= 2:
    strength = "WEAK"
    score = min(score, 2)

elif score <= 4:
    strength = "MODERATE"

else:
    strength = "STRONG"

# Display results
print("=" * 42)
print("         SECURITY ANALYSIS")
print("=" * 42)

print("\nPassword Strength:", strength)
print("Security Score:", score, "/5")

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)
else:
    print("\nAll basic security checks passed!")

print("\nThank you for using ANMOLNEXUS :)")
print("=" * 42)