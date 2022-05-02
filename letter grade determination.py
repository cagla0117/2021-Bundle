number = input('Öğrencinin puanını giriniz: ')
sayı = int(number)

if  (90 < sayı < 100) :
    note = 'AA'
elif  79 < sayı < 90 :
    note = 'BA'
elif  69 < sayı < 80 :
    note = 'BB'
elif  59 < sayı < 70 :
    note = 'CB'
elif  49 < sayı < 60 :
    note = 'CC'
elif  39 < sayı < 50 :
    note = 'DC'
elif  29 < sayı < 40 :
    note = 'DD'
elif  19 < sayı < 30 :
    note = 'FF'
else:
    note = 'VF'

print( 'Öğrencinin harf notu: ' , note)

