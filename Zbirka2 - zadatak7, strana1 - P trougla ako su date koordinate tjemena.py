
"""Napisati program koji ucitava šest realnih brojeva x1, y1, x2, y2, x3, y3 koji redom
predstavljaju koordinate tacaka A(x1, y1), B(x2, y2) i C(x3, y3) i štampa površinu i obim
trougla ABC.
"""
import numpy as np
x1 = int(input('Unesite x1 koordinatu:'))
y1 = int(input('Unesite y1 koordinatu:'))
x2 = int(input('Unesite x2 koordinatu:'))
y2 = int(input('Unesite y2 koordinatu:'))
x3 = int(input('Unesite x3 koordinatu:'))
y3 = int(input('Unesite y3 koordinatu:'))

matrica = np.array([[x1 , y1, 1],[x2, y2, 1], [x3, y3, 1]])
print(matrica)
Determinanta = np.linalg.det(matrica)
print('Determinanta je:',Determinanta)

#Najveci broj od unesena tri:
a = 5
b = 6
c = 7
najveci = max(a, b, c)
print(najveci)