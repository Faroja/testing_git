# Kenapa Perlu Try-Except?
# Misalnya, kita ingin meminta input angka dari user menggunakan int(input()).
#  Jika user memasukkan teks atau karakter lain yang bukan angka, program akan error dan langsung berhenti.
# cth:
num = int(input("Masukkan angka: "))  # Jika input "halo", akan error
print(f"Angka yang dimasukkan: {num}")

# Menggunakan Try-Except untuk Menangani Error
try:
    num = int(input("Masukkan angka: "))
    print(f"Angka yang dimasukkan: {num}")
except ValueError:
    print("Input harus berupa angka! Coba lagi.")

# Kode dalam try: akan dicoba dieksekusi.
# Jika terjadi ValueError, program tidak akan keluar, melainkan menjalankan bagian except.
# Program tetap berjalan tanpa langsung crash.

# Menangani Banyak Jenis Error
# Kadang kita butuh menangani lebih dari satu jenis error.
# Misalnya, jika user menekan Ctrl+C saat input, program akan keluar dengan KeyboardInterrupt.

try:
    num = int(input("Masukkan angka: "))
    print(f"Angka yang dimasukkan: {num}")
except ValueError:
    print("Input harus berupa angka! Coba lagi.")
except KeyboardInterrupt:
    print("\nInput dibatalkan oleh user.")
except Exception as e:
    print(f"Terjadi error lain: {e}")

# Kelebihan pendekatan ini:

# ValueError → Untuk salah input yang bukan angka.
# KeyboardInterrupt → Jika user menekan Ctrl+C.
# Exception as e → Menangani error lain yang tidak terduga.

#  Menggunakan Try-Except dalam Loop (Agar User Bisa Coba Lagi)

while True:
    try:
        num = int(input("Masukkan angka: "))
        break  # Keluar dari loop jika sukses
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
    
print(f"Angka yang dimasukkan: {num}")

# Kelebihan
# 1.Program tidak keluar meskipun user salah input.
# 2. User bisa mencoba lagi sampai input benar.

# Try-Except-Finally
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File tidak ditemukan.")
finally: # Jika kita ingin menjalankan kode terlepas dari apakah error terjadi atau tidak, kita bisa memakai ini.
    print("Program selesai.")
#  Fungsi finally:
# Bagian ini akan selalu dijalankan, baik ada error atau tidak.

# Kesimpulan
# try-except sangat penting untuk menjaga aplikasi agar tidak langsung keluar saat terjadi error.
# Bisa menangani berbagai jenis error dengan except.
# Bisa digunakan dalam loop agar user bisa coba lagi jika input salah.
# Bisa menambahkan finally untuk kode yang harus selalu dieksekusi.