import random
import string

def generate_password(length=20):
    # Define character sets
    letters = string.ascii_letters  # both uppercase and lowercase letters
    digits = string.digits  # numbers
    special_chars = "@!#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all characters
    all_chars = letters + digits + special_chars
    
    # Ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest randomly
    for _ in range(length - 3):
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    
    # Join characters into string
    return ''.join(password)

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)
