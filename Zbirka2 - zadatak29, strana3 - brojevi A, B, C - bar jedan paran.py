"""
Data su tri cijela broja A, B, C. Odrediti da li medu njima ima bar jedan paran broj i bar
jedan neparan broj. Ulaz: Prvi red ulaza sadrži tri cijela broja A, B i C (1  A  1000). Izlaz:
Štampati „YES“ ili „NO“.
"""

A = int(input('Unesite A:'))
B = int(input('Unesite B:'))
C = int(input('Unesite C:'))
if (A%2 == 0 or B%2 == 0 or C%2 == 0) and (A%2 == 1 or B%2 == 1 or C%2 == 1):
    print('YES')
else:
    print('NO')
