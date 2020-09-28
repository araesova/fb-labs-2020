import re
import math
alphabet = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я', ' ')
sum = 0
sumletters = 0

result_file = open("filteredtext.txt",'r',encoding='utf-8')

a = input("1. W/ Spaces / 2. W/out Spaces: ")
b = input("1. Step one / 2. Step two: ")

if a == "1" and b == "1":
    print("W/ Spaces, Step one")
    from collections import Counter
    bigram = re.findall(r'(?=([а-яА-Я, ' ']{2}))', result_file.read())
    bigram.sort()
    for i in Counter(bigram):
        result_file = open("filteredtext.txt", 'r', encoding='utf-8')
        n = result_file.read().count(i) / 1484696
        print(i, round(n,7))
        sum = sum + n
        formula = (-sum) * math.log2(n)
    print(round(formula, 4))

if a == "1" and b == "2":
    print("W/ Spaces, Step two")
    from collections import Counter
    bigram = re.findall(r'([а-яА-Я, ' ']{2})', result_file.read())
    bigram.sort()
    for i in Counter(bigram):
        result_file = open("filteredtext.txt", 'r', encoding='utf-8')
        n = result_file.read().count(i) / 1484696
        print(i, round(n, 6))
        sum = sum + n
        formula = (-sum) * math.log2(n)
    print(round(formula, 4))

if a == "2" and b == "1":
    print("W/out Spaces, Step one")
    from collections import Counter
    bigram = re.findall(r'(?=([а-яА-Я]{2}))', result_file.read())
    bigram.sort()
    for i in Counter(bigram):
        result_file = open("filteredtext.txt", 'r', encoding='utf-8')
        n = result_file.read().count(i) / 1484696
        print(i, round(n, 6))
        sum = sum + n
        formula = (-sum) * math.log2(n)
    print(round(formula, 4))

if a == "2" and b == "2":
    print("W/out Spaces, Step two")
    from collections import Counter
    bigram = re.findall(r'([а-яА-Я]{2})', result_file.read())
    bigram.sort()
    for i in Counter(bigram):
        result_file = open("filteredtext.txt", 'r', encoding='utf-8')
        n = result_file.read().count(i) / 1484696
        print(i, round(n, 6))
        sum = sum + n
        formula = (-sum) * math.log2(n)
    print(round(formula, 4))
