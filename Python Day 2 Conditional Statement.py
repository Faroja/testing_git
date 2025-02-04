# Contoh penggunaan operator perbandingan di Python

a = 10
b = 5

# Lebih besar dari (>)
print(a > b)  # Output: True, karena 10 lebih besar dari 5

# Lebih kecil dari (<)
print(a < b)  # Output: False, karena 10 tidak lebih kecil dari 5

# Lebih besar atau sama dengan (>=)
print(a >= b)  # Output: True, karena 10 lebih besar dari 5

# Lebih kecil atau sama dengan (<=)
print(a <= b)  # Output: False, karena 10 tidak lebih kecil atau sama dengan 5

# Tidak sama dengan (!=)
print(a != b)  # Output: True, karena 10 tidak sama dengan 5

# Sama dengan (==)
print(a == b)  # Output: False, karena 10 tidak sama dengan 5

# AND OR 

a = 10
b = 5
c = 15

# Operator AND (mengembalikan True jika kedua kondisi benar)
print(a > b and c > a)  # Output: True, karena 10 > 5 dan 15 > 10

# Operator OR (mengembalikan True jika salah satu kondisi benar)
print(a < b or c > a)  # Output: True, karena 15 > 10 (kondisi kedua benar)

# Operator NOT (mengubah hasil kondisi, True menjadi False dan sebaliknya)
print(not a < b)  # Output: True, karena a < b adalah False, jadi not membaliknya menjadi True

# (Start)
#    |
#    v
# (Pengajuan Permohonan)
#    |
#    v
#    (Decision: Umur Pemohon)
#    |-->[False]--> (End)
#    |-->[True]--> (Kirim Email Konfirmasi)
#                     |
#                     v
#                (Proses Berikutnya)
#                     |
#                     v
#                    (End)


umur = int(input("Masukkan umur pemohon: "))

# Decision: Memeriksa apakah umur memenuhi syarat
if umur >= 18:
    # Jika umur memenuhi syarat (True), kirim email konfirmasi
    print("Permohonan diterima. Kami akan mengirimkan email konfirmasi.")
    
    # Proses berikutnya
    print("Melakukan proses verifikasi lebih lanjut...")
else:
    # Jika umur tidak memenuhi syarat (False), langsung End
    print("Umur pemohon tidak memenuhi syarat. Proses selesai.")


# Penggunaan elif
# Input nilai dari user
nilai = int(input("Masukkan nilai murid: "))

# Menentukan grade berdasarkan nilai
if nilai >= 90 and nilai <= 100:
    print("Grade: A")
elif nilai >= 80 and nilai < 90:
    print("Grade: B")
elif nilai >= 70 and nilai < 80:
    print("Grade: C")
elif nilai >= 60 and nilai < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Operator XOR (^)
# Operator XOR (Exclusive OR) mengembalikan True jika kedua kondisi berbeda (satu True, satu False). 
# Jika kedua kondisi sama (baik True-True atau False-False), hasilnya adalah False.

total_belanja = 600000  # Contoh: total belanja pelanggan
is_vip_member = False   # Contoh: status keanggotaan pelanggan

# Validasi promosi
if (total_belanja > 500000) ^ is_vip_member:
    print("Selamat! Anda mendapatkan promosi.")
else:
    print("Maaf, Anda tidak memenuhi syarat untuk promosi.")

# total_belanja > 500000:
# Akan bernilai True jika pelanggan belanja lebih dari Rp500.000.
# is_vip_member:
# Akan bernilai True jika pelanggan adalah anggota VIP.
# (total_belanja > 500000) ^ is_vip_member:
# Menghasilkan True jika:
# Pelanggan hanya belanja lebih dari Rp500.000 atau
# Pelanggan hanya anggota VIP.