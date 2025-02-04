# Set di Python
# Set adalah tipe data yang menyimpan elemen unik (tidak ada duplikat) dan tidak terurut
# Urutan elemen dalam set tidak dapat diprediksi dan bisa berbeda setiap kali ditampilkan

my_set = {'Ultron', 'Iron Man', 'Captain America', 'Black Panther', 'Winter Soldier'}
print(my_set)  # Output akan acak

# Mengonversi berbagai tipe data menjadi set
my_list = [1, 2, 3, 4, 5]
my_tuple = ['satu', 'dua', 'tiga']
my_dictionary = {'nilai': 89, 'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19}

# Mengonversi ke dalam set
my_set_1 = set(my_list)  # Mengubah list menjadi set
my_set_2 = set(my_tuple)  # Mengubah tuple menjadi set
my_set_3 = set(my_dictionary)  # Mengubah dictionary menjadi set (hanya key yang diambil)
my_set_4 = set(my_dictionary.values())  # Mengambil hanya values dari dictionary

# Menampilkan hasil konversi
print(my_set_1)  # Output: {1, 2, 3, 4, 5}
print(my_set_2)  # Output: {'satu', 'dua', 'tiga'}
print(my_set_3)  # Output: {'nilai', 'nama', 'Alamat', 'umur'} (hanya keys)
print(my_set_4)  # Output: {89, 'Faroja', 'Tangerang Selatan', 19} (values)

# Looping melalui set
# Set tidak terurut, jadi urutan elemen saat di-loop akan acak
for item in my_set:
    print(item)

# Condition statement menggunakan set
if 'Iron Man' in my_set:
    print('IRON MAN!!!')

# Menambahkan elemen ke dalam set
my_set.add('Thor')  # Menambahkan satu elemen
print(my_set)  # Output akan menunjukkan elemen baru 'Thor' ditambahkan

# Menambahkan beberapa elemen sekaligus dengan update()
my_set.update({'Hulk', 'Black Widow'})  # Menambahkan lebih dari satu elemen
print(my_set)  # Output akan menunjukkan 'Hulk' dan 'Black Widow' ditambahkan

# Menghapus data dalam set
my_set.remove('Thor')  # Menghapus elemen dengan key 'Thor'
print(my_set)  # Output: set tanpa 'Thor'

# Menggunakan discard untuk menghapus elemen
my_set.discard('Hulk')  # Tidak ada error meskipun elemen tidak ada
print(my_set)  # Output: set tanpa 'Hulk'

# Pop akan menghapus elemen acak dari set
my_set.pop()
print(my_set)  # Output: set tanpa elemen yang dipilih secara acak

# Menghapus seluruh elemen dalam set
my_set.clear()
print(my_set)  # Output: set kosong

# Menggunakan len() untuk menghitung jumlah elemen dalam set
my_set = {'Ultron', 'Iron Man', 'Captain America', 'Black Panther', 'Winter Soldier'}
print(len(my_set))  # Output: 5 (jumlah elemen dalam set)

# Union: Menggabungkan dua set, elemen yang sama tidak akan terduplikasi
my_set_2 = {'Ultron', 'Iron Man', 'Spiderman', 'Thor'}
my_set_3 = my_set.union(my_set_2)  # Menggabungkan set tanpa duplikat
print(my_set_3)  # Output: set gabungan tanpa duplikat

# Difference: Mencari perbedaan antara dua set
difference = my_set.difference(my_set_2)  # Menghasilkan elemen yang ada di my_set tapi tidak di my_set_2
print(difference)  # Output: {'Captain America', 'Black Panther', 'Winter Soldier'}

# difference_update: Mengubah my_set dengan perbedaan antara my_set dan my_set_2
my_set.difference_update(my_set_2)
print(my_set)  # Output: {'Captain America', 'Black Panther', 'Winter Soldier'}

# Symmetric Difference: Menghasilkan perbedaan simetris antara dua set
my_set_3 = my_set.symmetric_difference(my_set_2)
print(f'output symmetric difference: {my_set_3}')  # Output: elemen yang hanya ada di salah satu set

# symmetric_difference_update: Memodifikasi my_set dengan perbedaan simetris antara my_set dan my_set_2
my_set.symmetric_difference_update(my_set_2)
print(f'output symmetric difference update: {my_set}')  # Output: set yang hanya berisi elemen yang berbeda
# gampangnya: tidak kebawa kalau ada kedua duplikasinya 

# Intersection: Menghasilkan irisan (persamaan) antara dua set
my_set_3 = my_set.intersection(my_set_2)
print(f'output intersection: {my_set_3}')  # Output: {'Ultron', 'Iron Man'}

# intersection_update: Memodifikasi my_set dengan irisan antara my_set dan my_set_2
my_set.intersection_update(my_set_2)
print(f'output intersection update: {my_set}')  # Output: set hanya berisi elemen yang ada di kedua set

# isdisjoint: Mengecek apakah dua set tidak memiliki elemen yang sama
my_set_one = {1, 2, 3}
my_set_two = {2, 3}
print(f'output isdisjoint: {my_set_one.isdisjoint(my_set_two)}')  # Output: False (karena ada elemen yang sama)

# issuperset: Mengecek apakah satu set mencakup semua elemen set lain
print(f'output issuperset: {my_set_one.issuperset(my_set_two)}')  # Output: True, karena my_set_one mencakup semua elemen my_set_two

# issubset: Mengecek apakah satu set adalah subset dari set lain (semua elemen ada dalam set yang lain)
print(f'output issubset: {my_set_two.issubset(my_set_one)}')  # Output: True, karena my_set_two hanya berisi elemen yang ada di my_set_one
