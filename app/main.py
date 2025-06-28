import os
from encrypt import Encryptor
from decrypt import Decryptor

class FileAdapter:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self) -> bytes:
        with open(self.filename, 'rb') as f:
            return f.read()
        
ORIGINAL_FILE = 'data/frame.png'
ENCRYPTED_FILE = 'data/image-encrypted.bin'
DECRYPTED_FILE = 'data/image-decrypted.png'

key = 'obvious_key'

# Encryption
encryptor = Encryptor(key)
original_adapter = FileAdapter(ORIGINAL_FILE)
encrypted_data = encryptor.encrypt(original_adapter)

with open(ENCRYPTED_FILE, 'wb') as f:
    f.write(encrypted_data)

print("Encrypted")

# Decryption
decryptor = Decryptor(key)
encrypted_adapter = FileAdapter(ENCRYPTED_FILE)
decrypted_data = decryptor.decrypt(encrypted_adapter)

with open(DECRYPTED_FILE, 'wb') as f:
    f.write(decrypted_data)

print("Decrypted")

# Verification
with open(ORIGINAL_FILE, 'rb') as f:
    original_bytes = f.read()

if original_bytes == decrypted_data:
    print("Decrypted image matches the original")
else:
    print("Decrypted PNG doesn't match the original")