# #presupunem existenta unei liste deja create . in lista dorim urmatoarele: pentru elementele a caror indice este mai mare de 5 , doresc sa se
# #calculeze jumatattea fiecrarui element, iar cu jumatatile sa se calculeze produsul lor, produsul jumatatilor
# # 2. in lista mea sa se faca cautarea unui element citit de la tastatura iar daca se gaseste elementul sa se calculeze o valoare de forma
# # functie = val *val/2 + val **4
# import math
#
# l = [10,20,30,40,50]
#
# def cautare():
#     valoare = int(input())
#     for i in range(len(l)):
#         if l[i] == valoare:
#             print(valoare*valoare/2 + valoare**4)
#
# def produs():
#     produs = 1
#     for i in range(len(l)):
#         if i>5:
#             produs = produs * l[i]/2
#     print (produs)
#
# def cautare_prin_salt():
#     l.sort()
#     n = len(l)
#     salt = int(math.sqrt(n))
#     val = int(input())
#     #identificam zona din lista unde se gaseste elementul pe care eu il preiau de la tastatura
#     for i in range(0,n,salt):
#         if l[i]<val:
#             start_lista_viitoare = i
#         elif l[i] ==val:
#             print(i)
#         else:
#             break
#     #am gasit zona din lista in care se gaseste elementul meu.. pot sa efectuez o cautare secventiala
#     flg = 0
#     for i in range(start_lista_viitoare,start_lista_viitoare+salt):
#         if l[i] == val:
#             print(i)
#             flg = 1
#     if flg == 0:
#         print("nu am gasit elementul")
#
#
# if __name__ =="__main__":
#   #  cautare()
#    # produs()
#     cautare_prin_salt()
#
#
#
#
# if __name__ == "__main__":
#     citire_fisier = open("pozitiiconsecutive.in", "r")
#     scriere_fisier = open("pozitiiconsecutive.out", "w")
#
#     n = int(citire_fisier.readline().strip())
#     f1 = 1
#     f2 = -1
#     for i in range(3, n + 1):
#         f3 = 1 - 2 * f2 - f1
#         if i != n:
#             f1 = f2
#             f2 = f3
#     for i in range(n + 1, 3, -1):
#         scriere_fisier.write(str(f3))
#         scriere_fisier.write(' ')
#         f1 = 1 - 2 * f2 - f3
#         f3 = f2
#         f2 = f1
#     scriere_fisier.write('-1 ')
#     scriere_fisier.write('1')
#
#
#
