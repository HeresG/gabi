def parcurgere_lista():
    l = list()
    for i in range(len(l)):
        print(l[i])
    for el in l:
        print(el)


# fiecare litera a alfabetului primeste o valoare key-value
# ex : a:200 , b:300 , c:1
# sa se calculeze pentru un cuvant, valoarea generata prin adunarea valorilor fiecarei litere
# ex : abc -> 501

def suma_cuvint(cuvint):
    ht = {'a' : 200 , 'b': 300, 'c': 1 , 'd': 40, 'e':50, 'f':60, 'g': 70, 'h':80, 'i':90, 'j': 1
    , 'k':2 , 'l':3 , 'm':4 , 'n': 5, 'o':6 , 'p':7 , 'r':8 ,'s':10 , 't':11 , 'u':12 , 'v':13 , 'w':14 , 'x':15 , 'y':16 , 'z':17 }
    suma = 0
    for element in cuvint:
        suma += ht[element]
    return suma


# se da o lista de nume ['ion', 'vasile', 'gheorghe', 'ioana', 'maria', 'ana']
# sa se determine care nume din aceasta lista genereaza valoarea cea mai mare conform problemei anterioare si sa se afiseze acel nume

def calcul_suma(lista):
    max = 0
    maxN = ''
    for element in lista:
        vc = suma_cuvint(element)
        if vc > max:
            max = vc
            maxN = element
    return maxN

def generare_ht(tip = 0):
    ht = {}
    litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
   # print(litere)
    listanoua = []
    start = 7
    for i in range(start, len(litere)):
       # print(litere[i], end= ',')
        listanoua.append(litere[i])
    for i in range(0, start):
       # print(litere[i], end= ',')
        listanoua.append(litere[i])
    for i in range(len(litere)):
        if tip ==0:
            ht[litere[i]] = listanoua[i]
        else:
            ht[listanoua[i]] = litere[i]
    return ht


def crypt_text(propozitie, tip =0):
    litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    ht = generare_ht()
    rezultat = ""
    for element in propozitie: # elementul din propozitie este o litera
        if element in litere:
            rezultat += ht[element]
        else:
            rezultat += element
    return rezultat


if __name__ == "__main__":
#   print(suma_cuvint('blabla'))
#   print(calcul_suma(['ion', 'vasile', 'gheorghe', 'ioana', 'maria', 'anamaria']))
    print(generare_ht())
    # prop = input(" propozitie:")
    # c = crypt_text(prop)
    # print(c)
    # d = crypt_text(c,1)
    # print(d)


