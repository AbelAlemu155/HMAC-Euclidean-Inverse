#!/usr/local/bin/python3
import numpy as np, base64, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cryptography.hazmat.primitives import hashes

from AES.util.key_file_util import read_key_file
from question2.sha256 import SHA256_c
vhex = np.vectorize(hex)


class HMACSHA256():
    def __init__(self):
        self.__inner_hash = SHA256_c()
        self.__outer_hash = SHA256_c()
    
    # inner and outer keys must be bstrings 
    def generate_HMAC(self,infile, hmac_file, keyI, keyO):
        # read the input file as chunks of 128 bytes
        num_bytes_chunk = 128 
        
        
        
        with open(infile, 'rb') as input_file:
            num_file_blocks_read=0 
            while(chunk:= input_file.read(num_bytes_chunk)):

                num_file_blocks_read+=1
                
                block_to_hash = chunk


                # if this is the first block read 
                if(num_file_blocks_read ==1):
                    # prepend inner key
                    
                    block_to_hash = keyI + block_to_hash
                
                # add to the hash values
                self.__inner_hash.push_data(block_to_hash)


        # the inner hash is completed for the whole file 
        inner_digest = self.__inner_hash.get_hash().tobytes()
        # prepend outer key
        outer_hash_to_compute = keyO + inner_digest
        # compute the outer hash in the nested hash
        self.__outer_hash.push_data(outer_hash_to_compute)
        final_digest = self.__outer_hash.get_hash().tobytes()


        # convert bstring to base64 encoding
        final_digest_b64= base64.b64encode(final_digest)
        # write it to HMAC_file 
        with(open(hmac_file, 'wb') as output_hmac_file):
            output_hmac_file.write(final_digest_b64)            


    # get validated key        
    def get_keys(self,key): 
        in_xor =  bytes.fromhex('36') * 32 # this hexadecimal value is xorred with a 32 byte key

        # perform xor
        inner_key=  bytes(a ^ b for a, b in zip(key,in_xor))
        out_xor= bytes.fromhex('5c') * 32

        # xor operation
        outer_key = bytes(a ^ b for a, b in zip(key,out_xor))

        return inner_key, outer_key
    
    # get validated hmac files 
    def verify_HMAC(self,hmac_file1, hmac_file2):
        hmac_bstr1= b''
        hmac_bstr2= b''
        with(open(hmac_file1, 'rb') as hmac1, open(hmac_file2, 'rb') as hmac2):
            hmac_bstr1= hmac1.read(32)
            hmac_bstr2= hmac2.read(32)
        return hmac_bstr1 == hmac_bstr2
    
    
    

