import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from AES.cbc_module.encrypt_cbc import encrypt_cbc
from generate_key_1b import key
import base64

# write the key to the file shared_key1b 
fd = open("codes/hmac_key_outputs/shared_key1b.b64", 'wb')
fd.write( base64.b64encode(key.tobytes() ) )
fd.close()

encrypt_cbc('codes/images/semien_mountain.jpg', 'images/encrypted_image.aes', key)
print(f'encryption completed!')

