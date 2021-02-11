import re
import string
file = open("ad6.txt", "r")
x = file.read()

lista = x.split("\n\n")

nlis = []
for i in lista:
    x = re.sub("\\n", " ", i)
    nlis.append(x)

war = 0
for i in nlis:
    value = 0

    alfa = list(string.ascii_lowercase)
    k1 = i.split(" ")

    for letter in alfa:
        buka = 0
        for words in k1:
            if letter in words:
                # print(letter + " jest w " + words)
                buka += 1
            if buka == len(k1):
                war += 1
print(war)
