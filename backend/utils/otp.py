import random
import string

def generate_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))