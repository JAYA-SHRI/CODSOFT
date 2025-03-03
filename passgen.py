import random
import string

def generate_password(length):
    if length < 5:
        print("Password length should be at least 5 characters.")
        return None

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    all_characters = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)

    # Fill the rest of the password length with random choices from all sets
    password += ''.join(random.choices(all_characters, k=length-4))

    # Shuffle the password to avoid predictable patterns
    password = ''.join(random.sample(password, len(password)))

    return password

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
