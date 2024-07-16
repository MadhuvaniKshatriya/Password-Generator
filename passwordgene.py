import random
import string

def generate_password(length):
    """Generate a random password of a given length."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)
    
    return ''.join(password)

def generate_passwords(count, length):
    """Generate a list of passwords."""
    return [generate_password(length) for _ in range(count)]

def main():
    """Main function to run the password generator."""
    try:
        
        length = int(input("Enter the length of the password (minimum 8): "))
        count = int(input("Enter the number of passwords to generate: "))

        
        passwords = generate_passwords(count, length)

        
        print("\nGenerated Passwords:")
        for idx, password in enumerate(passwords, 1):
            print(f"{idx}: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
