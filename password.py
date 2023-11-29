import string
import random

def generate_password(length, use_letters, use_digits, use_punctuation):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one type of characters.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            use_letters = input("Include letters (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits (yes/no): ").lower() == 'yes'
            use_punctuation = input("Include punctuation (yes/no): ").lower() == 'yes'
            
            return length, use_letters, use_digits, use_punctuation
        except ValueError:
            print("Please enter a valid length (a positive integer).")
        except KeyboardInterrupt:
            print("\n\nExiting.")
            return None

def main():
    print("Welcome to the Random Password Generator!")
    user_input = get_user_input()
    if user_input:
        length, use_letters, use_digits, use_punctuation = user_input
        password = generate_password(length, use_letters, use_digits, use_punctuation)
        if password:
            print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()