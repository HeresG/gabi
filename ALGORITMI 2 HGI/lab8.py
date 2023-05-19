#file = open('C:\\Users\\computer\\Downloads\\pycharm.txt', 'r+')
#for each in file:
 #   print(each)

# file = open('C:\\Users\\computer\\Downloads\\pycharm.txt', 'r+')
# el = []
#
# for line in file:
#     el.append(line)
# print(el)
# file.close()
# i= 0
# while i<len(el):
#     if el[i].startswith("4"):
#         el.insert(i, '3333\n')
#         i+=1
#     i+=1
# print(el)
#
# file = open('C:\\Users\\computer\\Downloads\\pycharm.txt', 'w+')
# for e in el:
#     file.write(e)
#file.close()


file = open('C:\\Users\\computer\\Downloads\\pycharm.txt', 'r+')
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())
el = []
for line in file:
    el.append(line)
print(el)
file.close()