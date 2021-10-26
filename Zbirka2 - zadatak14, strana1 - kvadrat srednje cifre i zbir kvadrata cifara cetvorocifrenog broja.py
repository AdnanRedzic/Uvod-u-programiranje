"""
Zadatak14, strana1

Dat je cetvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake,
štampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra
hiljada. Ako te dvije cifre nisu jednake, štampati zbir kvadrata svih cifara.
"""
import math
cetvorocifren_broj = 1231
b = cetvorocifren_broj//1000 # cifra hiljada
c = (cetvorocifren_broj//100)%10 #cifra stotina
d = (cetvorocifren_broj//10)%10 # cifra desetica
g = cetvorocifren_broj%10 # cifra jedinica
f = (cetvorocifren_broj//10)%100 #dvocifren broj koji se dobija uklananjem cifre jedinica i cifre hiljada

def kvadrat_srednjih_cifara_cetvorocifrenog_broja(cetvorocifren_broj):
    if cetvorocifren_broj > 999 and cetvorocifren_broj < 10000:   
        if g == b:
            print(f**2)
        elif b != g:
            zbir_kvadrata_cifara = b**2 + c**2 + d**2 + f**2
            print('Zbir kvadrata cifara:', zbir_kvadrata_cifara)
    else:
        print('Unijeli ste broj koji nije cetvorocifren') 

print(kvadrat_srednjih_cifara_cetvorocifrenog_broja(cetvorocifren_broj))

