import re

alphabet = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я', ' ')


buffer = ''
sumletters = 0


a = input("1. letter counter / 2. letter frequency: \n")

if a == "1":
    for i in alphabet:
        result_file = open("filteredtext.txt",'r',encoding='utf-8')
        print(i, result_file.read().count(i))

if a == '2':
    result_file = open("filteredtext.txt", 'r', encoding='utf-8')
    for i in result_file:
        for j in i:
            if j in alphabet:
                sumletters += 1

    for i in alphabet:
        result_file = open("filteredtext.txt",'r',encoding='utf-8')
        print(i, result_file.read().count(i)/sumletters)


print("SUM: " + str(sumletters))
