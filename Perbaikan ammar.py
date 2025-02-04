listBuku = [
    {
     'nama buku': 'Laskar Pelangi',
     'penerbit': 'Bentang Pustaka',
     'tahun terbit': '2005',
     'terpinjam': '8',
     'status' : 'Available',
     },
    {
     'nama buku': 'Orang-orang Proyek',
     'penerbit': 'Gramedia Pustaka Utama',
     'tahun terbit': '2001',
     'terpinjam': '9',
     'status' : 'Unvailable',
     },
    {
     'nama buku': 'Ronggeng Dukuh Paruk',
     'penerbit': 'Gramedia Pustaka Utama',
     'tahun terbit': '1982',
     'terpinjam': '12',
     'status' : 'Available',
     },
    {
     'nama buku': 'Sang Pemimpi',
     'penerbit': 'Bentang Pustaka',
     'tahun terbit': '2006',
     'terpinjam': '1',
     'status' : 'Available',
     },
    {
     'nama buku': 'Cantik Itu Luka',
     'penerbit': 'Gramedia Pustaka Utama',
     'tahun terbit': '2002',
     'terpinjam': '9',
     'status' : 'Available',
     },
    {
     'nama buku': 'Rectoverso',
     'penerbit': 'Truedee Books',
     'tahun terbit': '2008',
     'terpinjam': '7',
     'status' : 'Unvailable',
     },
    {
     'nama buku': 'Ayat-ayat Cinta',
     'penerbit': 'Republika',
     'tahun terbit': '2004',
     'terpinjam': '9',
     'status' : 'Available',
     },
    {
     'nama buku': 'Outliers: The Story of Success',
     'penerbit': 'Gramedia Pustaka',
     'tahun terbit': '2010',
     'terpinjam': '10',
     'status' : 'Unavailable',
     },
    {
     'nama buku': 'The Power of Habit',
     'penerbit': 'Gramedia Pustaka Utama',
     'tahun terbit': '2013',
     'terpinjam': '15',
     'status' : 'Available',
     },
    {
     'nama buku': 'Perahu Kertas',
     'penerbit': 'Bentang Pustaka',
     'tahun terbit': '2009',
     'terpinjam': '4',
     'status' : 'Unavailable',
     },
    ]
exitApp = False
# inputPenerbit = ''
# nomor = 0

def mainMenu():
    print('i.   Daftar Buku')
    print('ii.  Mendaftar Buku Baru')
    print('iii. Hapus Buku')
    print('iv.  Kembali')
    print('v.   Exit')
    
def daftarBuku():
    print('\n----------Daftar Buku----------')
    nomor = 0
    for daftarBuku in range (0, len(listBuku)):
        nomor += 1
        if nomor > len(listBuku):
            nomor = 0
        else:
            print(f'{nomor}.  {listBuku[daftarBuku]['nama buku']}')

def inputBukuBaru():
    print('----------Memasukkan Buku Baru----------')
    namaBuku = input('Nama buku: ')
    namaPenerbit = input('Nama penerbit: ')
    tahunTerbitBuku = input('Tahun terbit: ')
    bukuBaru = {     
                'nama buku': namaBuku,
                'penerbit': namaPenerbit,
                'tahun terbit': tahunTerbitBuku,
                'terpinjam': '0',
                'status' : 'Available',
                }
    listBuku.append(bukuBaru)
    print('Buku telah disimpan! Silahkan ketik "Daftar Buku" untuk pengecekan buku baru atau ketik "ii" untuk mendaftarkan buku baru.')
    print('')
    # mainMenu()

def menghapusBuku():
    print('')
    daftarBuku()
    while True:
        bukuYangDihapus = input('Buku yang ingin dihapus (ketik berdasarkan nomor urut): ')
        # intBukuYangDihapus = int(bukuYangDihapus)
        if bukuYangDihapus.isdigit():
            bukuYangDihapus = int(bukuYangDihapus)
            print(f'Buku {listBuku[bukuYangDihapus - 1]['nama buku']} berhasil dihapus!')
            return listBuku.pop(bukuYangDihapus - 1)
        else:
            print('Input salah! Mohon masukkan kembali dengan benar!')

def filterPenerbit(penerbit):
    if inputPenerbit in penerbit['penerbit']:
        return True
    else:
        return False
def penerbit():
    variableFilterPenerbit = filter(filterPenerbit, listBuku)
    filterListPenerbit = list(variableFilterPenerbit)
    count = 0
    print(f'----------{filterListPenerbit[0]['Penerbit'.lower()]}----------')
    for i in range (0,len(filterListPenerbit)):
        count += 1
        if count > len(listBuku):
            count = 0
        else:
            print(f'{count}.  {filterListPenerbit[i]['Nama Buku'.lower()]}')

def filterTahunTerbit(tahunTerbit):
    if inputTahunTerbit in tahunTerbit['tahun terbit']:
        return True
    else:
        return False
def tahunTerbit():
    variableFilterTahunTerbit = filter(filterTahunTerbit, listBuku)
    filterListTahunTerbit = list(variableFilterTahunTerbit)
    count = 0
    for i in range (0,len(filterListTahunTerbit)):
        count += 1
        if count > len(listBuku):
            count = 0
        else:
            print(f'{count}.  {filterListTahunTerbit[i]['Nama Buku'.lower()]}')
    print('')
            
def filterStatusBuku(status):
    if status['status'] == 'Available':
        return True
    else:
        return False
def statusBuku():
    variableStatusBuku = filter(filterStatusBuku, listBuku)
    filterListStatusBuku = list(variableStatusBuku)
    count = 0
    for i in range (0,len(filterListStatusBuku)):
        count += 1
        if count > len(listBuku):
            count = 0
        else:
            print(f'{count}.  {filterListStatusBuku[i]['Nama Buku'.lower()]}')
    print('')

def kategori():
    print('i.   Penerbit')
    print('ii.  Tahun terbit')
    print('iii. Tersedia')
    print('iv.  exit kategori')

daftarBuku()
while True:
    if exitApp == True:
        break
    print('')
    pilihKategori = input('Ingin memilih berdasarkan kategori? (YES/NO) \n')
    if pilihKategori == 'YES' or pilihKategori=='yes' or pilihKategori=='y' or pilihKategori=='Yes' or pilihKategori=='Ya'or pilihKategori=='ya':
        print('\nCari buku sesuai ketegori: ')
        while True:
            kategori()
            inputKategori = str(input(f'Pilihan: '))
            print('')
            if inputKategori == 'i' or inputKategori =='Penerbit' or inputKategori=='penerbit' or inputKategori =='1':
                while True:
                    inputPenerbit = input('Masukkan nama Penerbit: ')
                    cekBuku = True
                    for indexListBuku in range (0,len(listBuku)):
                        if inputPenerbit not in listBuku[indexListBuku]['penerbit']:
                            cekBuku = False
                        else:
                            cekBuku = True
                            break
                    if cekBuku == False:
                        print('Penerbit yang anda masukkan salah atau tidak terdaftar, mohon dimasukkan kembali.')
                    else:
                        penerbit()
                        input('(tekan enter untuk lanjut)')
                        print('')
                        break
            elif inputKategori == 'ii' or inputKategori=='Tahun Terbit' or inputKategori=='Tahun terbit' or inputKategori=='tahun Terbit' or inputKategori=='tahunterbit' or inputKategori=='Tahunterbit' or inputKategori=='tahunTerbit' or inputKategori =='2':
                while True:
                    inputTahunTerbit = input('Masukkan Tahun Terbit: ')
                    cekBuku = False
                    for indexListBuku in range (0,len(listBuku)):
                        if inputTahunTerbit not in listBuku[indexListBuku]['tahun terbit']:
                            cekBuku = False
                        else:
                            cekBuku = True
                            break
                    if cekBuku == False:
                        print('Anda salah memasukkan tahun terbit, mohon dimasukkan kembali.')
                    else:
                        tahunTerbit()
                        input('(tekan enter untuk lanjut)')
                        print('')
                        break
            elif inputKategori == 'iii' or  inputKategori =='Tersedia' or  inputKategori =='tersedia' or inputKategori =='3':
                statusBuku()
                input('(tekan enter untuk lanjut)')
                break
            elif inputKategori == 'iv' or inputKategori == 'exit' or  inputKategori == 'exit kategori' or  inputKategori == 'Exit Kategori'or  inputKategori =='Exit kategori'or  inputKategori == 'exitkategori' or inputKategori =='4':
                break
            else:
                print('')
                print('Oops pilihannya tidak tersedia, silahkan masukkan lagi')
    elif pilihKategori == 'NO' or pilihKategori=='no' or pilihKategori=='No' or pilihKategori == 'n' or pilihKategori == 'N':
        while True:
            print('')
            mainMenu()
            inputMainMenu = input('Pilihan: ')
            if inputMainMenu == 'i'or inputMainMenu == 'daftar buku'or inputMainMenu == 'Daftar Buku'or inputMainMenu == 'Daftarbuku' or inputMainMenu == 'Daftar buku' or inputMainMenu == 'daftarbuku' or  inputMainMenu == '1':
                daftarBuku()
                input('(tekan enter untuk lanjut)')
                continue
            elif inputMainMenu == 'ii' or inputMainMenu == 'mendaftar buku baru' or inputMainMenu == 'buku baru' or  inputMainMenu == '2':
                inputBukuBaru()
                input('(tekan enter untuk lanjut)')
                continue
            elif inputMainMenu == 'iii' or  inputMainMenu == 'Hapus Buku' or  inputMainMenu == 'Hapus buku' or  inputMainMenu == 'hapusbuku' or inputMainMenu =='Hapusbuku' or inputMainMenu == 'hapus buku' or  inputMainMenu == '3':
                menghapusBuku()
                input('(tekan enter untuk lanjut)')
                continue
            elif inputMainMenu == 'iv' or inputMainMenu == 'kembali' or inputMainMenu == 'Kembali' or  inputMainMenu == '4':
                break
            elif inputMainMenu == 'exit' or inputMainMenu == 'v' or inputMainMenu =='5':
                exitApp = True
                break
    else:
        continue