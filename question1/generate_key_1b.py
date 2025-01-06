import numpy as np, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from AES.cbc_module.decrypt_cbc import decrypt_cbc
from question1.mod_ex import modExEfficient
# code for generating shared key 

p = 100035179
alpha = 22055634

u = 29109759

secret_exponent = 5765936
# compute alpha**secret_exponenet mod p
v = modExEfficient(alpha, secret_exponent, p)

shared_secret = modExEfficient(u, secret_exponent, p)
key =np.frombuffer(shared_secret.to_bytes(32, 'big'), np.uint8, -1)

if(__name__ == '__main__'):
    print(f'V computed is: {v}')
    print(f'Shared secret computed is: {shared_secret}')


    # decrypt the file prob1image.aes
    correct_file_name= decrypt_cbc('codes/images/prob1image.aes', key)
    print(f'prob1 file decoded to file name: {correct_file_name} ')







