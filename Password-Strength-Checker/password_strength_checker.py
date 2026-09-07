import string
import secrets


# ---------------------------------------
# Check the strength of a password
# ---------------------------------------
def check_password(password):

    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MODERATE"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    # Display result
    print("\n" + "=" * 40)
    print("        PASSWORD ANALYSIS")
    print("=" * 40)

    print(f"Password Length     : {len(password)}")
    print(f"Uppercase           : {'Yes' if any(c.isupper() for c in password) else 'No'}")
    print(f"Lowercase           : {'Yes' if any(c.islower() for c in password) else 'No'}")
    print(f"Number              : {'Yes' if any(c.isdigit() for c in password) else 'No'}")
    print(f"Special Character   : {'Yes' if any(c in string.punctuation for c in password) else 'No'}")

    print("-" * 40)
    print(f"Score               : {score}/5")
    print(f"Strength            : {strength}")

    # Display suggestions
    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\n✓ Excellent password!")
        print("✓ Your password meets all basic requirements.")

    print("=" * 40)


# ---------------------------------------
# Generate a strong password
# ---------------------------------------
def generate_password():

    while True:
        try:
            length = int(input("\nEnter password length (8-20): "))

            if 8 <= length <= 20:
                break

            print("Please enter a length between 8 and 20.")

        except ValueError:
            print("Please enter a valid number.")

    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    all_characters = uppercase + lowercase + numbers + special

    # Make sure every type is included
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(special)
    ]

    # Add remaining characters
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle password
    secrets.SystemRandom().shuffle(password)

    password = "".join(password)

    print("\n" + "=" * 40)
    print("       GENERATED PASSWORD")
    print("=" * 40)
    print(password)
    print("=" * 40)


# ---------------------------------------
# Main program
# ---------------------------------------
def main():

    while True:

        print("\n" + "=" * 40)
        print("       PASSWORD STRENGTH CHECKER")
        print("=" * 40)

        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":

            password = input("\nEnter your password: ")

            if password == "":
                print("Password cannot be empty.")
            else:
                check_password(password)

        elif choice == "2":
            generate_password()

        elif choice == "3":
            print("\nThank you for using Password Strength Checker!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2 or 3.")


# Start program
if __name__ == "__main__":
    main()