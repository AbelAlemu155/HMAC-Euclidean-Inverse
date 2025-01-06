
import os
def test_hmac_size(hmac_file):
    if(os.path.getsize(hmac_file) != 32):
        return False
    return True