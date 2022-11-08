def adunare2():
    print("Introduceti va rog un numar natural de doua cifre:")
    x = int(input())
    z = x // 10
    u = x % 10
    print("Numarul rezultat prin adunarea cifrelor zecilor si unitatilor este: ", z + u)


def adunare3():
    print("Introduceti va rog un numar natural de trei cifre:")
    x = int(input())
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    print("Numarul rezultat prin adunarea cifrelor este: ", a + b + c)


def capetesipicioare():
    print("Introduceti va rog numarul de gaini:")
    g = int(input())
    print("introduceti va rog numarul de oi")
    o = int(input())
    print("Numarul de capete este: ", g + o, ", iar numarul picioarelor este: ", 2 * g + 4 * o)


def cub():
    print("Introduceti lungimea laturii:")
    l = int(input())
    a = 6 * (l ** 2)
    v = l ** 3
    print("Aria cubului este", a, " iar volumul cubului este: ", v)


def eliminacifra():
    print("Introduceti un numar natural de 3 cifre")
    x = int(input())
    a = x // 100
    b = x % 10
    print(" numarul obtinut prin eliminarea cifrei din mijloc: ", a * 10 + b)


def oreminute():
    print("Introduceti va rog ora:")
    o = int(input())
    print("Introduceti va rog minutele:")
    m = int(input())
    print("minutele pe care doriti sa le adaugati:")
    x = int(input())
    on = o*60 + m + x
    print("ora noua este:" , on//60, "minute:", on%60)


def produscifre():
    print("Introduceti va rog un numar natural de trei cifre:")
    x = int(input())
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    print("Numarul rezultat prin inmultirea cifrei unitatilor cu cifra sutelor este: ", a*c)


def globuri():
    print("Introduceti va rog numarul globurilor albe:")
    a = int(input())
    r = a*2
    v = r - 3
    print("Numarul total de globuri este: ", a+r+v)


def gauss():
    print("Va rog introduceti un numar natural:")
    a = int(input())
    g = a*(a+1)//2
    print("Suma lui Gauss este: ", g)


def animale():
    print("Introduceti va rog numarul caini:")
    c = int(input())
    p = 2 * c
    g = 2 * p
    print("Numarul animalelor din curte este: ", c+p+g)

def marte():
    print("m:")
    m = int(input())
    print("n:")
    n = int(input())
    print("p:")
    p = int(input())
    print("o valoare pt a:")
    a = int(input())
    print("o valoare pt b:")
    b = int(input())
    print("o valoare pt c:")
    c = int(input())
    moneda_1 = a * m
    moneda_2 = b * n
    moneda_3 = c * p
    print("Martianul Iggle are: ", moneda_1+ moneda_2 + moneda_3 , "lei martieni")

def cumparaturi():
    print("Va rog introduceti un pretul unei cutii de bomboane:")
    B = int(input())
    print("Va rog introduceti suma pe care o are Gigel")
    S = int(input())
    c = S//B
    bo = (c+1) * B - S
    print("Gigel poate cumpara:",c , "cutii de bomboane" , "iar pentru a mai cumpara o cutie are nevoie de" , bo , "lei.")


def inaltimetriunghi():
    print("Introduceti va rog lungimea laturii 1:")
    l1 = int(input())
    print("introduceti va rog lungimea laturii 2:")
    l2 = int(input())
    print("Introduceti va rog lungimea ipotenuzei:")
    i = int(input())
    h = l1 * l2 // i
    print(" Lungimea inaltimii dusa din unghiul drept pe ipotenuza este:" , h , ".")

def sumacifrapermutare():
    print("Introduceti va rog un numar de 3 cifre distincte:")
    n = int(input())
    a = n % 10
    b = n // 100
    c = (n // 10) % 10
    S = a*100+b*10+c+a*100+c*10+b+b*100+a*10+c+b*100+c*10+a+c*100+a*10+b+c*100+b*10+a
    print(" Suma tuturor numerelor care se pot obtine prin interschimbarea cifrelor numarului cerut este:" , S , ".")


if __name__ == "__main__":
    adunare2()
    adunare3()
    capetesipicioare()
    cub()
    eliminacifra()
    oreminute()
    produscifre()
    globuri()
    gauss()
    animale()
    marte()
    cumparaturi()
    inaltimetriunghi()
    sumacifrapermutare()