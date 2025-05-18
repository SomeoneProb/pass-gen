
from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=20):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
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

@app.route('/generate-password')
def get_password():
    return jsonify({'password': generate_password()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
