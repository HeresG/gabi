# sa se scrie o functie care realizeaza cautarea intr o lista ale carei valori pot fi nr naturale sau siruri de caractere/ litere
# si reintoarce functia elementul daca a fost gasit /pozitia elementului iar in caz contrar intoarce NONE.

def cautare(lista, element):
    n= len(lista)
    i = 0
    for i in range(n):
        if element == lista[i]:
            return element
    return None

if __name__ == '__main__':
    print(cautare())


