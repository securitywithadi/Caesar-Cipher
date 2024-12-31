def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    return ''.join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else
        chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char
        for char in text
    )

# Encrypt and Decrypt example
encrypted = caesar_cipher("Hello, World!", 3)
decrypted = caesar_cipher(encrypted, 3, decrypt=True)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
