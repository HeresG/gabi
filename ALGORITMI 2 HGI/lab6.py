def selectionSort(itemsList):
    n = len(itemsList)
    for i in range(n):
        minValueINdex= i

        for j in range(i+1, n):
            if itemsList[j] < itemsList[minValueINdex]:
                minValueINdex = j

        if minValueINdex != i:
            temp= itemsList[i]
            itemsList[i] = itemsList[minValueINdex]
            itemsList[minValueINdex] = temp

    return itemsList



employee1 = {
    'id': 14,
    'name': 'John Doe',
    'age': 36 ,
    'position' : 'Bussines maneger'
}
employee2 = {
    'id': 2,
    'name': 'Jane Doe',
    'age': 20,
    'position': 'N/A'
}
employee3 = {
    'id': 110,
    'name': 'john Smith',
    'age': 40,
    'position': 'software developer.'
}
employee4 = {
    'id': 40,
    'name': 'jane smith',
    'age': 35,
    'position': 'Engineer '
}

list1 = [ employee1, employee2, employee3]

 def cautareId(lista, id_cautat):
     for i in range(len(lista)):
         element = lista[i]
         if element['id'] == id_cautat:
             return lista[i]['position']
        return None

# def cautareId(lista, pozitie_cautata):
#     for i in range(len(lista)):
#         element = lista[i]
#         if element['position'] == pozitie_cautata:
#             return lista[i]
#         return {}

print(cautareId(list1,110))

