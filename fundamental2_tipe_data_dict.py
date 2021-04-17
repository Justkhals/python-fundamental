"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_in_eng = {'anak': 'kid', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_in_eng)
print(kamus_in_eng['ayah'])
print(kamus_in_eng['ibu'])

print('Data ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_gojek = {
    'tanggal': '2021-04-21',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}
print(data_dari_gojek)
print(f'Driver di sekitar sini {data_dari_gojek}')
print(f"Driver #1 {data_dari_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_gojek['driver_list'][0]['jarak']} meter")
