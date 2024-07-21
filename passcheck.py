import re


def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[@$!%*?&#]', password) is not None

    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Try making your password at least 8 characters long for better security.")
    if not upper_criteria:
        feedback.append("Adding at least one uppercase letter will make your password stronger.")
    if not lower_criteria:
        feedback.append("Including at least one lowercase letter helps improve your password.")
    if not digit_criteria:
        feedback.append("Including at least one number will boost your password's strength.")
    if not special_criteria:
        feedback.append("Adding a special character (@$!%*?&#) will make your password more secure.")

    return strength, feedback



password = input("Enter a password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
for comment in feedback:
    print(f"- {comment}")
