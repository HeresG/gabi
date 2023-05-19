denominations = [10, 20, 50, 100]

def rest(change, denominations):
    togiveback = [0] * len(denominations)
    for indice, valoare in enumerate(reversed(denominations)):
        while valoare <= change:
            change = change - valoare
            togiveback[indice] += 1
    return togiveback[::-1]



def fib(n):
    mem = []
    if n <= 2:
        mem = [0] * n
    else:
        mem = [0, 1]
        for i in range(2, n):
            mem.append(mem[i-1] + mem[i-2])
    return mem



def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n-1) + fib2(n-2)


def fibo3(n, mem):
    if n in mem:
        return mem[n]
    if n <= 2:
        rez = 1
    else:
        rez = fibo3(n-1, mem) + fibo3(n-2, mem)
        mem[n]= rez
        print(mem)
    return rez

print(fibo3(20,{}))


#lista de 3 numere cu valori cuprinse intre 0 si 255 ex[2,10,234]
# sa se returneze inversa listei obtinuta prin scaderea valorilor din lista , din numarul 255

def inversa(lista):
    inversa =[]
    if len(lista) != 3:
        return 0
    invers = [ 255 - elem for elem in lista]
    return inversa[::-1]


#if __name__ == "__main__":
  #  print(rest(47, denominations))
 #   print(fib(5))
 #print(fib2(10))

