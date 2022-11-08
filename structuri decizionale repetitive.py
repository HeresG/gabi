#de realizat o functie care imi verifica apartenenta unui numar la un domeniu
# 0 -> 4000 - mic
# 4000 -> 8000 - mediu
# 8000 ->  - mare

# de realizat o functie care creaza un meniu de forma
# apasati 1 pentru adunare , 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire
def adunare():
    print("a=", end="")
    a = int(input())
    print("b=" ,  end="")
    b = int(input())
    print("a+b", a+b)

def scadere():
    print("a=", end="")
    a= int(input())
    print("b=" , end="")
    b= int(input())
    print("a-b" , a-b)

def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b", a * b)

def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b", a / b)


def meniu():
    print("Apasati 1 pentru adunare , 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire ")
    opt = input().strip()  # strip -> elimina spatiile de la inceput sau sfarsit
    if opt == "1":
        print("adunare")
        adunare()
    else:
        if opt == "2":
            print("scadere")
            scadere()
        else:
            if opt == "3":
                print("inmultire")
                inmultire()
            else:
                if opt == "4":
                    print("impartire")
                    impartire()
                else:
                    print("apasati 1 2 3 sau 4")


if __name__== "__main__":
    exit_ = ""
    while exit_!="0":
        meniu()
        print("pentru iesire tastati 0 sau orice alta tasta pentru continuare")
        exit_ = input().strip()
