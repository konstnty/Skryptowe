#!/bin/python
import rsa
# pub priv gen
(pubkey, privkey) = rsa.newkeys(2048)
with open('pubkey.key','wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))

with open('privkey.key','wb') as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))

#hash
def file_open(file):
    key_file = open(file,'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data

message = file_open('message')
hash_value = rsa.compute_hash(message,'SHA-512')
signature = rsa.sign(message,privkey, 'SHA-512')
s = open('signature','wb')
s.write(signature)
try:
    rsa.verify(message,signature,pubkey)
    print("Verified")
except:
    print("File Changed")
