"""
1. Odrediti da li je dati simbol cifra ili ne. 
2. Promijeniti „veličinu“ simbola: ako je malo slovo pretvoriti ga u veliko i obratno. 
3. Za dati string koji sadrži praznine (blankove), odrediti broj riječi u stringu.
4. Za dati string koji sadrži praznine (blankove), odrediti najdužu riječ u stringu.
5. Ispitati da li je data riječ palindrom (npr „topot“).
6. Dat je string u kojem postoje 2 jednaka slova; odrediti ta dva slova.
7. Za data dva stringa, ispitati da li je drugi string podstring prvog.
8. Dat je string koji sadrži samo mala slova i može sadržati praznine; ispitati da li je palindrom, ne računajući praznine (npr. „ana voli
milovana“).
9. U datom stringu sve uzastopne blankove (ako ih ima više od jednog) zamijeniti jednim blankom.
"""
#------------------------------------------------------------------------------------
# 1.Odrediti da li je dati simbol cifra ili ne.
#------------------------------------------------------------------------------------
from typing import Counter


string="011"
print (string.isdigit())

#------------------------------------------------------------------------------------
# 2.Promijeniti „veličinu“ simbola: ako je malo slovo pretvoriti ga u veliko i obratno.
#------------------------------------------------------------------------------------
string = "Moja"
print(string.lower())
print(string.upper()) 

#------------------------------------------------------------------------------------
# 3.Za dati string koji sadrži praznine (blankove), odrediti broj riječi u stringu.
#------------------------------------------------------------------------------------
def broj_rijeci(ulazni_string): #f-ja koja broji rijeci u stringu bez razmaka
    
    niz_rijeci = ulazni_string.split(' ') # brisemo razmake
    duzina_niza = len(niz_rijeci)         # duzina stringa
    return duzina_niza

a = broj_rijeci('Uvod u programiranje')
print(a)
#------------------------------------------------------------------------------------
# 4. Za dati string koji sadrži praznine (blankove), odrediti najdužu riječ u stringu.
#------------------------------------------------------------------------------------
string = 'Uvod u programiranje'
rijeci_u_string = string.split(' ') # dijeli string na elemente po blankovim --> DOBIJAMO ['Uvod','u','programiranje']
duzina_prve_rijeci = len(rijeci_u_string[0]) # racuna duzinu rijeci
duzina_druge_rijeci = len(rijeci_u_string[1])
duzina_trece_rijeci = len(rijeci_u_string[2])
najduza_rijec = max(duzina_prve_rijeci,duzina_druge_rijeci,duzina_trece_rijeci) # racuna koja je rijec najduza u stringu
if duzina_prve_rijeci > duzina_druge_rijeci and duzina_prve_rijeci > duzina_trece_rijeci:
    print('Najduza rijec je:',rijeci_u_string[0])
elif duzina_druge_rijeci > duzina_trece_rijeci:
    print('Najduza rijec je:', rijeci_u_string[1])
else:
    print('Najduza rijec je:', rijeci_u_string[2])

#------------------------------------------------------------------------------------
# 5. Ispitati da li je data riječ palindrom (npr „topot“).
#------------------------------------------------------------------------------------
def da_li_je_rijec_palindorom(rijec):
    return rijec == rijec[::-1]
print(da_li_je_rijec_palindorom('topot'))
#------------------------------------------------------------------------------------
# 6. Dat je string u kojem postoje 2 jednaka slova; odrediti ta dva slova.
#------------------------------------------------------------------------------------
string = "topot";    
print("Duplikati u stringu:");  
#Broji svaki znak prisutan u nizu 
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            #Postavite string[j] na 0 kako biste izbjegli ispis posjećenog znaka 
            string = string[:j] + '0' + string[j+1:];  
    # znak se smatra duplikatom ako je broj veći od 1
    if(count > 1 and string[i] != '0'):  
        print(string[i], end=',');  


#------------------------------------------------------------------------------------
# 7. Za data dva stringa, ispitati da li je drugi string podstring prvog.
#----------------------------------------------------------------------------
string1 ='Kompjuteri'
string2 = 'ter'
if string2 in string1:
    print('da')
else:
    print('ne')
#------------------------------------------------------------------------------------
# 8. Dat je string koji sadrži samo mala slova i može sadržati praznine; ispitati da li je palindrom, 
# ne računajući praznine (npr. „ana volimilovana“).
#------------------------------------------------------------------------------------

def da_li_je_string_palindorom(string):
    string = string.replace(' ','')
    return string == string[::-1]
print(da_li_je_string_palindorom('ana voli milovana'))

#------------------------------------------------------------------------------------
# 9. U datom stringu sve uzastopne blankove (ako ih ima više od jednog) zamijeniti jednim blankom.
#------------------------------------------------------------------------------------
string_blankovi = 'uvod u    programiranje'
print(string_blankovi.replace(' ''  '' ',' '))