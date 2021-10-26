"""
Napisati kod koji za datu godinu određuje da li je prestupna i štampa odgovarajucu
poruku.
"""
godina = int(input('Unesite godinu:'))

def prestupna_godina(godina):
    if godina%4 == 0:
        if godina%100 == 0:
            if godina%400 == 0:
                print('Godina', godina, 'je prestupna')
        else:
            print('Godina', godina, 'je prestupna')
    else:
        print('Godina', godina, 'nije prestupna')
prestupna_godina(godina)

