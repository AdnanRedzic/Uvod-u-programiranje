#Da li je broj prost.
def prost_broj(broj):
    i = 2
    while i < broj:
        if broj%i == 0:
           return False
        i= i + 1
    return True
print(prost_broj(24))