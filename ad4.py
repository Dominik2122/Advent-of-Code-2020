import re
file = open("ad4.txt", "r")
x = file.read()
x = x.split("\n\n")
lista = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = []
correct_pass = 0
for i in x:
    i = i.rstrip("\n")
    ilosc_warunkow = 0
    for warunek in lista:
        szukacz = re.search(warunek, i)
        if szukacz:
            ilosc_warunkow += 1
        if ilosc_warunkow == 7:
            passports.append(i)

lista = []
for i in passports:
    x = re.sub(r"\n", " ",i)
    lista.append(x)

ilosc = 0
for i in lista:
    ilosc_warunkow = 0
    x = i.split(" ")
    obiekt = {}
    for cechy in x:
        tup = re.search(":", cechy).span()
        obiekt[cechy[:tup[0]]] = cechy[tup[0]+1:]

    if int(obiekt.get('byr'))>1919 and int(obiekt.get('byr'))<2003:
        ilosc_warunkow +=1

    if int(obiekt.get('iyr'))>2009 and int(obiekt.get('iyr'))<2021:
        ilosc_warunkow +=1

    if int(obiekt.get('eyr'))>2019 and int(obiekt.get('eyr'))<2031:
        ilosc_warunkow +=1

    if obiekt.get('hgt')[-2:] == "cm":
        if int(obiekt.get('hgt')[:-2])>149 and int(obiekt.get('hgt')[:-2])<194:
            ilosc_warunkow +=1
    elif obiekt.get('hgt')[-2:] == "in":
        if int(obiekt.get('hgt')[:-2])>58 and int(obiekt.get('hgt')[:-2])<77:
            ilosc_warunkow +=1
    if obiekt.get('hcl')[0] == "#" and len(obiekt.get('hcl'))==7:
        literki = 0
        for i in range(7):
            if obiekt.get('hcl')[i] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                literki += 1
        if literki == 6:
            ilosc_warunkow +=1
    if obiekt.get('ecl') in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:

        ilosc_warunkow +=1
    if len(obiekt.get('pid'))==9:
        ilosc_warunkow +=1

    if ilosc_warunkow == 7:
        ilosc += 1



print(ilosc)
