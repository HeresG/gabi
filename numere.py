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
