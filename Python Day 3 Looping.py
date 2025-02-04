# Introduction to Looping in Python

# Apa itu loop statements?
# Loop statements adalah sebuah perintah yang memungkinkan kita 
# untuk mengulang pekerjaan serupa selama kondisi tertentu terpenuhi.

# Kapan kita membutuhkan loop statements?
# Kita membutuhkan loop statements saat adanya suatu perulangan 
# dalam proses yang serupa, sehingga mempermudah pengerjaan.

# Kenapa kita memerlukan loop statements?
# Loop statements membantu kita menulis kode secara efisien,
# terutama untuk menangani proses yang dilakukan berulang-ulang.

# Sekarang, bagaimana cara menggunakan loop statements di Python?
# Di Python, kita memiliki 2 jenis loop utama yang sering digunakan:
# 1. For Loop
# 2. While Loop

# -----------------------------------------------------------------------------------------------------------------------------------------
# While Loop di Python

# While loop memiliki syntax sebagai berikut:
# while kondisi:
#     # kode yang akan dijalankan selama kondisi bernilai True

# Penulisan dimulai dengan keyword `while`, diikuti dengan kondisi yang akan menghasilkan
# nilai Boolean (True atau False). Kondisi ini bisa berupa perbandingan atau variable.
# Jika kondisi bernilai True, maka komputer akan menjalankan kode yang ada di dalam blok while.
# Setelah itu, komputer akan kembali mengevaluasi kondisi.
# Jika kondisi tetap True, kode akan diulang. Jika kondisi menjadi False,
# komputer akan berhenti menjalankan while dan melanjutkan ke kode setelahnya.

# Contoh penggunaan while loop:
# Kita akan membuat program sederhana untuk menghitung mundur dari 5.

# Inisialisasi nilai awal
count = 5

# While loop
while count > 0:  # Kondisi: selama count lebih besar dari 0
    print(f"Countdown: {count}")  # Cetak nilai count
    count -= 1  # Kurangi nilai count dengan 1 di setiap loop

# Penjelasan kode:
# 1. Pada loop pertama, count = 5, kondisi count > 0 bernilai True.
#    Program mencetak "Countdown: 5", kemudian mengurangi nilai count menjadi 4.
# 2. Loop berikutnya, kondisi count > 0 tetap True (count = 4), 
#    program mencetak "Countdown: 4" dan mengurangi count menjadi 3.
# 3. Proses ini terus diulang sampai count = 0.
# 4. Ketika count = 0, kondisi count > 0 bernilai False, 
#    sehingga while loop berhenti dan program selesai.

# Hasil dari kode di atas:
# Countdown: 5
# Countdown: 4
# Countdown: 3
# Countdown: 2
# Countdown: 1

# Catatan:
# Sangat penting untuk memastikan ada mekanisme untuk mengubah kondisi menjadi False,
# seperti mengurangi nilai count di atas, agar while loop tidak berjalan selamanya (infinite loop).

# -----------------------------------------------------------------------------------------------------------------------------------------

# Syntax for loop di Python:
# for variable in data:
#     # kode yang akan dijalankan untuk setiap item di data

# Setelah keyword `in`, kita menentukan kumpulan data yang ingin di-loop, 
# seperti range atau string atau collection list,tuple,dictionary,set. 

# Sebelum membahas lebih jauh, mari kita pelajari apa itu range function.

# Range Function di Python
# Range function dapat menerima tiga parameter: start, stop, dan step.

# 1. Parameter `start`: menentukan awal urutan angka (opsional, default 0).
# 2. Parameter `stop`: menentukan akhir urutan angka (wajib, tidak termasuk nilai ini).
# 3. Parameter `step`: menentukan nilai penambahan atau pengurangan (opsional, default 1).

# Contoh penggunaan range:
print("Contoh penggunaan range:")
for i in range(1, 6):  # Start = 1, Stop = 6 (tidak termasuk 6), Step = 1
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Contoh penggunaan range dengan step:
print("\nContoh range dengan step:")
for i in range(0, 10, 2):  # Start = 0, Stop = 10, Step = 2
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8

# -----------------------------------------------------------------------------------------------------------------------------------------
# For Loop dengan String
# String adalah kumpulan karakter, sehingga kita bisa melakukan loop pada setiap karakternya.

# Contoh for loop dengan string:
print("\nContoh for loop dengan string:")
text = "Python"
for char in text:  # Loop melalui setiap karakter di string "Python"
    print(char)

# Output:
# P
# y
# t
# h
# o
# n

# Penjelasan Flow For Loop:
# 1. For loop membaca setiap item di kumpulan data (seperti range atau string) satu per satu.
# 2. Setiap item disimpan di variable sementara (contoh: `i` atau `char`).
# 3. Kode dalam blok for akan dijalankan untuk setiap item.
# 4. Ketika semua item selesai dibaca, for loop berhenti.

# Flow chart dari for loop sangat mirip dengan while loop, tetapi kondisinya lebih sederhana:
# For loop akan terus berjalan selama masih ada item yang belum dibaca dalam kumpulan data.

# Catatan:
# For loop sangat fleksibel dan berguna untuk bekerja dengan tipe data koleksi lainnya
# seperti list, tuple, dictionary, dan set.

# Keyword Break dan Continue

# Python memiliki dua keyword khusus untuk mengontrol loop: `break` dan `continue`.
# 1. `break`: Menghentikan proses loop sepenuhnya.
# 2. `continue`: Melewatkan satu iterasi loop dan langsung ke iterasi berikutnya.

# Contoh Penggunaan Break:
# Kita ingin mencari angka pertama yang habis dibagi 3 dalam range tertentu.
print("\nContoh penggunaan break:")
for num in range(1, 10):
    if num % 3 == 0:  # Kondisi break: angka habis dibagi 3
        print(f"Angka pertama yang habis dibagi 3 adalah: {num}")
        break  # Menghentikan loop jika kondisi terpenuhi

# Output:
# Angka pertama yang habis dibagi 3 adalah: 3

# Penjelasan:
# - Loop dimulai dari angka 1 hingga 9.
# - Pada iterasi pertama (num = 1), kondisi num % 3 == 0 bernilai False, sehingga loop berlanjut.
# - Ketika num = 3, kondisi bernilai True, sehingga `break` dijalankan dan loop berhenti.

# Contoh Penggunaan Continue:
# Kita ingin mencetak semua angka dari 1 sampai 10, kecuali angka yang habis dibagi 2 (angka genap).
print("\nContoh penggunaan continue:")
for num in range(1, 11):
    if num % 2 == 0:  # Kondisi continue: angka genap
        continue  # Melewatkan iterasi jika kondisi terpenuhi
    print(num)
    
# Output:
# 1
# 3
# 5
# 7
# 9

# Penjelasan:
# - Loop berjalan dari angka 1 hingga 10.
# - Pada setiap iterasi, jika num % 2 == 0 bernilai True (angka genap),
#   keyword `continue` dijalankan dan iterasi tersebut dilewati.
# - Angka yang dicetak adalah angka ganjil.

# -----------------------------------------------------------------------------------------------------------------------------------------

# Gambar dengan Looping

# Awalnya kita bikin variabel kosong untuk nyimpen hasilnya
stars = ""

# Loop ini bakal jalan 5 kali, dari 0 sampai 4
for i in range(5):
    # Tiap kali loop, kita tambahin '* ' ke variabel stars
    stars += '* '

# Setelah loop selesai, kita print isi variabel stars
print(stars)

# -----------------------------------------------------------------------------------------------------------------------------------------

# Versi Horizontal hanya beda bagian looping ada '\n' artinya new line (baris baru)
stars = ""
for i in range(5):
    stars += '*\n'
print(stars)

# -----------------------------------------------------------------------------------------------------------------------------------------

# Versi Kotak (Double Looping)
# 1. Kita mulai dengan mendeklarasikan variabel 'stars' yang kosong
stars = ""

# 2. Loop pertama untuk baris (5 kali)
for i in range(5):
    
    # 3. Loop kedua untuk kolom (5 kali)
    for j in range(5):
        # 4. Tambahkan '* ' di setiap kolom
        stars += '* '
    
    # 5. Setelah selesai satu baris, tambahkan baris baru
    stars += '*\n'

# 6. Setelah kedua loop selesai, tampilkan hasil dari 'stars'
print(stars)

# 1. Loop pertama (for i in range(5)) mengatur jumlah baris (5 baris).
# 2. Loop kedua (for j in range(5)) mengatur jumlah kolom dalam setiap baris (5 kolom).
# 3. Setelah mencetak bintang di setiap kolom, kita menambahkan \n agar setelah baris selesai, pindah ke baris baru.

# -----------------------------------------------------------------------------------------------------------------------------------------

# Versi Segitiga (Double Looping)
# 1. Kita mulai dengan mendeklarasikan variabel 'stars' yang kosong
stars = ""

# 2. Loop pertama untuk baris (5 kali)
for i in range(5):
    
    # 3. Loop kedua untuk kolom, jumlah kolom bertambah setiap baris (i+1)
    for j in range(i+1):
        # 4. Tambahkan '* ' di setiap kolom
        stars += '* '
    
    # 5. Setelah selesai satu baris, tambahkan baris baru
    stars += '*\n'

# 6. Setelah kedua loop selesai, tampilkan hasil dari 'stars'
print(stars)

# 1. Loop pertama (for i in range(5)): Loop ini mengatur jumlah baris yang akan dicetak (5 baris).
# 2. Loop kedua (for j in range(i+1)): Di sini, jumlah kolom yang dicetak di setiap baris bertambah setiap kali i bertambah. 
#   Misalnya, di baris pertama (i=0), hanya satu bintang yang dicetak, di baris kedua (i=1), dua bintang, dan seterusnya.
# 3. Setiap selesai mencetak bintang untuk satu baris, stars += '*\n' akan memastikan bahwa baris baru dimulai setelah kolom selesai dicetak

# -----------------------------------------------------------------------------------------------------------------------------------------
# Piramida Terbalik dan Biasa

stars = ''
# Tentukan ukuran piramida (5 baris)
size = 5

# Bagian pertama: membuat piramida terbalik
for i in range(size):
    # Loop untuk menambahkan bintang, semakin sedikit bintang di setiap baris
    for j in range(size - i):
        stars += '* '  # Tambahkan bintang
    stars += '\n'  # Pindah ke baris baru setelah mencetak bintang

# Bagian kedua: membuat piramida normal
for i in range(1, size):
    # Loop untuk menambahkan bintang, semakin banyak bintang di setiap baris
    for j in range(i + 1):
        stars += '* '  # Tambahkan bintang
    stars += '\n'  # Pindah ke baris baru setelah mencetak bintang

# Cetak hasil akhirnya
print(stars)

# Penjelasan:
# Bagian pertama: Membuat piramida terbalik dengan mengurangi jumlah bintang di setiap baris.
#   for j in range(size - i): Mengurangi jumlah bintang dengan bertambahnya baris.
# Bagian kedua: Membuat piramida normal dengan menambah jumlah bintang di setiap baris.
#   for j in range(i + 1): Menambah jumlah bintang dengan bertambahnya baris.

# -----------------------------------------------------------------------------------------------------------------------------------------

# Pola Belah Ketupat

stars = ''
# Tentukan ukuran belah ketupat (5 baris)
size = 5

# Bagian pertama: membentuk bagian atas belah ketupat
for i in range(size):
    # Tambahkan spasi agar bintang berada di tengah
    for j in range(size - i):
        stars += '  '  # Menambahkan spasi untuk meratakan bintang
    # Tambahkan bintang bertambah sesuai barisnya
    for k in range(i * 2 + 1):
        stars += '* '  # Tambahkan bintang
    stars += '\n'  # Pindah ke baris baru setelah mencetak bintang

# Bagian kedua: membentuk bagian bawah belah ketupat
for i in range(1, size):
    # Tambahkan spasi agar bintang tetap berada di tengah
    for j in range(i + 1):
        stars += '  '  # Menambahkan spasi untuk meratakan bintang
    # Kurangi jumlah bintang sesuai barisnya
    for k in range((size * 2) - (i * 2) - 1):
        stars += '* '  # Tambahkan bintang
    stars += '\n'  # Pindah ke baris baru setelah mencetak bintang

# Cetak hasil akhirnya
print(stars)

# Bagian pertama: Membuat bagian atas dari belah ketupat dengan menambahkan spasi dan bintang yang bertambah.
#   for j in range(size - i): Menambahkan spasi di setiap baris untuk meratakan bintang.
#   for k in range(i * 2 + 1): Menambahkan bintang sesuai jumlah baris (bertambah setiap baris).
# Bagian kedua: Membuat bagian bawah dari belah ketupat dengan menambahkan spasi dan mengurangi jumlah bintang.
#   for k in range((size * 2) - (i * 2) - 1): Mengurangi jumlah bintang sesuai dengan urutan barisnya.
