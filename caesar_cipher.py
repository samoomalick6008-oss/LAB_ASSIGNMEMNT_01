
# Caesar Cipher Program
# This program encrypts and decrypts text using the Caesar Cipher technique.

def caesar_encrypt(text, shift):
    """Encrypts the given text using Caesar Cipher."""
    encrypted_text = ""  # Store encrypted result

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            # Shift character within A-Z range
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        # Check if character is lowercase letter
        elif char.islower():
            # Shift character within a-z range
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        else:
            # Keep spaces and special characters unchanged
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    """Decrypts the given ciphertext using Caesar Cipher."""
    # Decryption is just encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)


# Main Program Execution
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift_value)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift_value)
    print("Decrypted Message:", decrypted)
