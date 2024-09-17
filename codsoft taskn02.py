[10:45 AM, 9/17/2024] Apoorva Srinivas: import random
import string

def generate_password(length=12):
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
