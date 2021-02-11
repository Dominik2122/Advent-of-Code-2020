import re
import numpy
file = open("ad5.txt", "r")
x = file.read()
DUPA = []
lista = x.split("\n")

dict = {
    "F" : 0,
    "B" : 1,
    "L" : 0,
    "R" : 1,
}
row = []
for i in range(128):
    row.append(i)

the_best = 0

for code in lista:
    row = []
    for i in range(128):
        row.append(i)
    column = []
    for i in range(8):
        column.append(i)

    for i in range(7):
        row = numpy.array_split(row,2)
        if code[i] == "F":
            row = row[0]
        else:
            row = row[1]
    for i in range(7,10):
        column = numpy.array_split(column,2)
        if code[i] == "L":
            column = column[0]
        else:
            column = column[1]
    rzad = row[0]
    kol = column[0]
    ID = rzad*8+kol
    if ID > the_best:
        the_best = ID
    DUPA.append(ID)
lista = []


porzadek = sorted(DUPA)

for i in porzadek:
    if i < len(porzadek)-3:
        if porzadek[i+2]-porzadek[i] != 2:
            print(porzadek[i+1])
