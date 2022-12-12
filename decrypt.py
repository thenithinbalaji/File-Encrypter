import json
import os
import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def decrypt(tup):
    cipher = AES.new(tup[1], AES.MODE_EAX, tup[3])
    data = cipher.decrypt_and_verify(tup[0], tup[2])

    file = open("temp1.bin", "wb")
    file.write(data)
    file.close()

    os.remove(tup[4])
    os.rename("temp1.bin", tup[4])


print(
    """         
        ███████████████████████████████████████████
        █▄─▄▄▀█▄─▄▄─█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█
        ██─██─██─▄█▀█─███▀██─▄─▄██▄─▄███─▄▄▄███─███
        ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀
    """
)


print("\n\nWelcome To Decrypter")
print("Checking the existence of key.json in root...")

time.sleep(2)

try:
    with open("key.json", "r") as json_file:
        key_dict = json.load(json_file)

    print("key.json found. \nExtracting keys...")
    time.sleep(2)

    for i in key_dict:
        file = open(i, "rb")
        data = file.read()
        file.close()
        for vals in key_dict[i]:

            l = []

            for j in key_dict[i].values():
                a = bytearray()
                for k in j:
                    a.append(ord(k))
                byteString = bytes(a)
                l.append(byteString)

            tup = (data, l[0], l[1], l[2], i)
            decrypt(tup)

    print("\nDecryption Successful\n\n")

except FileNotFoundError:
    print(
        "FATAL ERROR: key.json not found. The key.json must be in same level as the application\n\n"
    )
