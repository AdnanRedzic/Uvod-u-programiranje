# Odrediti broj rijeci u stringu ako su one odvojene razmacima

def broj_rijeci(ulazni_string):
    """ 
    ulazni_string -> string koji ima razmake
    Funkcija vraca broj elemenata niza razbijenog po razmacima
    """
    niz_rijeci = ulazni_string.split(' ')
    duzina_niza = len(niz_rijeci)
    return duzina_niza

a = broj_rijeci('Uvod u programiranje')
print(a)

# Da li je riječ palindrom
"""
if rijec == rijec[::-1]:
       return True
    else:
       return False
"""

def da_li_je_palindrom(rijec):
    rijec = rijec.replace(' ','') #zamjenjuje razmak praznim karakterom
    rijec = rijec.lower()         # prebacijue velika slova u mala
    return rijec == rijec[::-1]   # provjerava uslov IF iz komentara 
print(da_li_je_palindrom('ana voli milovanA'))
