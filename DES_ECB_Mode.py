from DES import *


def encrypt_des_ecb_mode(plaintext, key, rounds_number):
    result = ""
    i = 0
    while i < len(plaintext):
        # convert to binary
        block = plaintext[i:i+8]
        block = string_to_binary(block)
        block = list(block)  # convert to list
        result += encrypt_des(block, key, rounds_number)[2:]
        i += 8
    return result


def decrypt_des_ecb_mode(plaintext, key, rounds_number):
    result = ""
    i = 0
    while i < len(plaintext):
        block = plaintext[i:i+16]
        # convert to binary and split plain text to 64 bit blocks and operate DES on any of them
        block = hex_to_binary(block)
        block = list(block)
        result += decrypt_des(block, key, rounds_number)[2:]
        i += 16
    return result


msg = "Hermioneeee!!@$%RD$$$%ghghg" \
      "" \
      "" \
      "" \
      "" \
      "hghghghghghghgggjfjtg     55533"
key = "d1D3!7$%"
res = encrypt_des_ecb_mode(msg, key, 16)
print("enc: " + res)
q = hex_to_ascii(decrypt_des_ecb_mode(res,key,16))
print("dec: " + q)