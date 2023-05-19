def schimbare():
    cuvint = input().strip()
    print(cuvint)
    for caracter in cuvint:
        if caracter in 'aeiou':
            print(caracter.upper())
        else:
            print(caracter)


if __name__ == "__main__":
    schimbare()

