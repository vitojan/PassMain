# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:53:55 2023

@author: VitoJan
"""

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from hashlib import md5

def calculate_md5(input_string):
    md5_hash = md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest().encode("utf-8")[:32]
    #return md5_hash.encode("utf-8")[:32]


def aes_256_encrypt(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return iv + ciphertext


def aes_256_decrypt(key, encrypted_data):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext

if __name__ == "__main__":
    
    print(calculate_md5("i"))
    
    print(type(calculate_md5("i")))
    
    #key = os.urandom(32)  # 生成一个随机的32字节密钥
    key = calculate_md5("i")
    key2 = calculate_md5("i")
    
    plaintext = b"123456"  # 要加密的明文
    
    encrypted_data = aes_256_encrypt(key, plaintext)
    
    decrypted_data = aes_256_decrypt(key, encrypted_data)
    
    
    
    print("Encrypted data:", encrypted_data.hex())

    print("Decrypted data:", decrypted_data.decode('utf-8'))
    for i in range(0,1000000000000000000):
        try:
            key2 = calculate_md5(str(i))
            #print("MD5_key_test : ", key2, end = "")
            decrypted_data2 = aes_256_decrypt(key2, encrypted_data)
            print("Decrypted data:", decrypted_data2.decode('utf-8'),i)
        except:
            #print(" Error")
            pass