import json
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)


def enc(inp):
    data = inp
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (ciphertext, tag, cipher.nonce)


data_dict = {}

print(
    """
        █████████████████████████████████████████████
        █▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█
        ██─▄█▀██─█▄▀─██─███▀██─▄─▄██▄─▄███─▄▄▄███─███
        ▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀
    """
)


print(
    "\n\n\nWelcome To Rijndael Encrypter. Enter the folder name of the folder to be encrypted in the below prompt"
)
print("NOTE 1:: The folder must be present in root of the application.")
print(
    "NOTE 2:: All the files present in the folder as well as it's subfolders will be encrypted."
)
print("NOTE 3:: Works best in encrypting txt, pdf, png, jpg files.\n")

folder_name = input("Enter Folder Name:: ")

print("\n\nChecking folder existence... \n\n")

if not os.path.exists(folder_name):
    print(
        "Folder Doesn't Exist \n\nThe folder must be there in root of this application/program.\n"
    )

else:
    print("GG! The Folder exists \n")

    for (root, dirs, files) in os.walk(folder_name, topdown=True):
        for file in files:
            path1 = root + "\\" + file

            f = open(path1, "rb")
            inp = f.read()
            f.close()

            fl = open("temp.bin", "wb")
            add = enc(inp)
            fl.write(add[0])
            fl.close()

            a = bytearray(key)
            key1 = "".join(chr(x) for x in a)

            a = bytearray(add[1])
            tag1 = "".join(chr(x) for x in a)

            a = bytearray(add[2])
            nonce1 = "".join(chr(x) for x in a)

            os.remove(path1)
            os.rename("temp.bin", path1)
            data_dict[path1] = {
                "key": key1,
                "tag": tag1,
                "nonce": nonce1,
            }

    print()

    with open("key.json", "w") as fp:
        json.dump(data_dict, fp)

    print(
        "Encryption Successful and the key is stored in key.json. \nNOTE 4:: In order to decrypt the folder, copy the key.json to root and run the decryption algorithm (decrypt.py file).\nNOTE 5:: A folder can't be decrypted without the key.json file.\n"
    )
