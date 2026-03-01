import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
KEY = b"brainrotyJakies8"


def encrypt_data(plaintext: str) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(
            algorithms.AES(KEY),
            modes.CBC(iv),
            backend=default_backend
    )
    encrytpor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encrytpor.update(padded_data) + encrytpor.finalize()

    return iv + ciphertext


def decrypt_data(ciphertext: bytes) -> str:
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(
            algorithms.AES(KEY),
            modes.CBC(iv),
            backend=default_backend()
    )

    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()
