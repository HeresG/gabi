def numere():
    print("Introduceti un numar natural:")
    x = input()
    contor = 0
    suma = 0
    for i in x:
        if i == "3":
            contor += 1


def sumapare():
    n = 2
    suma = 0
    matrice = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i // 2 == 0:
                suma += matrice[i][j]
    print("suma pare=" , suma)



def dictionar():
    ht = {}
    litere = ['a', 'b', 'c', 'd', 'e', 'f']
    lista_noua = ""
    i = 0
    for i in range(len(litere)):
        ht[litere[i]]=i


if __name__ == "__main__":
    numere()
    sumapare()
    dictionar()