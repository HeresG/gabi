# 1. sa se def o functie care primeste ca si parametrii o lista de nr naturale si un nr natural si reintorace true daca
# il gasetse numarul in lista, altfel false

# listele se parcurg cu for
# matricile cu while, cand nu stiu nr elementee "cat timp"


# def p1(lista, n):
#     for i in range(len(lista)):
#         if lista[i] == n:
#             return True
#     return False


#2. sa se def o functie cae primeste ca si parametru o matrice si un nr nat si reintoarce true daca gaseste nr in matrice,
# si false daca nu gaseste

# def p2(matrice, nr):
#     m=len(matrice)
#     n=len(matrice[0])
#     matrice = [[0]* m for i in range(m)]
#     for i in range(m):
#         for j in range(n):
#            if matrice[i][j] == n:
#                return True
#     return False


#3.a sa se def o functie recursiva care calculeaza factorialul unui nr natural primit ca parametru
#b. sa se def o functie recursieva care calc suma digitilor unui nr n primit ca parametru
#c. sa se scrie o fucntie recursiva care numara de cate ori apare cifra 0 intre digitii unui nr natural

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)


def p3(n):  # suma digitilor numarului
    if n == 0:
        return n
    return n%10+p3(n//10)


# 4 BUBBLE SORT
def bubblesort(lista):
    flg = 1
    while flg ==1:
        flg = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                lista[i+1], lista[i] = lista[i], lista[i+1]
                flg= 1



if __name__ == '__main__':
   # print(factorial(60))
   print(p3(302))

