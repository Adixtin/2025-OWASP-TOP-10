from crypto_utils import encrypt_data, decrypt_data

secret = "My SSN is 123-45-6789"

encrypted = encrypt_data(secret)
print("Encrypted:", encrypted)

decrypted = decrypt_data(encrypted)
print("Decrypted:", decrypted)
