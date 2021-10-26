# Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.

unesen_broj = int(input('Unesite trocifren broj:'))

prva_cifra = unesen_broj//100
druga_cifra = (unesen_broj//10)%10
treca_cifra = unesen_broj%10
prva_cifra, druga_cifra, treca_cifra = treca_cifra, druga_cifra, prva_cifra

rezultat = 100 * prva_cifra + 10 * druga_cifra + treca_cifra

print(rezultat)