# Aturan Penamaan Variabel di Python:
# 1. Harus dimulai dengan huruf atau garis bawah (_).(jika tidak sesuai Error Code) cek
# 2. Tidak boleh dimulai dengan angka.(jika tidak sesuai Error Code) cek
# 3. Hanya boleh mengandung huruf, angka, atau garis bawah (A-z, 0-9, _).(jika tidak sesuai Error Code) cek
# 4. Case-sensitive: 'nama', 'Nama', dan 'NAMA' adalah variabel berbeda. cek
# 5. Gunakan nama yang deskriptif agar mudah diingat karena nanti banyak variabel, misalnya 'total_income' daripada 'x'. reminder

# Gaya Penulisan Variabel di Python:
# 1. Camel Case:
#    - Dimulai dengan huruf kecil untuk kata pertama.
#    - Huruf pertama dari kata kedua dan seterusnya menggunakan huruf besar.
#    - Contoh:
#      - 'my number' menjadi 'myNumber'.
#      - 'our last night' menjadi 'ourLastNight'.

# 2. Snake Case:
#    - Semua huruf menggunakan huruf kecil.
#    - Kata-kata dipisahkan dengan garis bawah (_).
#    - Contoh:
#      - 'my number' menjadi 'my_number'.
#      - 'our last night' menjadi 'our_last_night'.

# Tips:
# - Gunakan gaya yang konsisten sesuai standar proyek atau preferensi tim.
# - Snake case sering digunakan di Python karena sesuai dengan PEP 8 (gaya standar Python).

# -----------------------------------------------------------------------------------------------------------------------------------------
# Tipe Data String di Python:
# - String adalah kumpulan karakter atau angka yang diapit oleh tanda kutip satu (' '), kutip dua (" "), atau kutip tiga (''' ''' / """ """).
# - String dianggap sebagai teks, meskipun berisi angka.

# 1. Kutip Satu (' ') dan Kutip Dua (" "):
#    - Fungsinya sama, digunakan untuk string satu baris.
#    - Gunakan kutip dua jika string mengandung kutip satu, dan sebaliknya.
# Contoh tipe data string
greeting = "Hello Purwadhika"  # String dengan kutip dua
fruit = 'jeruk'  # String dengan kutip satu
number_as_string = "1234"  # Angka dalam tanda kutip dianggap string
# Output contoh string
print(greeting)  # Output: Hello Purwadhika
print(fruit)  # Output: jeruk
print(number_as_string)  # Output: 1234

# 2. Kutip Tiga (''' ''' atau """ """):
#    - Digunakan untuk string yang terdiri dari banyak baris (multiline).
#    - Juga dapat digunakan untuk mendokumentasikan fungsi atau kode (docstring).
# Menggunakan string dengan kutip tiga
long_text = """Ini adalah contoh
teks panjang yang ditulis
dengan kutip tiga."""   
print(long_text)


#--------------------------------------------------------------------------------------------------------------------------------------------
# Tipe Data Angka di Python:
# 1. Integer (int):
#    - Bilangan bulat tanpa koma desimal.
#    - Contoh: 10, -3, 0.
#
# 2. Float:
#    - Bilangan desimal dengan koma (menggunakan titik).
#    - Contoh: 3.14, -7.89, 0.0.
#
# Catatan:
# - Variabel yang menyimpan angka akan otomatis dianggap sebagai integer atau float sesuai nilainya.
# - Penjelasan tipe data lain akan dibahas lebih lanjut pada sesi yang sesuai.

# Contoh:
integer_example = 42  # Integer
float_example = 3.14159  # Float

print(type(integer_example))  # Output: <class 'int'>
print(type(float_example))  # Output: <class 'float'>

#--------------------------------------------------------------------------------------------------------------------------------------------
# Tipe Data Boolean di Python:
# - Boolean hanya memiliki dua nilai: True dan False (case-sensitive).
# - Tipe data ini sering digunakan dalam pernyataan logika (logic statements) 
#   atau kondisi (conditional statements).

# Contoh:
is_student = True  # Boolean dengan nilai True
is_graduated = False  # Boolean dengan nilai False

# Boolean dalam operasi logika:
x = 10
y = 5
print(x > y)  # Output: True (karena 10 lebih besar dari 5)
print(x < y)  # Output: False (karena 10 tidak lebih kecil dari 5)


#----------------------------------------------------------------------------------------------------------------------------------------------
# Note Penting: Pengenalan Saja untuk sekarang boleh cukup tau saja nanti dibahas lebih detail materinya
# Tipe Data Collection: List, Tuple, dan Dictionary
# 1. List:
#    - Merupakan tipe data yang dapat menyimpan lebih dari satu data (elemen).
#    - Elemen dalam list bisa memiliki tipe data yang berbeda.
#    - List dapat diubah (mutable).
#    - Ditandai dengan tanda kurung siku [].
#    Contoh:
my_list = [1, "Hello", 3.14, True]

# 2. Tuple:
#    - Mirip dengan list, tetapi bersifat tidak bisa diubah (immutable).
#    - Ditandai dengan tanda kurung biasa ().
#    Contoh:
my_tuple = (1, "World", 7.89)

# 3. Dictionary:
#    - Tipe data yang menyimpan data dalam bentuk pasangan kunci (key) dan nilai (value).
#    - Elemen disimpan dalam format key:value.
#    - Ditandai dengan tanda kurung kurawal {}.
#    Contoh:
my_dict = {"name": "Oja", "age": 25}

# Output contoh:
print(my_list)  # Output: [1, "Hello", 3.14, True]
print(my_tuple)  # Output: (1, "World", 7.89)
print(my_dict)  # Output: {'name': 'Oja', 'age': 25}

#----------------------------------------------------------------------------------------------------------------------------------------------
# Note Penting: Pengenalan Saja untuk sekarang boleh cukup tau saja nanti dibahas lebih detail materinya
# Tipe Data Range di Python:
# - Range adalah tipe data yang digunakan untuk menghasilkan urutan angka.
# - Biasanya digunakan dalam perulangan (looping), seperti di dalam 'for' loop.
# - Range dapat menghasilkan urutan angka mulai dari 0 (default) hingga nilai tertentu.

# Cara penggunaan:
# range(start, stop, step) 
# - start: Angka mulai (default 0).
# - stop: Angka akhir (tidak termasuk).
# - step: Langkah di antara angka (default 1).


# Contoh:
my_range = range(1, 10, 2)  # Angka dari 1 hingga 9, dengan langkah 2
for number in my_range:
    print(number)  # Output: 1 3 5 7 9

# Tanpa parameter step (default step=1):
for number in range(5):
    print(number)  # Output: 0 1 2 3 4

#----------------------------------------------------------------------------------------------------------------------------------------------
# Note Penting: Pengenalan Saja untuk sekarang boleh cukup tau saja nanti dibahas lebih detail materinya

# Tipe Data Set di Python:
# - Set adalah tipe data yang menyimpan lebih dari satu data.
# - Set hanya menyimpan elemen unik, jadi otomatis menghilangkan duplikat.
# - Elemen dalam set tidak terurut dan tidak dapat diakses dengan indeks.
# - Set ditandai dengan tanda kurung kurawal {}.

# Contoh:
my_set = {1, 2, 3, 3, 4}  # Duplikat angka 3 akan dihilangkan
print(my_set)  # Output: {1, 2, 3, 4}
# Set tidak terurut, jadi urutan elemen bisa berbeda setiap kali running code.


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Note Penting: Pengenalan Saja untuk sekarang boleh cukup tau saja nanti dibahas lebih detail materinya

# Tipe Data None di Python:
# - None digunakan untuk menandakan bahwa suatu variabel kosong atau tidak memiliki nilai.
# - None sering digunakan untuk inisialisasi variabel yang belum memiliki nilai atau sebagai indikator bahwa suatu operasi tidak mengembalikan hasil.

# Contoh:
empty_value = None  # Variabel kosong, tidak memiliki data
print(empty_value)  # Output: None


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Operasi Aritmatika di Python:
# 1. Penjumlahan (+)
#    - Digunakan untuk menjumlahkan dua angka.
#    Contoh:
x = 5
y = 3
result_addition = x + y  # 5 + 3 = 8
print(result_addition)  # Output: 8

# 2. Pengurangan (-)
#    - Digunakan untuk mengurangi angka.
#    Contoh:
result_subtraction = x - y  # 5 - 3 = 2
print(result_subtraction)  # Output: 2

# 3. Perkalian (*)
#    - Digunakan untuk mengalikan dua angka.
#    Contoh:
result_multiplication = x * y  # 5 * 3 = 15
print(result_multiplication)  # Output: 15

# 4. Pembagian (/)
#    - Digunakan untuk membagi dua angka (hasilnya selalu float).
#    Contoh:
result_division = x / y  # 5 / 3 = 1.666...
print(result_division)  # Output: 1.666...

# 5. Pembagian Bulat (//)
#    - Digunakan untuk pembagian bulat, menghasilkan hasil tanpa angka desimal.
#    Contoh:
result_floor_division = x // y  # 5 // 3 = 1
print(result_floor_division)  # Output: 1

# 6. Sisa Pembagian (%) - Modulus
#    - Digunakan untuk mendapatkan sisa hasil bagi dari pembagian.
#  Analogi: Bayangkan kamu punya 10 buah apel dan ingin membagikannya ke 3 teman.
#  Setiap teman dapat 3 apel, tapi setelah dibagikan,
#  masih ada 1 apel yang tersisa. Sisa 1 Apel tersebut itu yang disebut modulus atau sisa dari pembagian.
#    Contoh:
result_modulus = x % y  # 5 % 3 = 2
print(result_modulus)  # Output: 2

# 7. Pemangkatan (**)
#    - Digunakan untuk menghitung pangkat (eksponen).
#    Contoh:
result_exponentiation = x ** y  # 5 ** 3 = 125
print(result_exponentiation)  # Output: 125


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Math Module
import math

# 1. math.sqrt(x) - Menghitung akar kuadrat dari x
x = 20
result_sqrt = math.sqrt(x)  # Akar kuadrat dari 16
print(result_sqrt)  # Output: 4.0

# 2. math.pow(x, y) - Menghitung x pangkat y (x^y)
result_pow = math.pow(2, 3)  # 2 pangkat 3 = 8 -> 2 x 2 x 2 = 8
print(result_pow)  # Output: 8.0

# 3. math.pi - Konstanta nilai pi (π)
print(math.pi)  # Output: 3.141592653589793

# 4. math.fabs(x) - Menghitung nilai absolut (nilai mutlak) dari x
negative_num = -5
result_fabs = math.fabs(negative_num)  # Menghitung nilai absolut dari -5 -> intinya bukan minus yang minus plus
print(result_fabs)  # Output: 5.0

# 5. math.floor(x) - Membulatkan angka ke bawah (ke bilangan bulat terdekat)
y = 4.1
result_floor = math.floor(y)  # Membulatkan ke bawah 4.7
print(result_floor)  # Output: 4 -> as INT (interger)

# 6. math.ceil(x) - Membulatkan angka ke atas (ke bilangan bulat terdekat)
result_ceil = math.ceil(y)  # Membulatkan ke atas 4.7
print(result_ceil)  # Output: 5 

# 7. math.factorial(x) - Menghitung faktorial dari x (x!)
z = 5
result_factorial = math.factorial(z)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print(result_factorial)  # Output: 120


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Casting

# Mengubah dari Integer ke String
x = 10
x_as_string = str(x)
print(x_as_string)  # Output: '10' (tipe data string)

# Mengubah dari Float ke String
y = 3.14
y_as_string = str(y)
print(y_as_string)  # Output: '3.14' (tipe data string)

# Mengubah dari String ke Integer
string_to_int = "abc"
string_as_int = int(string_to_int)
print(string_as_int)  # Output: 123 (tipe data integer)

# Mengubah dari String ke Float
string_to_float = "45.67"
string_as_float = float(string_to_float)
print(string_as_float)  # Output: 45.67 (tipe data float)

# Mengubah dari Integer ke Float
z = 5
z_as_float = float(z)
print(z_as_float)  # Output: 5.0 (tipe data float)

# Mengubah dari Float ke Integer (perhatikan pembulatan)
w = 7.89
w_as_int = int(w)  # Akan membuang angka setelah koma
print(w_as_int)  # Output: 7 (tipe data integer)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# String Detail

# 1. Backslash untuk menampilkan tanda kutip satu di dalam string
string_with_single_quote = 'It\'s a beautiful day!'
print(string_with_single_quote)  # Output: It's a beautiful day!

# 2. Double backslash untuk menampilkan tanda backslash
string_with_backslash = "This is a backslash: \\"
print(string_with_backslash)  # Output: This is a backslash: \

# 3. Backslash n (\n) untuk membuat baris baru (new line)
string_with_newline = "Hello\nWorld"
print(string_with_newline)
# Output:
# Hello
# World

# Output: Hello    World (dengan tab di antara Hello dan World)

# 5. Backslash b (\b) untuk menambahkan backspace (menghapus karakter sebelumnya)
string_with_backspace = "Hello World\b!"
print(string_with_backspace)  # Output: Hello World! (karakter 'd' akan terhapus)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# String Detail Part 2

# 1. Menggunakan len() untuk mengetahui panjang string,tidak bisa digunakan di float dan interger
# kalau di collection data types seperti list,set,tuple & dictionary bisa.
halo_dunia = "Halo Dunia" 
print(len(halo_dunia))  # Output: 10, menghitung jumlah karakter dalam string

# 2. Menggunakan index() untuk mencari posisi kata "Dunia" dalam string
print(halo_dunia.index("Dunia"))  # Output: 5, index dimulai dari 0

# 3. Menggunakan split() untuk memecah string berdasarkan spasi by default
print(halo_dunia.split())  # Output: ['Halo', 'Dunia'], memisahkan string menjadi list
# note: jika memisahkan string selain dengan sepasi bisa di dalam function split misal
# aku ingin misahin 'Halo Dunia' dengan pemisahnya huruf D maka functinnya
print(halo_dunia.split('D')) # Output ['Halo ', 'unia']

# 4. Menggunakan lower() untuk mengubah string menjadi huruf kecil
print(halo_dunia.lower())  # Output: halo dunia, mengubah semua huruf menjadi kecil

# 5. Menggunakan upper() untuk mengubah string menjadi huruf besar
print(halo_dunia.upper())  # Output: HALO DUNIA, mengubah semua huruf menjadi besar

# 6. Menggunakan capitalize() untuk mengubah huruf pertama menjadi kapital
print(halo_dunia.capitalize())  # Output: Halo dunia, huruf pertama kapital dan sisanya kecil

#-----------------------------------------------------------------------------------------------------------------------------------------------
# String Slicing
halo_dunia = "Halo Dunia"
# indexing slicing dimulai dengan tanda kurung kotak '[]'
# dengan parameter [start : stop : step]
# Mengambil bagian dari string mulai dari index 0 sampai index 4
print(halo_dunia[0:4])  # Output: Halo

# Mengambil bagian dari string mulai dari index 5 sampai akhir
print(halo_dunia[5:])   # Output: Dunia

# Mengambil bagian dari string dari awal sampai index 4
print(halo_dunia[:5])   # Output: Halo

# Mengambil seluruh string (dari awal sampai akhir)
print(halo_dunia[:])    # Output: Halo Dunia

# Mengambil bagian dengan langkah tertentu (misalnya, setiap 2 karakter)
print(halo_dunia[::2])  # Output: Hl ui


#-----------------------------------------------------------------------------------------------------------------------------------------------
# String Concatenation (Penggabungan)

# Contoh 1: Penggabungan 2 string
apel = "Apel"
jeruk = "Jeruk"
c = apel + jeruk
print(c)  # Output: ApelJeruk

# Contoh 2: Penggabungan 4 string (termasuk spasi)
apel = "Apel"
spasi = " "
jeruk = "Jeruk"
mangga = "Mangga"
d = apel + spasi + jeruk + spasi + mangga
print(d)  # Output: Apel Jeruk Mangga

# Contoh 3: Penggabungan string dan integer (integer diubah menjadi string terlebih dahulu)
apel = "Apel"
spasi = " "
jumlah = 5
e = apel + spasi + str(jumlah)
print(e)  # Output: Apel 5

#-----------------------------------------------------------------------------------------------------------------------------------------------
# String function .format()

# Menggabungkan string dan angka dengan format()
nama = "Baron"
umur = 27

# Menyisipkan variabel ke dalam string dengan format()
output = "Nama saya {} dan umur saya {}".format(nama, umur)
print(output)  # Output: Nama saya Baron dan umur saya 25

# Format dengan nama placeholder
output = "Nama saya {nama} dan umur saya {umur}".format(nama=nama, umur=umur)
print(output)  # Output: Nama saya Baron dan umur saya 25

# Rekomendasi gampang biar pemakai
output = f"Nama saya {nama} dan umur saya {umur}"

# String Check
# Menggunakan in dan not in untuk memeriksa substring
kalimat = "Nama saya Baron"

x = "faroja" in kalimat
print(x)  # Output: False

# Mengecek apakah kata 'aya' ada dalam string
x = "aya" in kalimat
print(x)  # Output: True

# Mengecek apakah kata 'say' ada dalam string
x = "say" not in kalimat
print(x)  # Output: True

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Function Input

# Program untuk meminta input nama pengguna
nama_pengguna = input("Masukkan nama Anda: ")  # Meminta input nama pengguna
print("Nama Anda adalah:", nama_pengguna)  # Menampilkan nama yang dimasukkan

# Jika ingin mengubah input menjadi tipe data lain, seperti integer
umur = int(input("Masukkan umur Anda: "))  # Meminta input umur dan mengubahnya ke integer
print("Umur Anda adalah:", umur)  # Menampilkan umur yang dimasukkan

