lista = [[0,1],[0,2],[1,2],[1,3],[3,4]]
def functie(lista):
    maxim= max(lista)+1
    m =[]
    for i in range(max):
        rand = []
        for j in range(max):
            rand.append(0)
        m.append(rand)
    print(m) # vizualizam matricea
    for element in lista:
        x= element[0]
        y= element[1]
        m[x][y] = 1
        m[y][x] = 1

#varianta 2:

def genf(matrice): # generare functie = genf
    l_f = []  # l_f = lista finala
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] ==1:
                l= [i,j]
                l_f.append(l)

# problema comis voiajor exemplu incercat









def max():
    maxim= 0
    for rand in lista:
        for element in rand:
            if element > maxim:
                maxim = element
    return maxim
