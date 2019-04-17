import math


def tamanho(x):
    x = abs(int(x))
    if x == 0:
        return 1
    else:
        return math.floor(math.log10(x)) + 1


def tamanhomaior(lista):
    z = 0
    for x in range(len(lista)):
        y = tamanho(lista[x])
        if y > z:
            z = y
        else:
            continue
    return z


def countradizdifsize(lista):
    x = 1
    listafinal = []
    while x < tamanhomaior(lista) + 1:
        y = 0
        lista2 = []
        while y < len(lista):
            if tamanho(lista[y]) == x:
                lista2.append(lista[y])
            y = y + 1
        listafinal.append(countradiz(lista2))
        x = x + 1
    print(listafinal)


def countradizdifsize2(lista):
    x = 1
    listafinal = []
    while x < tamanhomaior(lista) + 1:
        y = 0
        lista2 = []
        while y < len(lista):
            if tamanho(lista[y]) == x:
                lista2.append(lista[y])
            y = y + 1
        a = countradiz(lista2)
        z = 0
        while z < len(a):
            listafinal.append(a[z])
            z = z + 1
        x = x + 1
    print(listafinal)


def countradiz(lista):
    x = tamanhomaior(lista) - 1
    listafinal = lista.copy()
    while x != -1:
        countlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        y = 0
        xlista = []
        while y < len(lista):
            xlista.append(int(str(lista[y])[x]))
            y = y + 1
        z = 0
        while z < 10:
            countlist[z] = xlista.count(z)
            z = z + 1
        z = 0
        while z < 10:
            if z == 0:
                countlist[z] = countlist[z]
            else:
                countlist[z] = countlist[z - 1] + countlist[z]
            z = z + 1
        y = len(lista) - 1
        while y >= 0:
            z = int(str(lista[y])[x])
            listafinal[countlist[z] - 1] = lista[y]
            countlist[z] = countlist[z] - 1
            y = y - 1
        x = x - 1
        lista = listafinal.copy()
    print(listafinal)
    return listafinal


c = [40000000, 65, 122, 80, 880, 670, 30, 288, 8, 260]
countradizdifsize2(c)