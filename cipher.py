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
    #For docker un-comment the 2 lines below and add your password as string in the variable, further comment out the line above, this is due to docker limitations.
    #user_passwd=""
    #print(user_passwd)
    if "\x1dNRL[\x06qD[RD" == encrypt(key, user_passwd):
    	print("Success")
    else:
    	print("Please refrain from unauthorized access")
