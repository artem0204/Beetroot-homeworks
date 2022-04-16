# alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# smeshenie = int(input('Шаг шифровки: '))    #Создаем переменную с шагом шифровки
# message = input("Сообщение для шифровки: ").upper()    #создаем переменнную, куда запишем наше сообщение
# itog = ''    #создаем переменную для вывода итогового сообщения
# for i in message:
#     mesto = alfavit.find(i)    #Вычисляем места символов в списке
#     new_mesto = mesto + smeshenie
#     if i in alfavit:
#         itog += alfavit[new_mesto]  # Задаем значения в итог
#     else:
#         itog += i
# print(itog)
from socket import *

host = "localhost"
port = 9065
buffur_size = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((host, port))
print(f"the server {host}:{port} is working now ")


def shifr(msg, key):
    rez = ""
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            rez += chr((ord(char) + int(key) - 65) % 26 + 65)
        else:
            rez += chr((ord(char) + int(key) - 97) % 26 + 97)
    return rez


keys = {}
try:
    while True:
        connection_addres_pair = sock.recvfrom(buffur_size)
        msg1 = connection_addres_pair[0]
        adress = connection_addres_pair[1]
        print(f"Data from client {host}:{port}: {msg1.decode()}")
        if "key:" in msg1.decode():
            keys[adress[0]] = msg1.decode().split(":")[1]
            reply_from_server = str.encode(f"key: {keys[adress[0]]} was added")
            sock.sendto(reply_from_server, adress)
        else:
            rez = shifr(msg1.decode(), keys[adress[0]])
            reply_from_server = str.encode(f"your data were encripted by server. result:{rez}")
            sock.sendto(reply_from_server, adress)
finally:
    sock.close()
