#!/bin/python

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    pad_l =16 - len(data)%16
    pad = bytes([pad_l] * pad_l)
    return data + pad

def encrypt(it, ot):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        with open(it, 'rb') as f:
            plaintext = f.read()
        padded_plaintext = pad(plaintext)
        ciphertext = cipher.encrypt(padded_plaintext)
        with open(ot, 'wb') as f:
            f.write(ciphertext)
        encoded_key = key.hex()
        encoded_iv = iv.hex()
        return encoded_key, encoded_iv
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None, None

if __name__ == "__main__":
    input_file = "random"
    encrypted_file = "EncryptedFile"
    decrypted_file = "DecryptedFile"

    # Encrypt the file
    key, iv = encrypt(input_file, encrypted_file)
    if key and iv:
        print("File encrypted successfully.")
        print("Key:", key)
        print("IV:", iv)
        #decrypt_file(key, iv, encrypted_file, decrypted_file)
        print("File decrypted successfully.")
    else:
        print("Encryption failed.")
