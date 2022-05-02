a = input('Dörtgenin uzun kenarı: ')
b = input('Dörtgenin kısa kenarı: ')
ax = float(a)
bx = float(b)
z = ax*ax + bx*bx
z = pow(z,1/2)
print('Köşegen: ',z )
alan = ax * bx
print('Alan: ',alan )
cevre = 2*ax + 2*bx
print('Çevre: ',cevre )


