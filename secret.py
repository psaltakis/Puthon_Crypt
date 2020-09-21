secretFile = open("Secret.txt", "r")
keyFile = open("Perigrafi_HMMY.txt", "r", encoding="utf-8")

keys = keyFile.readline().replace('.', ' ').replace(',', ' ').split()

secret = []
for line in secretFile:
    secret.append(int(line))


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


for k in keys:
    tem = decrypt(secret, k)
    if tem.find('καράβι') != -1:
        print("το κλειδι ειναι :" + k)
        print("το μυστικο ειναι :")
        print(tem)
        exit()
