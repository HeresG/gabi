l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z']
l2 = ['f', 'g', 'h', 'i', 'j', 'k' , 'l' , 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z''a', 'b', 'c', 'd', 'e']


def adunareelementelista():
    s = 0
    for i in range(len(lista)):
        s +=lista(i)
    return s


def adunare(*argumente):          #*argumente este o lista
    # o functie intotdeauna foloseste return OBLIGATORIUUU
    # daca nu are return atunci e metoda
    s = 0
    for element in argumente:
        s += element
    return s

def produs(*argumente):
    p = 1
    for element in argumente:
        p *= element
    return p

def factorial(n):
    f = 1
    for i in range(1,n+1):
       f *= i
    return f

def cautare(listadecaractere,caracter):  #functia reintoarce un index
    for i in range(len(listadecaractere)):
        if listadecaractere(i) == caracter:
            return i
    return -1


def crypt(plaintext):     # reintoarce textul criptat
    text = ""
    for element in plaintext:
        i = cautare(l1, e)           # am gasit indexul in lista l2
        if element not in ["", 1,2,3,4,5,6,7,8,9,0]:
            text += l2 + i
        else:
            text += element
    return text






if __name__ == "__main__":



  #  text = "hello world"
   # ctext = crypt(text)
  #  print(ctext)


 #   print(produs(1,2))
 #   print(produs(1))
 #   print(produs())
  #  print(produs(1,2,3,4,5,6,7,8,9))
  #  print(factorial(3))
