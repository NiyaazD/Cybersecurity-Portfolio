import bcrypt

# Function to hash a password
def hash_password(password):
    # Encode the password string into bytes
    encoded_password = password.encode()

    # Generate a random salt and hash the password
    hashed_password = bcrypt.hashpw(
        encoded_password,
        bcrypt.gensalt()
    )

    return hashed_password


# Ask the user for a password
user_password = input("Enter a password: ")

# Call the function
hashed = hash_password(user_password)

# Display the hashed password
print("\nHashed Password:")
print(hashed.decode())