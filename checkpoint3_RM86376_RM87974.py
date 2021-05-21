'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 3
Alunos:
João Paulo Silva de Queiroz - RM86376
Mateus Amado Monteiro da Silva - RM87974
'''
from sklearn import tree
features = [[0, 0, 0], [10, 5, 10],[20, 10, 20],[30, 15, 30],[40, 20, 40],[50, 25, 50],[60, 25, 60],[55, 35, 65],[70, 23, 40],[90, 139, 199], [100, 140, 100], [125, 199, 199], [105, 150, 167], [114, 144, 39], [119, 193, 37], [103, 149, 123], [102, 141, 102], [107, 150, 162], [110, 155, 188], [106, 144, 19], [126, 200, 200], [139, 239, 339], [134, 243, 324], [176, 444, 777], [444, 444, 444], [145, 356, 378], [177, 423, 634], [198, 237, 281], [271, 359, 432], [166, 231, 312]]
labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
em_jejun = float(input("valor em jejun: "))
pos_sobrecarga = float(input("valor em sobrecarga:"))
glicemia_casual = float(input("glicemia casual:"))
x = classif.predict([[em_jejun, pos_sobrecarga, glicemia_casual]])
if x == 0:
    print("glicemia está normal")
elif x == 1:
        print("tolerância a glicose diminuída")
else:
    print("Você tem diabetes melitus")
