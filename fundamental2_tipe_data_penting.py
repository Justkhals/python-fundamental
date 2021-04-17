print('tipe data skalar => tope data sederhana')

anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')

anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nsapa semua anak: cara ribet')
for index in range(0, len(anak)):
    print(f'{index + 1}. Hai {anak[index]}!')