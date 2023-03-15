#citim T timp de la tastatura
# intr o lista M timpii pt masini
# M trebuie sortat
# T ramas = T
# while T ramas> 0:
# if M[i]< Tr
#    MM[j] = M[i]

def masini_reparatii():
    T = input('Timp total de lucru:' )
    M = [5,4,30,2,2,1,4,6]
    m_reparate = []
    M.sort()
    t_ramas = int(T)
    i = 0
    while t_ramas > 0 and i < len(M):
        if M[i] <= t_ramas:
            t_ramas = t_ramas - M[i]
            m_reparate.append(M[i])
        i= i+1
    print(m_reparate)
    print("timp ramas", t_ramas)


# suma elementelor unei liste folosind recursivitate
def suma(lista, stanga, dreapta):
    if stanga == dreapta:
        return lista[stanga]
    else:
        mijloc = (stanga + dreapta) //2
        return suma(lista, stanga, mijloc) + suma(lista, mijloc+1, dreapta)

def suma2(lista):
    if len(lista) == 1:
        return int(lista[0])
    else:
        mijloc = len(lista) //2
        return suma2(lista[:mijloc]+ suma2)


if __name__ == "__main__":
    masini_reparatii()

