# avem o matrice de dim n x m , sa se determine valoarea minima si maximul elementelor din matricea mea

def matrice_min_max(matrice):
    m= len (matrice)
    n =len (matrice[0])
    min = matrice[0][0]
    max = matrice[0][0]
    for i in range(m):
        if matrice[i][j]> max:
            max= matrice[i][j]
            if matrice[i][j] < min:
                min = matrice[i][j]
    print(" max" , max)
    print(" min" , min)


#EX2
def matrice_completeaza(matrice):
    m = len(matrice)
    n = len(matrice[0])
    #  se se completeze matricea dupa regula
    # daca produsul indicilor este par atunci completeaza valoarea 1
    # daca produsul indicilor este impar completeaza 0
    # daca elementul este pe diagonala principala atunci compl 2
    # elementul este matrice[indice] , i j sunt indicii matrice

    for i in range(m):
        for i in range(n):
            if i==j:
                matrice[i][j] = 2
            elif i*j % 2 == 0:
                matrice[i][j] = 1
            else:
                matrice[i][j] = 0


# merge_sort
def merge(left, right):
    i, j = 0,0
    while i< len(left) and j < len(right):
        if len[i] <=right[i]:
            result.append(left[i])




if __name__ == "__main__":
    matrice_completeaza()
   # matrice_min_max()

