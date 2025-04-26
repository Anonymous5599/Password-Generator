import random
import string

def generate_password(user_name="", length=12, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character sets selected."

    # Remove username from length count
    remaining_length = max(length - len(user_name), 4)  # ensure enough randomness

    random_part = ''.join(random.choice(characters) for _ in range(remaining_length))
    combined = list(user_name + random_part)
    random.shuffle(combined)  # shuffle to mix name and random parts
    password = ''.join(combined)
    return password
