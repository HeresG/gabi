# def spectacol(lista):  # lista mea va fi de forma [ [ 1,8] , [8,12] , [ 8, 10 ] , ...]
#     lista = sorted(lista, key = lambda el : el[1])
#     final = [lista[0]]
#     ultimaora = lista[0][1]
#     for el in specs:
#         if el[0] >= ultimaora:
#             ultimaora = el[1]
#             final.append(el)
#     print("numar spectacole", len(final))


# def solve(bag, gMax):
#    bag = sorted(bag, key=lambda k: k[1]/k[0],reverse=True)
#    win = 0
#    weight = 0
#    final = []
#    c = 0
#    while weight <= gMax and c < len(bag):
#        obj = bag[c]
#        if weight+obj[0] <= gMax:
#            weight += obj[0]
#            win += obj[1]
#            final.append([obj[0],obj[1],"added wholly"])
#        else:
#            fits_weight = gMax-weight
#            if fits_weight > 0:
#                #regula de 3 simpla
#                fits_value = fits_weight * obj[1]
#                fits_value //= obj[0]
#                weight += fits_weight
#                win += fits_value
#                final.append([fits_weight,fits_value,"added partially"])
#        c = c+1
#    print(len(final))
#    print(win)
#    print("weight:",weight,"kg's")
#    for obj in final:
#        print("["+str(obj[0])+"kg's & "+str(obj[1])+" points ("+obj[2]+")]")
#
#
# if __name__ == '__main__':
#    n = int(input("n: "))
#    gMax = int(input("G: "))
#    if 1 <= n <= 1000 and 1 <= gMax <= 10000:
#        bag = []
#        for i in range(n):
#            inp = input().split(" ")
#            weight, value = int(inp[0]), int(inp[1])
#            if 1 <= weight <= 10000 and 1 <= value <= 10000:
#                bag.append([weight, value])
#        if len(bag) == n:
#            solve(bag, gMax)


#if __name__ == "__main__":
#    specs = list()
#    n = int(input("numar spectacole:"))
 #   for i in range(n):
 #       oi = int(input("ora inceput"))
 #       os = int(input("ora sfarsit"))
  #      specs.append([oi, os])
  #  specs = [[1,8], [8,10],[8,12],[12,13],[15,17],[18,21],[17,20]]
   # spectacol(specs)