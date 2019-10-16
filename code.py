import StringIO
import os
import sys
import math

ACSII_A = 65
ACSII_Z = 90
ACSII_a = 97
ACSII_z = 122

def encode_ascii(content, encode_key):
    new_content = ''
    
    for x in xrange(0,len(content)):
        value = ord(content[x])
        
        key_index = x % len(encode_key)
        key_bit_value = ord(encode_key[key_index])
        delt_value = 0
        
        if key_bit_value >= ACSII_a and key_bit_value <= ACSII_z:
            delt_value = key_bit_value - ACSII_a
            pass
        elif key_bit_value >= ACSII_A and key_bit_value <= ACSII_Z:
            delt_value = key_bit_value - ACSII_A
            pass
        pass

        if value >= ACSII_a and value <= ACSII_z:
            value = value + delt_value
            if value > ACSII_z:
                value = ACSII_a + (value - ACSII_z - 1)
            pass
        elif value >= ACSII_A and value <= ACSII_Z:
            value = value + delt_value
            if value > ACSII_Z:
                value = ACSII_A + (value - ACSII_Z - 1)
            pass

        new_content = new_content + str(chr(value))
    
    return new_content

def decode_ascii(content, encode_key):
    new_content = ''
    
    for x in xrange(0,len(content)):
        value = ord(content[x])
        
        key_index = x % len(encode_key)
        key_bit_value = ord(encode_key[key_index])
        delt_value = 0
        
        if key_bit_value >= ACSII_a and key_bit_value <= ACSII_z:
            delt_value = key_bit_value - ACSII_a
            pass
        elif key_bit_value >= ACSII_A and key_bit_value <= ACSII_Z:
            delt_value = key_bit_value - ACSII_A
            pass
        pass

        if value >= ACSII_a and value <= ACSII_z:
            value = value - delt_value
            if value < ACSII_a:
                value = ACSII_z - (ACSII_a - value - 1)
            pass
        elif value >= ACSII_A and value <= ACSII_Z:
            value = value - delt_value
            if value < ACSII_A:
                value = ACSII_Z - (ACSII_A - value - 1)
            pass
        
        new_content = new_content + str(chr(value))
    
    return new_content



if __name__ == '__main__':
    func_type = sys.argv[1]
    content = sys.argv[2]
    key = sys.argv[3]

    if func_type == 'encode':
        print(encode_ascii(content, key))
    elif func_type == 'decode':
        print(decode_ascii(content, key))

# usage
# python code.py encode abcdefghijklmnopqrstuvwxyz test
