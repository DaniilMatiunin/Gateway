
from base64 import b64encode
from Crypto.Cipher import AES
import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(b'OYZFFF')
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'nonce': nonce, 'ciphertext': ct})
print(result)
{"nonce": "XqP8WbylRt0=", "ciphertext": "Mie5lqje"}



# We assume that the key was securely shared beforehand

try:
    b64 = json.loads('s')
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    pt = cipher.decrypt(ct)
    print("The message was: ", pt)
except (ValueError, KeyError):
    ''''''