"""
Za prirodan broj k, štampati frazu „Na izletu smo ubrali k pecuraka“, gdje završetak rijeci
„pecurka“ prilagodite broju k. Npr. 101 pecurku, 1204 pecurke, 506 pecuraka
"""
broj_pecuraka = int(input('Unesite broj pecuraka:'))

def mijenjanje_rijeci_pecurka_u_odnosu_na_unijeti_broj(broj_pecuraka):
    if broj_pecuraka%10 == 1:
        print('Na izletu smo ubrali', broj_pecuraka,'pecurku')
    elif broj_pecuraka%10 > 1 and broj_pecuraka%10 < 5:
        print('Na izletu smo ubrali', broj_pecuraka,'pecurke')
    else:
        print('Na izletu smo ubrali', broj_pecuraka,'pecuraka')
        
print(mijenjanje_rijeci_pecurka_u_odnosu_na_unijeti_broj(broj_pecuraka))


