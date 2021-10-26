"""
Zbirka2 - Zadatak1, strana1

Napisati kod koji za date katete a i b (a<b) pravouglog trougla racuna površinu i
zapreminu tijela koje se dobija rotacijom trougla oko manje katete.

Rotacijom se dobija kupa čija je visina H = a, a poluprečnik R = b.
Ostaje nam da izračunamo P i V kupe.
"""
import math
a = 5
b = 7
c = math.sqrt(a**2 + b**2)

def povrsina_kupe(a, b, c):
    """Funkcija koja racuna P kupe, gdje je B baza a M omotač"""
    B = b**2*math.pi
    M = b*3.14*c
    P = B + M
    return P
povrsina_kupe(a, b, c)

def zapremina_kupe(a, b):
    """Funkcija koja racuna V kupe, gdje je a manja strana trougla a u kupi predstavlja visinu kupe"""
    V = (b**2*math.pi*a)//3
    return V

zapremina_kupe(a, b)

print('Površina kupe je:', povrsina_kupe(a, b, c))
print('Zapremina kupe je:', zapremina_kupe(a, b))

