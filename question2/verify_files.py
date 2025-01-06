import sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# get the shared key from previous calculations
from question1.generate_key_1b import key

from question2.hmac_sha256 import HMACSHA256






# the input file names are defined in the order defined in the document 

input_files = ['codes/tested_files/bit_manip_demo.py', 'codes/tested_files/lab 3.pdf', 'codes/tested_files/lecture 01.pdf',
               'codes/tested_files/python tutorial 2022--01-10.pdf', 'codes/tested_files/sha256_demo.py'  ]



# the output file names are also defined in the same way 
output_file_names = ['codes/hmac_key_outputs/bit_manip_hmac.b64', 'codes/hmac_key_outputs/lab3_hmac.b64', 
                     'codes/hmac_key_outputs/lecture1_hmac.b64', 'codes/hmac_key_outputs/python_tutorial_hmac.b64', 
                      'codes/hmac_key_outputs/sha256_demo_hmac.b64'
                       ]



# compute the HMAC for the above files store the hmacs in hmac and key outputs folder
for i in range(len(input_files)):
    hmac_obj= HMACSHA256()
    # generate inner and outer keys using the shared key
    # convert numpy array to bstring key
    inner_key, outer_key = hmac_obj.get_keys(key.tobytes())
    hmac_obj.generate_HMAC(input_files[i], output_file_names[i], inner_key, outer_key)


# display the HMAC generated for the python tutorial pdf 

# 2 a) 

# read 32 bytes of the HMAC (sha256 message digest)
with(open('codes/hmac_key_outputs/python_tutorial_hmac.b64', 'rb') as fourth_file  ):
    fourth_hmac = fourth_file.read(32)

print(f'The python tutorial base 64 encoded HMAC: {fourth_hmac}')






# 2 b) 


# test the given hmac with the computed hmacs to verify identity  

tested_signatures = ['codes/tested_signatures/sig1.b64', 'codes/tested_signatures/sig2.b64', 
                     'codes/tested_signatures/sig3.b64'
                     , 'codes/tested_signatures/sig4.b64', 'codes/tested_signatures/sig5.b64'
                     ]


for i in range(len(output_file_names)):
    hmac_obj= HMACSHA256()
    hmac_check= hmac_obj.verify_HMAC(output_file_names[i], tested_signatures[i])
    print(f'file name of the checked input: {input_files[i].split('/')[-1]}. Outcome of the check: ')
    if(hmac_check ):
        print('File check succeded')
    else: 
        print('File check failed')
    
    print('//////////////////////////////////////////////////////////')

