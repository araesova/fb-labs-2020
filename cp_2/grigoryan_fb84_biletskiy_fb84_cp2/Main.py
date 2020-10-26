import re
import math
import collections

alphabet = (
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
    'ч',
    'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ')
#sumletters = 0

letter_ord = 0
def sumabukv(text):
    sumletters = 0
    for i in text:
        for j in i:
            if j in alphabet:
                sumletters += 1
    return sumletters

message = open("filteredtext.txt", 'r', encoding="utf-8")
letters = re.findall(r'(?=([а-я," "]{1}))', message.read())  # ділим посимвольно ВТ.

# key = ("да", "нет", "липа", "зачем", "необразованый")
def encryption(key):
    #key = ("григорянанаперездачу")
    encr_mess = ""
    key *= sumabukv(letters) // len(key)  # розтягуєм ключ на всю довжину Відкритого тексту
    for i, j in zip(letters, key):
        # print(ord(i), "+", ord(j), "=", ord(i) + ord(j), "==", ((ord(i) + ord(j)) % 32 + 1072))  # по пріколу для перевірки.
        letter_ord = ord(i) + ord(j)
        encr_mess += chr(letter_ord % 32 + 1072)  # зашифрований текст
    print(encr_mess)

from collections import Counter

def index_vidpovidnosti(text,sum):
    sum=sumabukv(text)
    index = 0
    for t in Counter(text):  # для відкритого тексту замінити encr_mess на letters.
        N = text.count(t)  # кількість появи букви t у шифротексті.........для відкритого тексту замінити encr_mess на letters.
        index += N * (N - 1)  # чисельник
    index = index / (sum * (sum - 1))  # Індекс Відповідності тексту

    print('Індекс відповідності тексту: ', index)
    return index

a = 0
message1 = open("text.txt", 'r', encoding="utf-8")
letters1 = re.findall(r'(?=([а-я," "]{1}))', message1.read())

for i in letters1:
    a += 1
    if a % 30 == 0:
        print()
    else:
        print(i, " ", end="")

def blocks(text, num_block):
    newarr = []
    i = 0
    j = 0
    suma = 0
    while i < num_block:
        newarr.append("")
        i += 1
    for id in range(0, len(text)):
        newarr[id%num_block] += text[id]
    while j < num_block:
        indexforblocks = index_vidpovidnosti(newarr[j], newarr[j])
        j += 1

        # indexforblocks+=indexforblocks/num_block
        suma += indexforblocks / num_block
    print("Середнє", suma)
    return newarr


print()
index2=blocks(letters1,3)