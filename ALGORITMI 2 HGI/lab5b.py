def min_max(lista):
    prod = 1
    min = 1
    max = lista[0] * lista[1]
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            prod = lista[i] * lista[j]
            if prod > max:
                max = prod
            elif prod < min:
                min = prod
    return min, max



if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print(min_max(lista))

