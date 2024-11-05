#in simple word encoding and decoding by shifting char
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

text = input("Enter the text: ")
shift = int(input("Enter shift value: "))

encrypted_message = encrypt(text, shift)
print(f"Encrypted text: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted text: {decrypted_message}")
