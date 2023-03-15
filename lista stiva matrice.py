def lista():
    l = [100, 1001, 348, 200, 500, 10, 40, 128]
    print(l)
    # suma elementelor din a doua jumatate a listei
    suma = 0
    for i in range(len(l)):
        if i >= len(l) // 2 :
            suma += l[i]
    print("suma elementelor din a doua jumatate este:", suma)
    # suma elementelor mai mari decat 200
    suma = 0
    for element in l:
        if element > 200:
            suma += element
    print("suma elementelor mai mari decat 200 este:" , suma)
    l.append(156)
    l.append(45)
    l.append(900)
   # l.insert(0, 10000000)
    for i in range (len(l)):
        print("l[",i,"]=", l[i], end=",")
    l.pop()
    print("")
    print(l)
    l.pop()
    print(l)
    l.pop(0)
    print(l)

def exemplu_deque():
    from collections import deque
    l2 = deque()
    l1 = list()
    l1.append(100)
    l2.append(100)
    l1.append(100000)
    l2.append(100000)
    l1.append(158)
    l2.append(158)
    l1.append(300)
    l2.append(300)
    l1.append(10)
    l2.append(10)
    print(l1)
    print(l2)
    l1.append(5)
    l2.append(5)
    print(l1)
    print(l2)
    l2.pop()
    print(l2)


def matrice():
   # matrice = []    #fiecare element al listei mele este la randul sau o lista
    nr_randuri = 3
    nr_coloane = 3
    matrice=[[0]* nr_coloane for k in range(nr_randuri)]
    print(matrice)
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            print("(", i, ",", j,")=" , end="")
            matrice[i][j] = int(input())

    for i in range(nr_randuri):
        print("|" , end="")
        for j in range(nr_coloane):
            print("(",i, ",", j,")=", matrice[i][j], end="")
            print("|", end="")
            print("")

    suma = 0
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if i==j :
                suma += matrice[i][j]
    print(suma)

    lista_suma_coloane = [0] * nr_coloane
    for i in range(nr_randuri):
       for j in range(nr_coloane):
           lista_suma_coloane[j] += matrice[i][j]
           print(lista_suma_coloane)





if __name__ == "__main__":
   lista()