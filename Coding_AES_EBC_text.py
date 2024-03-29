import random
import struct
from Crypto.Cipher import AES
import os
'''key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
print('key', [x for x in key])
iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

aes = AES.new(key, AES.MODE_CBC, iv)
sz=2048
fsz = os.path.getsize('example.txt')

with open('example.txt') as fin:
    while True:
        data = fin.read(sz)
        n = len(data)
        if n == 0:
            break
        elif n % 16 != 0:
            data += ' ' * (16 - n % 16) # <- padded with spaces
        encd = aes.encrypt(data)
        fout.write(encd)'''
'''from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
f=open('example.txt','rb')
data=str(f)




key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR)
cipher_text = cipher.encrypt(data)
nonce = cipher.nonce

decrypt_cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
plain_text = decrypt_cipher.decrypt(cipher_text)
print(data)
print(cipher_text)
print(plain_text)
''''''
from Crypto.Cipher import AES
import binascii, os
import random, string

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print('Key:', key)

encryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, 'Это IV-12'.encode("utf8"))
decryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, 'Это IV-12'.encode("utf8"))


def aes_encrypt(plaintext):
    ciphertext = encryptor.encrypt(plaintext)


return ciphertext


def aes_decrypt(ciphertext):
    plaintext = decryptor.decrypt(ciphertext)


return plaintext

encrypted = aes_encrypt('Это секретное сообщение '.encode("utf8"))
decrypted = aes_decrypt(encrypted)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted.decode())'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(plaintext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext and encrypt it
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data


# Example usage
plaintext = b"This is the message to be encrypted"
# Generate a random 256-bit (32-byte) key
# Key-length accepted: 16, 24, and 32 bytes.
key = get_random_bytes(32)  # Generating keys/passphrase
print("Key:", key.hex())
# Encryption
encrypted_data = encrypt(plaintext, key)
print("Encrypted data:", encrypted_data)
# Decryption
decrypted_data = decrypt(encrypted_data, key)
print("Decrypted data:", decrypted_data)