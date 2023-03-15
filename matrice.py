def matrice1():
    n = 4
    sdp = 0
    sds = 0
    matrice = [[0]* n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i<j: # elementul este deasupra
                sdp += matrice[i][j]
            if i+j<n-1:
                sds += matrice[i][j]
    print("SDP=" , sdp)
    print("SDS=" , sds)


def matrice2():
    n = 2 #nr coloane
    m = 3 # nr linii
    matrice = [[0]* n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j] ** 2
    print(matrice)


def matrice3():
    n = 2 # nr coloane
    m = 3 # nr linii
    matrice = [[0]* n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j] + 10
    print(matrice)


def caut100():
    n= 5
    lista =[]
    for i in range(n):
        lista.append(int(input()))
    for i in range(n):
        if lista[i] == 100:
            print(i)


def cauta100inmatrice():
    n = 2 # nr coloane
    m = 2 # nr linii
    matrice = [[0]* n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i] == 100:
                print(i)
                if matrice[j] == 100:
                    print(i)
    print(matrice)


def sumapare():
    n = 2
    suma = 0
    matrice = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i // 2 == 0:
                suma += matrice[i][j]
                if j // 2 == 1 :
                    suma += matrice [i][j]
    print("suma pare=" , suma)
    print("suma impare=" , suma)


if __name__ == "__main__":
    sumapare()