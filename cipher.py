def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

if __name__ == '__main__':
    key = 'The_key'
    
    print("Please enter password for admin: ")
    user_passwd=input()
    if "\x1dNRL[\x06qD[RD" == encrypt(key, user_passwd):
    	print("Success")
    else:
    	print("Please refrain from unauthorized access")
