
# se da un sir de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5
def sir5():
    print("introduceti sirul de numere naturale")
    sir = input() # sir de [inceput:sf:pas]
    contor = 0
    for index in range(0,len(sir),1):              #range(len(sir))
        print(sir[index])
        if sir[index]=="5":
            contor += 1
    print("numarul de aparitii al cifrei 5 este:", contor)



# se da o lista de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5
def lista5():
    print("introduceti sirul de numere naturale despartit prin virgula")
    l = input().strip() # sir de [inceput:sf:pas]
    contor = 0
    for index in range(len(l)): #range(len(sir))
        if l[index]=="5":
            contor += 1
    print("numarul de aparitii al lui 5 este:", contor)

#de realizat o functie care imi verifica apartenenta unui numar la un domeniu
# 0 -> 4000 - mic
# 4000 -> 8000 - mediu
# 8000 ->  - mare
def incadrare():
    print("va rog introduceti un numar pentru care doriti incadrarea in domeniile date")
    nr = int(input())
    if nr<4000:
        print("mic")
    else:
        if nr<8000:
            print("mediu")
        else:
            print("mare")

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
    print("Apasati 1 pentru adunare , 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire, 5 pentru incadrare , 6 sir5, 7 pentru lista")
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
                    if opt == "5":
                        print("incadrare")
                        incadrare()
                    else:
                        if opt == "6":
                            print("sir")
                            sir5()
                        else:
                            if opt == "7":
                                print("lista")
                                lista5()


if __name__== "__main__":
    exit_ = ""
    while exit_!="0":
        meniu()
        print("pentru iesire tastati 0 sau orice alta tasta pentru continuare")
        exit_ = input().strip()
