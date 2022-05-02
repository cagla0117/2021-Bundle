topla = lambda a,b: a + b
çıkarma = lambda a,b: a - b
çarpma = lambda a,b: a * b
bölme = lambda a,b: a / b

x = int(input("ilk sayıyı giriniz: "))
y = int(input("ikinci sayıyı giriniz: "))
z = input("İşlem seçin(toplama:+,çıkarma:-,çarpma:*,bölme:/): ")
if z == "+":
    sonuç = topla(x,y)
elif z == "-":
    sonuç = çıkarma(x,y)
elif z == "*":
    sonuç = çarpma(x,y)
elif z == "/":
    sonuç = bölme(x,y)

print(sonuç)