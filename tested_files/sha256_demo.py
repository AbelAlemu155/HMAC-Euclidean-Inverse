#!/usr/local/bin/python3
import numpy as np
import sys
import math
from numpy import linalg as LA
import os
from cryptography.hazmat.primitives import hashes
vhex = np.vectorize(hex)

class SHA256_c(object):
  def __init__(self):
    self.__digest = hashes.Hash(hashes.SHA256())

  def push_data(self, data_block):
    self.__digest.update(data_block)
  
  def get_hash(self):
    return( np.frombuffer(self.__digest.finalize(), np.uint8, -1) )
  
# MAIN STARTS HERE
# Note that either python b strings or numpy arrays can be used as input

# can push_data() using different sizes
myHash = SHA256_c()
mydata = np.asarray([i%256 for i in range(2149)], np.uint8)
myHash.push_data( mydata[0:123] )
myHash.push_data( mydata[123:124] )
myHash.push_data( mydata[124:1765] )
myHash.push_data( mydata[1765:] )
h = myHash.get_hash()
print(f"h = {vhex(h)}")

# can push_data() of an entire array at once.  Here a b string is used
# as input, but it could have just been the array mydata.  b string's were
# used just to show the flexibility
myHash1 = SHA256_c()
myHash1.push_data( mydata.tobytes() )
h1 = myHash1.get_hash()
print(f"h1 = {vhex(h1)}")

# test vectors from: https://www.di-mgt.com.au/sha_testvectors.html
myHash2 = SHA256_c()
testvec = "abc".encode()
myHash2.push_data( testvec )
h2 = myHash2.get_hash()
print(f"h2 = {vhex(h2)}")

myHash3 = SHA256_c()
testvec = "".encode()
myHash3.push_data( testvec )
h3 = myHash3.get_hash()
print(f"h3 = {vhex(h3)}")
