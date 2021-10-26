"""
Zbirka2 - Zadatak11, strana1
Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broj dvocifren broj.
"""
unesen_broj = int(input('Unesite trocifren broj:'))

prva_cifra = unesen_broj//100
druga_cifra = (unesen_broj//10)%10
treca_cifra = unesen_broj%10
zbir_cifara_unesenog_broja = prva_cifra + druga_cifra + treca_cifra

def zbir_cifara_unesenog_broja_dvocifren_broj(unesen_broj):
   if unesen_broj > 99 and unesen_broj < 1000:
      if zbir_cifara_unesenog_broja > 9 and zbir_cifara_unesenog_broja < 100:
         print('Zbir cifara trocifrenog broja je:', zbir_cifara_unesenog_broja,'Broj je dvocifren')
      else:
         print('Zbir cifara trocifrenog broja je:', zbir_cifara_unesenog_broja,'Broj nije dvocifren')
   else: 
      print('Niste unijeli trocifren broj')  

zbir_cifara_unesenog_broja_dvocifren_broj(unesen_broj)

