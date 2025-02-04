# enumerate() adalah fungsi built-in di Python yang digunakan untuk
#  mengiterasi sebuah iterable (seperti list) 
#  dan menghasilkan pasangan yang terdiri
#  dari index dan nilai dari elemen dalam iterable tersebut.

list_buku = ["Laskar Pelangi", "Ayat-Ayat Cinta", "Genius Kampus"]

for index, buku in enumerate(list_buku):
    print(index, buku)
# Output
# 0 Laskar Pelangi
# 1 Ayat-Ayat Cinta
# 2 Genius Kampus
data = [[i, buku["Penerbit"], buku["Judul buku"], buku["Tahun diterbitkan"], buku["Jumlah dipinjam"], buku["Status"]]
            for i, buku in enumerate(list_buku)]