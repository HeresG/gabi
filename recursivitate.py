def cautare_sir(sirprincipal, subsir):
    i = 0
    n = len(sirprincipal) - len(subsir)
    while i <= n:
        j = 0
        while j < len(subsir):
            if sirprincipal[i+j] != subsir[j]:
                j = j +1
                break
            else:
                j = j+1
        if j == len(subsir):
            return i
        i = i+j
    return -1


def adunare(n): # 1+2+3+4+5+....
    s= 0
    for i in range(1,n+1):
        s = s + i
    return s


def adunare_recursiv(n):
    if n == 1:
        return 1
    return n + adunare_recursiv(n-1)


def factorial(n):
    if n >1:
        return n * factorial(n-1)
    else:
        return 1


def factorialvarianta2(n):
    if n == 1:
        return 1
    return n * factorialvarianta2(n-1)


def fibonacci(n): # al n -lea termen in sirul lui Fibonacci
    f =0
    t1 = 0
    t2 = 1
    for i in range(2,n+1):
        f = t1+t2
        t1 = t2
        t2 = f
    return f


def fibrec(n): # fibonacci recursiv   F(n)= F(n-1) + F(n-2)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibrec(n-1) + fibrec(n-2)


#de realizat o functie recursiva care imi determina nr de aparitii al cifrei 0 intr un numar natural
def nr_zero_sir(n):   #n = nr natural
    sir = str(n)
    c =0
    if sir[len(sir)-1]=="0":
        c = 1
    if len(sir)-1<=0:
        return c
    return c + nr_zero_sir(int(sir[:len(sir)-1]))


def nr_zero(n):
    c =0
    if n == 0:
        return 0
    if n%10 ==0:
        c = 1
    return c +nr_zero(n//10)


# sa se realizeze o functie care ia ca paramentru un nr natural si il reintoarce in ordine inversa a elementelor numarului
# ex : 220 -> 0 2 2
def nr_invers(n):
    sir = str(n)           # convertesc numarul in sir
    c = sir[len(sir)-1]    # extrag ultimul element
    if len(sir)-1<=0:      # verific daca nu cumva am ajuns la sfarsit
        return c
    return c+ ' , '+ nr_invers(int(sir[:len(sir)-1]))



if __name__ == "__main__":
 #   print(cautare_sir("caini de tractiune husky", "ni"))
 #   print(adunare(5))
 #   print(adunare_recursiv(5))
 #   print(factorial(5))
 #   print(factorialvarianta2(5))
    print(fibonacci(15))
 #   print(fibrec(15))
 #   print(nr_zero_sir(15000))
 #   print(nr_zero(30000))
 #   print(nr_invers(321))