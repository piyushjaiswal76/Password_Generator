import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main password generator function
def password_generator():
    print("Random Password Generator")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        
        try_again = input("Generate another password? (yes/no): ").lower()
        if try_again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    password_generator()
