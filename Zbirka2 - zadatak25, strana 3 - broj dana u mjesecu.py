"""
Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i datu godinu štampa broja dana u
datom mjesecu.

"""
mjesec = int(input('Unesite redni broj mjeseca:'))
godina = int (input('Unesite godinu:'))
mjeseci_sa_31_dana = [1,3,5,7,8,10,12]
mjesec_sa_30_dan = [4,6,9,11]

def prestupna_godina(godina):
    if godina%4 == 0:
        if godina%100 == 0:
            if godina%400 == 0:
                return '29 dana u mjesecu'  
            else:
                return '28 dana u mjesecu'    
        else:
            return '29 dana u mjesecu'
    else:
        return '28 dana u mjesecu' 


def broj_dana_u_mjesecima(mjesec):
    if mjesec < 13:
        if mjesec in mjeseci_sa_31_dan:
            return '31 dan u mjesecu'
        elif mjesec in mjeseci_sa_30_dana:
            return '30 dana u mjesecu'
        else:
            return prestupna_godina(godina)
    else:
        return'Pogresan unos.'      

print(broj_dana_u_mjesecima(mjesec))