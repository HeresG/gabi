def cifre(nr):
    unit = nr % 10
    zeci = nr // 10 % 10
    suma = unit + zeci
   # return unit + zeci
    return suma


def versiunea_01(sir_de_caractere):
    for litera in sir_de_caractere:
        if litera in "aeiou":
            print(litera.upper(), end='')
        else:
            print(litera, end='')


def literemici():
    text = input()
    lista_litere = []
    for i in range(len(text)):
        if ord(text[i]) > 20 and ord(text[i]) < 123:
            if text[i] not in lista_litere:
                lista_litere.append(text[i])
    print(lista_litere)


if __name__=="__main__":
    literemici()