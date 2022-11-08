def schimbare():
    cuvint = input().strip()
    print(cuvint)
    index = 0
    for caracter in cuvint:
        if caracter in 'aeiou':
            print(caracter.upper(), "am gasit vocala" , index)
        else:
            print(caracter, index)
        index = index + 1


def primasiultimalitera():
    cuvint = input().strip()
    cuvantn = ""
    print(cuvint)
    index = 0
    for caracter in cuvint:
        if index == 0 or index==len(cuvint)-1:
            cuvantn = cuvantn + caracter.upper()
        else:
            cuvantn = cuvantn + caracter
        index = index +1
    print(cuvantn)


def prefix_sufix():
    sufix = "_"
    prefix = "#"
    cuvint = input().strip()
    cuvintn = prefix + cuvint.strip()+ sufix
    print(cuvintn)

def prefix_sufix_extrag():
    nrsf = 2
    cuvint = input()
    print(cuvint[:nrsf], cuvint[-nrsf:])


def asterisc():
    cuvint = input().strip()
    cuvintn = ""
    print(cuvint)
    for caracter in cuvint:
        if caracter in 'aeiou':
            cuvintn = cuvintn + caracter + "*"
        else:
            cuvintn = cuvintn + caracter
    print(cuvintn)


def counter():
    cuvint = input().strip()
    contor = 0
    for caracter in cuvint:
       if caracter in "aA":
           contor +=1
    print(contor)


def lista():
    l = [234, 100, 90, 300, 111, 2, 1, 5, 0]
    jumatate = len(l) // 2
    l1 = l[:jumatate:]
    l1.sort()
    print(l1)
    l2 = l[jumatate::]
    l2.sort(reverse=True)
    print (l2)
    l2.append(4)
    l2.append(8)
    print (l2)
    print (l)
    l.pop()
    print(l)


def dublare():
    cuvint = input()
    sir_nou = ""
    for caracter in cuvint:
        if caracter in 'aeiou':
            sir_nou = sir_nou+ caracter*2
        else:
            sir_nou = sir_nou+caracter
    print(sir_nou)


def elim_spatii_inutile():
   propozitie = input()
   propozitie += ' '
   auxiliar_propozitie = ""
   cuvant = ""
   for i in range(len(propozitie)):
       if propozitie[i] != ' ':
           cuvant = cuvant + propozitie[i]
       elif len(cuvant) > 0:
           auxiliar_propozitie += cuvant + ' '
           cuvant = ""
   auxiliar_propozitie = auxiliar_propozitie[:len(auxiliar_propozitie) -1]
   print(auxiliar_propozitie)


if __name__ == "__main__":
    elim_spatii_inutile()

