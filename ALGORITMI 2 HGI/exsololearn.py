# # def func(x):
# #   res = 0
# #   for i in range(x):
# #      res += i
# #   return res
# #
# # print(func(4))
#
# #
# import numpy as np
# import pandas as pd
# import hashlib
#
# # descarcam datele necesare de pe site-ul recensamantului
# populatie_judete = pd.read_csv("http://www.recensamantromania.ro/wp-content/uploads/2013/07/sR_Tab_5.xls", skiprows=5)
# populatie_virste_sexe = pd.read_csv("http://www.recensamantromania.ro/wp-content/uploads/2013/07/sR_Tab_6.xls",
#                                     skiprows=5)
#
# # definim un dicționar de nume
# nume = {
#     "B": ["Popescu", "Ionescu", "Pop", "Georgescu", "Radu"],
#     "F": ["Popescu", "Ionescu", "Pop", "Georgescu", "Radu", "Andrei", "Maria", "Alexandra", "Ioana"]
# }
#
#
# # definim funcția de generare a CNP-urilor
# def generare_CNP(populatie_judete, populatie_virste_sexe, sex):
#     # alegem un județ aleatoriu bazat pe distribuția populației
#     judet = np.random.choice(populatie_judete["Judet"], p=populatie_judete["Total"] / populatie_judete["Total"].sum())
#
#     # alegem o vârstă aleatorie bazată pe distribuția populației pe vârste și sex
#     virsta = np.random.choice(
#         populatie_virste_sexe.loc[(populatie_virste_sexe["Sex"] == sex) & (populatie_virste_sexe["Judet"] == judet)][
#             "Varsta"],
#         p=populatie_virste_sexe.loc[(populatie_virsta



print(len((1,)))

