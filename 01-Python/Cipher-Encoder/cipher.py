def encode_message(message):
    encoded = ""
    shift = 15

    for character in message:
      # Handle lowercase letters
        if "a" <= character <= "z":
            base = ord("a")
            encoded += chr((ord(character) - base + shift) % 26 + base)

      # Handle uppercase letters
        elif "A" <= character <= "Z":
            base = ord("A")
            encoded += chr((ord(character) - base + shift) % 26 + base)

      # Keep spaces and punctuation unchanged
        else:
            encoded += character

    return encoded


message = input("Enter a message to encode: ")
encoded_message = encode_message(message)
print(encoded_message)