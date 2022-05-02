def check():
    i = 0
    while i == 0:
        x = input("Şifreyi Giriniz:")
        if len(x) < 7:
            print("En az 7 karakter içermelidir")
            i= 0
        elif x.isupper() == True:#sayıyı küçük harften saymıyor
            print("Küçük harf içermelidir.")
            i=0
        else :
           print("Doğru Parola")
           break

check()