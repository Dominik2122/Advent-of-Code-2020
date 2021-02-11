file = open("ad3.txt", "r")

lista = []
x = file.read()
x = x.split("\n")
def t(a,b):
    i = 0
    j = 0
    ilosc = 0

    while i < len(x):
        if j >= len(x[0]):
            j = j-len(x[0])
        else:
            pass

        if x[i][j] == "#":
            ilosc += 1

            i +=a
            j +=b
        else:
            i +=a
            j +=b

    return ilosc

print(t(1,1)*t(1,3)*t(1,5)*t(1,7)*(t(2,1)))
