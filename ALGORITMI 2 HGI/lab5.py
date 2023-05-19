#se da o lista de nr naturale, neg, poz, sa se calculeze maximul si minimul produsului care se poate face cu numerele respective
# folosind 2 numere din lista respectiva

# lista se parcurge cu UN SINGUR FOR
# matricea se parcurge cu 2 FOR ( FOR I IN RANGE, FOR J IN RANGE)

def min_max(l):
    min = l[0]
    max = l[0]
    for i in range(len(l)):
        if l[i]< min:
            min =l[i]
        if l[i]> max:
            max = l[i]
        if min >l[i]:
            l[i] = min2
        if max < l[i]:
            l[i] =max2


def min_max2():
    l = [1,20,3,40,5]
    l.sort()
    n=len(l)
    produs_max = l[n-1] * l[n-2]
    produs_min = l[0]*l[1]
    print(produs_min)
    print(produs_max)



#matrice patratica
def matrice_nume(matrice):
    lista= ['a', 'b', 'c', 'd']
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            print(lista[i],end = "")
            if matrice[i][j] == 1:
                print(lista[j])
            else:
                print("-")


if __name__ == "__main__":
    matrice_nume([[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,0,1]])



def my_function(my_string):
    print(my_string.upper())