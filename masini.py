def masini():
    fisier = open("masini.in", "r")
    linie = fisier.readline().strip().split(' ')
    n = linie[0]
    T = linie[1]
    timp_de_lucru = fisier.readline().strip().split(' ')
    fisier.close()
    n = int(n)
    T = int(T)
    timp_de_lucru.sort()
    nr_masini = 0
    i = 0
    # while T > 0 and T - int(timp_de_lucru[i]) >= 0  :
    #     T -= int(timp_de_lucru[i])
    #     nr_masini += 1
    #     i += 1
    for j in range(len(timp_de_lucru)):
        if T - int(timp_de_lucru[j]) >= 0:
            T -= int(timp_de_lucru[j])
            nr_masini += 1
        else:
            break
    scriere_fisier = open("masini.out", "w")
    scriere_fisier.write(str(nr_masini))
    scriere_fisier.close()

if __name__=="__main__":
    masini()