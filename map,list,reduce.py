#odev 2 hafta 9#
#tek ssay�lar� listeliyoruz 
iki ile carp�yoruz
ve son listeyi topluyoruz#

from functools import reduce

def tek(sayi):
    return sayi%2==1
def carp(x):
    return x*2
def topla(a,b):
    return a+b

say=range(1,10)

b=list(filter(tek,say))
print("tek say�lar:  ",b)
c=list(map(carp,b))
print("tek say�lar�n iki ile carp�m�:  ",c)
print("son liste toplam�:  ",reduce(topla,c))

