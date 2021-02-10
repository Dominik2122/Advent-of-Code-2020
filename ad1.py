file = open("docx.txt", "r")

lista = []
x = file.read()
x = x.split("\n") #converting .txt into a list
ilosc_hasel = 0
for i in x:

    i = i.split(" ")
    szukana = i[1][0]
    ilosc = i[0]
    ilosc = ilosc.split("-")
    a = int(ilosc[0])
    b = int(ilosc[1])
    hop = 0
    if i[2][a-1] == szukana and i[2][b-1] != szukana:
        ilosc_hasel += 1
    elif i[2][a-1] != szukana and i[2][b-1] == szukana:
        ilosc_hasel += 1
    else:
        continue


print(ilosc_hasel)
