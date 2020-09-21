def encrypt(txt_message, key):
    ret = []
    j = 0
    for i in range(len(txt_message)):
        if j == len(key):
            j = 0
        ret.append(ord(txt_message[i]) + ord(key[j]))
        j = j + 1
    return ret


def decrypt(encrypted_message, key):
    ret = ""
    j = 0
    for i in range(len(encrypted_message)):
        if j == len(key):
            j = 0
        if ord(key[j]) > encrypted_message[i]:
            continue
        ret = ret + '' + chr(encrypted_message[i] - ord(key[j]))
        j = j + 1
    return ret


message = input('Δωσε το μυνημα που θες να κρυπτογραφισεις: ')
key = input('δωσε το κλεισι κρυπτογραφησης: ')

print('κρυπτογραφημενο μυνημα:')
print(encrypt(message, key))
print('αποκρυπτογραφημενο :')
print(decrypt(encrypt(message, key), key))
