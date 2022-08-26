
daftarAsetMobil = [
    {'Nomor Plat' : 'P 1001 AA', 'Merek' : 'Lamborgini', 'Tipe' : 'Aventador', 'Harga Sewa' : 990000, 'Jenis' : 'Sport', 'Tahun' : 2022, 'Warna' : 'Orange', 'Kapasitas' : 2},
    {'Nomor Plat' : 'P 1002 AB', 'Merek' : 'Daihatsu', 'Tipe' : 'Ayla', 'Harga Sewa' : 100000, 'Jenis' : 'Hatchback', 'Tahun' : 2010, 'Warna' : 'Putih', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1003 AC', 'Merek' : 'Honda', 'Tipe' : 'Jazz', 'Harga Sewa' : 150000, 'Jenis' : 'Hatchback', 'Tahun' : 2017, 'Warna' : 'Kuning', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1004 AD', 'Merek' : 'Honda', 'Tipe' : 'HRV', 'Harga Sewa' : 300000, 'Jenis' : 'SUV', 'Tahun' : 2015, 'Warna' : 'Abu', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1005 AE', 'Merek' : 'Toyota', 'Tipe' : 'Avanza', 'Harga Sewa' : 150000, 'Jenis' : 'MPV', 'Tahun' : 2016, 'Warna' : 'Hitam', 'Kapasitas' : 7},
    {'Nomor Plat' : 'P 1006 AF', 'Merek' : 'Mazda', 'Tipe' : 'CX-5', 'Harga Sewa' : 300000, 'Jenis' : 'SUV', 'Tahun' : 2017, 'Warna' : 'Merah', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1007 AG', 'Merek' : 'Toyota', 'Tipe' : 'Alphard', 'Harga Sewa' : 600000, 'Jenis' : 'Luxury', 'Tahun' : 2020, 'Warna' : 'Putih', 'Kapasitas' : 7},
    {'Nomor Plat' : 'P 1008 AH', 'Merek' : 'Suzuki', 'Tipe' : 'Baleno', 'Harga Sewa' : 200000, 'Jenis' : 'City Car', 'Tahun' : 2012, 'Warna' : 'Merah', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1009 AI', 'Merek' : 'Mitsubishi', 'Tipe' : 'Lancer', 'Harga Sewa' : 500000, 'Jenis' : 'Sedan', 'Tahun' : 1995, 'Warna' : 'Abu', 'Kapasitas' : 5},
    ]

daftarMobilTersedia = [
    {'Nomor Plat' : 'P 1001 AA', 'Merek' : 'Lamborgini', 'Tipe' : 'Aventador', 'Harga Sewa' : 990000, 'Jenis' : 'Sport', 'Tahun' : 2022, 'Warna' : 'Orange', 'Kapasitas' : 2},
    {'Nomor Plat' : 'P 1002 AB', 'Merek' : 'Daihatsu', 'Tipe' : 'Ayla', 'Harga Sewa' : 100000, 'Jenis' : 'Hatchback', 'Tahun' : 2010, 'Warna' : 'Putih', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1003 AC', 'Merek' : 'Honda', 'Tipe' : 'Jazz', 'Harga Sewa' : 150000, 'Jenis' : 'Hatchback', 'Tahun' : 2017, 'Warna' : 'Kuning', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1004 AD', 'Merek' : 'Honda', 'Tipe' : 'HRV', 'Harga Sewa' : 300000, 'Jenis' : 'SUV', 'Tahun' : 2015, 'Warna' : 'Abu', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1005 AE', 'Merek' : 'Toyota', 'Tipe' : 'Avanza', 'Harga Sewa' : 150000, 'Jenis' : 'MPV', 'Tahun' : 2016, 'Warna' : 'Hitam', 'Kapasitas' : 7},
    {'Nomor Plat' : 'P 1006 AF', 'Merek' : 'Mazda', 'Tipe' : 'CX-5', 'Harga Sewa' : 300000, 'Jenis' : 'SUV', 'Tahun' : 2017, 'Warna' : 'Merah', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1007 AG', 'Merek' : 'Toyota', 'Tipe' : 'Alphard', 'Harga Sewa' : 600000, 'Jenis' : 'Luxury', 'Tahun' : 2020, 'Warna' : 'Putih', 'Kapasitas' : 7},
    {'Nomor Plat' : 'P 1008 AH', 'Merek' : 'Suzuki', 'Tipe' : 'Baleno', 'Harga Sewa' : 200000, 'Jenis' : 'City Car', 'Tahun' : 2012, 'Warna' : 'Merah', 'Kapasitas' : 5},
    {'Nomor Plat' : 'P 1009 AI', 'Merek' : 'Mitsubishi', 'Tipe' : 'Lancer', 'Harga Sewa' : 500000, 'Jenis' : 'Sedan', 'Tahun' : 1995, 'Warna' : 'Abu', 'Kapasitas' : 5},
    ]

daftarMobilDisewa = []
keranjangSementara = []


# SECTION SHOW DATA ASET MOBIL =======================================================================================================================================================================
def funcTampilkanSeluruhAsetMobil():
    print ('''
-----------------------------
     DAFTAR SELURUH MOBIL
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
    for i in range(len(daftarAsetMobil)):
        singkatanTipe = ''
        singkatanMerek = ''
        if len(daftarAsetMobil[i]['Tipe']) > 7:
            singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
            if len(daftarAsetMobil[i]['Merek']) > 6:
                singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
            elif len(daftarAsetMobil[i]['Merek']) <= 6:
                singkatanMerek = daftarAsetMobil[i]['Merek']
        elif len(daftarAsetMobil[i]['Tipe']) <= 7:
            singkatanTipe = daftarAsetMobil[i]['Tipe']
            if len(daftarAsetMobil[i]['Merek']) > 6:
                singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
            elif len(daftarAsetMobil[i]['Merek']) <= 6:
                singkatanMerek = daftarAsetMobil[i]['Merek']

        print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
        .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))
    


# SECTION PILIHAN MENU CUSTOMER =======================================================================================================================================================================
def funcMenuCustomer():
    pilihanMenuCustomer = (input('''
----------------------
     MENU CUSTOMER
----------------------

1. Sewa Mobil
2. Pengembalian Mobil

0. Kembali ke Halaman Utama

Pilih menu: '''))
    if pilihanMenuCustomer == '1':
        funcSewaCustomer()
    elif pilihanMenuCustomer == '2':
        funcPengembalian()
    elif pilihanMenuCustomer == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcMenuCustomer()



# SECTION PILIHAN MENU CUSTOMER => SEWA =======================================================================================================================================================================
def funcSewaCustomer():
    pilihanMenuSewa = (input('''
----------------------
      MENU SEWA
----------------------

1. Tampilkan Seluruh Mobil
2. Cari Kategori Mobil

9. Kembali ke Menu Customer
0. Kembali ke Halaman Utama

Pilih menu: '''))
    if pilihanMenuSewa == '1':
        funcSewaTampilkanSemua()
    elif pilihanMenuSewa == '2':
        funcSewaSearch()
    elif pilihanMenuSewa == '9':
        funcMenuCustomer ()
    elif pilihanMenuSewa == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcSewaCustomer()



# SECTION MENU SEWA CUSTOMER => TAMPILKAN SELURUH MOBIL  =======================================================================================================================================================================
def funcSewaTampilkanSemua():
    
    funcTampilkanSeluruhAsetMobil()

    konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
    if konfirmasiLanjut == '1':    

        pilihanMobil = input('''
Masukkan Nomor Plat mobil yang ingin Anda Sewa :    
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == pilihanMobil:
                print ('''
-----------------------------
           KERANJANG
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
            .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                keranjangSementara.append(daftarAsetMobil[i])
                daftarMobilDisewa.append(daftarAsetMobil[i])
                del daftarMobilTersedia[i]    

                funcKonfirmasiPesananKeranjang()
            
    elif konfirmasiLanjut == '2':
        funcSewaCustomer()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)       
        funcSewaTampilkanSemua()
            


# SECTION MENU SEWA CUSTOMER => CARI KATERGORI MOBIL  =======================================================================================================================================================================
def funcSewaSearch():
    inputSewaSearch = (input('''
-----------------------------
     CARI SESUAI KATEGORI
-----------------------------

1. Merek Mobil
2. Jenis Mobil
3. Warna Mobil
4. Kapasitas Mobil

9. Kembali ke Menu Sewa
0. Kembali ke Halama Utama

Pilih menu: '''))

    if inputSewaSearch == '1':
        inputSearchMerek = input('''
-----------------------------
     CARI SESUAI MEREK
-----------------------------        
    
Masukkan Merek Mobil yang Dicari : ''')

        print ('''
-----------------------------
     DAFTAR SELURUH MOBIL
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Merek'].lower() == inputSearchMerek.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
        if konfirmasiLanjut == '1':
    
            pilihanMobil = input('''
Masukkan Nomor Plat mobil yang ingin Anda Sewa :    
''')
            for i in range(len(daftarAsetMobil)):
                if daftarAsetMobil[i]['Nomor Plat'].lower() == pilihanMobil.lower():
                    print ('''
-----------------------------
           KERANJANG
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                    keranjangSementara.append(daftarAsetMobil[i])
                    daftarMobilDisewa.append(daftarAsetMobil[i])
                    del daftarMobilTersedia[i]    

                    funcKonfirmasiPesananKeranjang()
        elif konfirmasiLanjut == '2':
            funcSewaCustomer()      
        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)             
            funcSewaSearch()


    elif inputSewaSearch == '2':
        inputSearchJenis = input('''
-----------------------------
     CARI SESUAI JENIS
-----------------------------        
    
Masukkan Jenis Mobil yang Dicari : ''')

        print ('''
-----------------------------
     DAFTAR SELURUH MOBIL
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Jenis'].lower() == inputSearchJenis.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
        if konfirmasiLanjut == '1':
    
            pilihanMobil = input('''
Masukkan Nomor Plat mobil yang ingin Anda Sewa :    
''')
            for i in range(len(daftarAsetMobil)):
                if daftarAsetMobil[i]['Nomor Plat'] == pilihanMobil:
                    print ('''
-----------------------------
           KERANJANG
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                    keranjangSementara.append(daftarAsetMobil[i])
                    daftarMobilDisewa.append(daftarAsetMobil[i])
                    del daftarMobilTersedia[i]    

                    funcKonfirmasiPesananKeranjang()
        elif konfirmasiLanjut == '2':
            funcSewaCustomer()            
        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)             
            funcSewaSearch()


    elif inputSewaSearch == '3':
        inputSearchWarna = input('''
-----------------------------
     CARI SESUAI WARNA
-----------------------------        
    
Masukkan Warna Mobil yang Dicari : ''')

        print ('''
-----------------------------
     DAFTAR SELURUH MOBIL
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Warna'].lower() == inputSearchWarna.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
        if konfirmasiLanjut == '1':
    
            pilihanMobil = input('''
Masukkan Nomor Plat mobil yang ingin Anda Sewa :    
''')
            for i in range(len(daftarAsetMobil)):
                if daftarAsetMobil[i]['Nomor Plat'] == pilihanMobil:
                    print ('''
-----------------------------
           KERANJANG
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                    keranjangSementara.append(daftarAsetMobil[i])
                    daftarMobilDisewa.append(daftarAsetMobil[i])
                    del daftarMobilTersedia[i]    

                    funcKonfirmasiPesananKeranjang()
        elif konfirmasiLanjut == '2':
            funcSewaCustomer()            
        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)             
            funcSewaSearch()



    elif inputSewaSearch == '4':
        inputSearchKapasitas = int(input('''
-----------------------------
    CARI SESUAI KAPASITAS
-----------------------------        
    
Masukkan Kapasitas Mobil yang Dicari : '''))

        print ('''
-----------------------------
     DAFTAR SELURUH MOBIL
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Kapasitas'] == inputSearchKapasitas: 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
        if konfirmasiLanjut == '1':
    
            pilihanMobil = input('''
Masukkan Nomor Plat mobil yang ingin Anda Sewa :    
''')
            for i in range(len(daftarAsetMobil)):
                if daftarAsetMobil[i]['Nomor Plat'] == pilihanMobil:
                    print ('''
-----------------------------
           KERANJANG
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                    keranjangSementara.append(daftarAsetMobil[i])
                    daftarMobilDisewa.append(daftarAsetMobil[i])
                    del daftarMobilTersedia[i]    

                    funcKonfirmasiPesananKeranjang()
        elif konfirmasiLanjut == '2':
            funcSewaCustomer()    
        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)             
            funcSewaSearch()        

    elif inputSewaSearch == '9':
        funcSewaCustomer()
    elif inputSewaSearch == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)       
        funcSewaSearch()



# SECTION MENU SEWA CUSTOMER => TAMPILKAN SELURUH MOBIL => KERANJANG  =======================================================================================================================================================================
def funcKonfirmasiPesananKeranjang ():
    konfirmasiPesanan = (input('''
Apakah mobil yang Anda pesan sudah sesuai?

1. Ya
2. Tidak, saya berubah pikiran

Pilih menu: '''))

    if konfirmasiPesanan == '1':
        funcKonfirmasiDurasi()
    elif konfirmasiPesanan == '2':
        funcSewaCustomer()     
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)       
        funcKonfirmasiPesananKeranjang()



# SECTION MENU SEWA CUSTOMER => TAMPILKAN SELURUH MOBIL => DURASI  =======================================================================================================================================================================
def funcKonfirmasiDurasi():
    lamaWaktuSewa = int(input('''
Berapa durasi Anda menyewa mobil (hari): '''))

    if lamaWaktuSewa > 0:
        print('''




-----------------------------------------
                 RECEIPT
-----------------------------------------

Total biaya yang harus Anda bayarkan adalah:

Rp '''+str(lamaWaktuSewa*keranjangSementara[0]['Harga Sewa'])+'''

=========================================
TERIMA KASIH TELAH MEMPERCAYAKAN CAR-RENT
     SEBAGAI SOLUSI SEWA MOBIL ANDA
=========================================     





''')
        funcMenuCustomer()
        
    elif lamaWaktuSewa <= 0:
        print ('''
========>>>>>  !!!!!  <<<<<========
  HARAP MASUKKAN JUMLAH HARI SEWA 
========>>>>>  !!!!!  <<<<<========''')
        funcKonfirmasiDurasi()



# SECTION PILIHAN MENU CUSTOMER => PENGEMBALIAN =======================================================================================================================================================================
def funcPengembalian():
    print('''
-------------------------------
      PENGEMBALIAN MOBIL
-------------------------------        
    
-------------------------------
DAFTAR MOBIL YANG SEDANG DISEWA
-------------------------------
| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
    for i in range(len(daftarMobilDisewa)):
            singkatanTipe = ''
            singkatanMerek = ''
            if len(daftarMobilDisewa[i]['Tipe']) > 7:
                singkatanTipe = daftarMobilDisewa[i]['Tipe'][:7:]
                if len(daftarMobilDisewa[i]['Merek']) > 6:
                    singkatanMerek = daftarMobilDisewa[i]['Merek'][:7:]
                elif len(daftarMobilDisewa[i]['Merek']) <= 6:
                    singkatanMerek = daftarMobilDisewa[i]['Merek']
            elif len(daftarMobilDisewa[i]['Tipe']) <= 7:
                singkatanTipe = daftarMobilDisewa[i]['Tipe']
                if len(daftarMobilDisewa[i]['Merek']) > 6:
                    singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                elif len(daftarMobilDisewa[i]['Merek']) <= 6:
                    singkatanMerek = daftarMobilDisewa[i]['Merek']

            print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
            .format(daftarMobilDisewa[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarMobilDisewa[i]['Jenis'], daftarMobilDisewa[i]['Warna'], daftarMobilDisewa[i]['Kapasitas'], daftarMobilDisewa[i]['Harga Sewa']))

    konfirmasiLanjut = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
    if konfirmasiLanjut == '1':
    
        pilihanMobil = input('''
Masukkan Nomor Plat mobil yang akan dikembalikan :    
''')
        for i in range(len(daftarMobilDisewa)):
            if daftarMobilDisewa[i]['Nomor Plat'] == pilihanMobil:
                print ('''
-----------------------------
        PENGEMBALIAN
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(daftarMobilDisewa[i]['Nomor Plat'], daftarMobilDisewa[i]['Merek'], daftarMobilDisewa[i]['Tipe'], daftarMobilDisewa[i]['Jenis'], daftarMobilDisewa[i]['Warna'], daftarMobilDisewa[i]['Harga Sewa']))

        konfirmasiPengembalian = (input('''
Lanjutkan proses?

1. Ya
2. Tidak

Pilih menu: '''))
        if konfirmasiPengembalian == '1':
            print('''




-----------------------------------------
                CAR-RENT
-----------------------------------------

TERIMA KASIH TELAH MENGGUNAKAN JASA KAMI

=========================================
   Kritik & Saran silahkan menghubungi
          Customer Service Kami
=========================================     





''')
            
            daftarMobilTersedia.append(daftarMobilDisewa[i])
            del daftarMobilDisewa[i]

            funcMenuCustomer()

        elif konfirmasiPengembalian == '2':
            funcMenuCustomer()

        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcPengembalian()

    elif konfirmasiLanjut == '2':
        funcMenuCustomer()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcPengembalian()
    funcMenuCustomer()



# SECTION PILIHAN MENU ADMIN ========================================================================================================================================================================
def funcMenuAdmin():
    pilihanMenuAdmin = (input('''
----------------------
      MENU ADMIN
----------------------

1. Menambah Aset Mobil
2. View Aset Mobil
3. Update Aset Mobil
4. Delete Aset Mobil

0. Kembali ke Halaman Utama

Pilih menu: '''))
    if pilihanMenuAdmin == '1':
        funcCreate()
    elif pilihanMenuAdmin == '2':
        funcView()
    elif pilihanMenuAdmin == '3':
        funcUpdateAdmin()
    elif pilihanMenuAdmin == '4':
        funcDeleteAdmin()    
    elif pilihanMenuAdmin == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcMenuAdmin()



# SECTION PILIHAN MENU ADMIN => CREATE =======================================================================================================================================================================
def funcCreate():

    funcTampilkanSeluruhAsetMobil()

    inputNomorPlat = input('''
Masukkan Nomor Plat Mobil Baru: ''')
    for i in range(len(daftarAsetMobil)):
        if daftarAsetMobil[i]['Nomor Plat'] == inputNomorPlat:
            print ('''
========>>>>>  !!!!!  <<<<<========
   DITEMUKAN NOMOR PLAT YANG SAMA
   MOHON PASTIKAN NOMOR PLAT YANG 
        ANDA MASUKKAN SESUAI 
========>>>>>  !!!!!  <<<<<========''')            
            funcCreate()

    inputMerekMobil = input('''
Masukkan Merek Mobil Baru: ''')
    inputTipeMobil = input('''
Masukkan Tipe Mobil Baru: ''')
    inputJenisMobil = input('''
Masukkan Jenis Mobil Baru: ''')
    inputTahunMobil = int(input('''
Masukkan Tahun Mobil Baru: '''))
    inputWarnaMobil = input('''
Masukkan Warna Mobil Baru: ''')
    inputHargaMobil = int(input('''
Masukkan Harga Sewa Mobil Baru: '''))
    inputKapasitasMobil = int(input('''
Masukkan Kapasitas Mobil Baru: '''))
    print('''
-----------------------
DAFTAR YANG DITAMBAHKAN
-----------------------
| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
                .format(inputNomorPlat, inputMerekMobil, inputTipeMobil, inputJenisMobil, inputWarnaMobil, inputHargaMobil))

    konfirmasiBuatDaftarBaru = input('''
Apakah data daftar mobil baru yang Anda masukkan sudah benar? 

1. Ya
2. Tidak, saya akan ulangi

Pilih menu: ''')
    if konfirmasiBuatDaftarBaru == '1':
        daftarAsetMobil.append({
            'Nomor Plat' : inputNomorPlat,
            'Merek' : inputMerekMobil,
            'Tipe' : inputTipeMobil,
            'Harga Sewa' : inputHargaMobil,
            'Jenis' : inputJenisMobil,
            'Tahun' : inputTahunMobil,
            'Warna' : inputWarnaMobil,
            'Kapasitas' : inputKapasitasMobil
        })
        daftarMobilTersedia.append({
            'Nomor Plat' : inputNomorPlat,
            'Merek' : inputMerekMobil,
            'Tipe' : inputTipeMobil,
            'Harga Sewa' : inputHargaMobil,
            'Jenis' : inputJenisMobil,
            'Tahun' : inputTahunMobil,
            'Warna' : inputWarnaMobil,
            'Kapasitas' : inputKapasitasMobil
        })



        tambahItemDaftarBaru = input('''
Apakah ingin menambahkan data lagi? 

1. Ya
2. Tidak

Pilih menu: ''')
        if tambahItemDaftarBaru == '1':
            funcCreate()
        elif tambahItemDaftarBaru == '2':
            funcMenuAdmin()
        else:
             print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcCreate()   

    elif konfirmasiBuatDaftarBaru == '2':
        funcMenuAdmin()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcCreate()
    funcMenuAdmin()



# SECTION PILIHAN MENU ADMIN => VIEW =======================================================================================================================================================================
def funcView():
    menuViewAdmin = (input('''
----------------------
      MENU VIEW
----------------------
1. Lihat Daftar Mobil
2. Cari Mobil

9. Kembali ke Menu Admin
0. Kembali ke Halaman Utama

Pilih menu: '''))
    if menuViewAdmin == '1':
        funcViewDaftar()
    elif menuViewAdmin == '2':
        funcViewSearch()
    elif menuViewAdmin == '9':
        funcMenuAdmin()
    elif menuViewAdmin == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcView()



# SECTION PILIHAN MENU VIEW DAFTAR =======================================================================================================================================================================
def funcViewDaftar():
    menuViewDaftarMobil = (input('''
----------------------
  LIHAT DAFTAR MOBIL
----------------------
1. Daftar Seluruh Aset Mobil
2. Daftar Mobil yang Disewa
3. Daftar Mobil yang Tersedia

9. Kembali ke Menu View
0. Kembali ke Halaman Utama

Pilih menu: '''))

    if menuViewDaftarMobil == '1':
        funcTampilkanSeluruhAsetMobil()
        funcViewDaftar()
    
    elif menuViewDaftarMobil == '2':
        print ('''
-----------------------------
   DAFTAR MOBIL YANG DISEWA
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarMobilDisewa)):
            print('''| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
            .format(daftarMobilDisewa[i]['Nomor Plat'], daftarMobilDisewa[i]['Merek'], daftarMobilDisewa[i]['Tipe'], daftarMobilDisewa[i]['Jenis'], daftarMobilDisewa[i]['Warna'], daftarMobilDisewa[i]['Harga Sewa']))
        funcViewDaftar()

    elif menuViewDaftarMobil == '3':

        print ('''
-----------------------------
  DAFTAR MOBIL YANG TERSEDIA
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarMobilTersedia)):
            print('''| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
            .format(daftarMobilTersedia[i]['Nomor Plat'], daftarMobilTersedia[i]['Merek'], daftarMobilTersedia[i]['Tipe'], daftarMobilTersedia[i]['Jenis'], daftarMobilTersedia[i]['Warna'], daftarMobilTersedia[i]['Harga Sewa']))
        funcViewDaftar()

    elif menuViewDaftarMobil == '9':
        funcView()
    
    elif menuViewDaftarMobil == '0':
        funcMenuStart()

    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcViewDaftar()



# SECTION PILIHAN MENU VIEW SEARCH =======================================================================================================================================================================
def funcViewSearch():
    
    inputViewSearch = (input('''
-----------------------------
     CARI SESUAI KATEGORI
-----------------------------

1. Nomor Plat
2. Merek Mobil
3. Jenis Mobil
4. Warna Mobil
5. Kapasitas Mobil

9. Kembali ke Menu View
0. Kembali ke Halama Utama

Pilih menu: '''))

    if inputViewSearch == '1':
        inputSearchNomorPlat = input('''
-----------------------------
    CARI SESUAI NOMOR PLAT
-----------------------------        
    
Masukkan Nomor Plat Mobil yang Dicari : ''')

        print ('''
-----------------------------
 DAFTAR BERDASARKAN NO. PLAT
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'].lower() == inputSearchNomorPlat.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        funcViewSearch()

    elif inputViewSearch == '2':
        inputSearchMerek = input('''
-----------------------------
     CARI SESUAI MEREK
-----------------------------        
    
Masukkan Merek Mobil yang Dicari : ''')

        print ('''
-----------------------------
  DAFTAR BERDASARKAN MEREK
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Merek'].lower() == inputSearchMerek.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        funcViewSearch()

    elif inputViewSearch == '3':
        inputSearchJenis = input('''
-----------------------------
     CARI SESUAI JENIS
-----------------------------        
    
Masukkan Jenis Mobil yang Dicari : ''')

        print ('''
-----------------------------
  DAFTAR BERDASARKAN JENIS
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Jenis'].lower() == inputSearchJenis.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        funcViewSearch()

    elif inputViewSearch == '4':
        inputSearchWarna = input('''
-----------------------------
     CARI SESUAI WARNA
-----------------------------        
    
Masukkan Warna Mobil yang Dicari : ''')

        print ('''
-----------------------------
   DAFTAR BERDASARKAN WARNA
-----------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Warna'].lower() == inputSearchWarna.lower(): 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        funcViewSearch()

    elif inputViewSearch == '5':
        inputSearchKapasitas = int(input('''
-----------------------------
    CARI SESUAI KAPASITAS
-----------------------------        
    
Masukkan Kapasitas Mobil yang Dicari : '''))

        print ('''
------------------------------
 DAFTAR BERDASARKAN KAPASITAS
------------------------------

| Nomor Plat\t| Merek & Tipe  \t| Jenis \t| Warna \t| Kap.\t| Harga per hari
===============================================================================================''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Kapasitas'] == inputSearchKapasitas: 
                singkatanTipe = ''
                singkatanMerek = ''
                if len(daftarAsetMobil[i]['Tipe']) > 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe'][:7:]
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']
                elif len(daftarAsetMobil[i]['Tipe']) <= 7:
                    singkatanTipe = daftarAsetMobil[i]['Tipe']
                    if len(daftarAsetMobil[i]['Merek']) > 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek'][:7:]
                    elif len(daftarAsetMobil[i]['Merek']) <= 6:
                        singkatanMerek = daftarAsetMobil[i]['Merek']

                print('''| {}\t| {} {}     \t| {}   \t| {}   \t| {}\t| {}'''
                .format(daftarAsetMobil[i]['Nomor Plat'], singkatanMerek, singkatanTipe, daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Kapasitas'], daftarAsetMobil[i]['Harga Sewa']))

        funcViewSearch() 

    elif inputViewSearch == '9':
        funcView()
    elif inputViewSearch == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)       
        funcViewSearch()


            
# SECTION PILIHAN MENU ADMIN => UPDATE =======================================================================================================================================================================
def funcUpdateAdmin():
    menuUpdateAdmin = (input('''
----------------------
      MENU UPDATE
----------------------
1. Update Nomor Plat
2. Update Warna Mobil
3. Update Harga Sewa

9. Kembali ke Menu Admin
0. Kembali ke Halaman Utama

Pilih menu: '''))
    if menuUpdateAdmin == '1':
        funcTampilkanSeluruhAsetMobil()

        inputUpdatePlat = input('''
Masukkan Nomor Plat Mobil yang ingin Diupdate : 
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                print ('''
-----------------------------
DATA MOBIL YANG AKAN DIUPDATE
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
        .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
        inputNomorPlatBaru = input('''
Masukkan Nomor Plat baru:        
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                daftarAsetMobil[i]['Nomor Plat'] = inputNomorPlatBaru
                daftarMobilTersedia[i]['Nomor Plat'] = inputNomorPlatBaru
           
        funcShowUpdate()

    elif menuUpdateAdmin == '2':
        funcTampilkanSeluruhAsetMobil()

        inputUpdatePlat = input('''
Masukkan Nomor Plat Mobil yang ingin Diupdate : 
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                print ('''
-----------------------------
DATA MOBIL YANG AKAN DIUPDATE
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
        .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
        inputWarnaBaru = input('''
Masukkan perubahan Warna Mobil:        
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                daftarAsetMobil[i]['Warna'] = inputWarnaBaru
                daftarMobilTersedia[i]['Warna'] = inputWarnaBaru
           
        funcShowUpdate()

    elif menuUpdateAdmin == '3':
        funcTampilkanSeluruhAsetMobil()

        inputUpdatePlat = input('''
Masukkan Nomor Plat Mobil yang ingin Diupdate : 
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                print ('''
-----------------------------
DATA MOBIL YANG AKAN DIUPDATE
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
        .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))

                    
        inputHargaBaru = input('''
Masukkan perubahan Harga Sewa:        
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputUpdatePlat:
                daftarAsetMobil[i]['Harga Sewa'] = inputHargaBaru
                daftarMobilTersedia[i]['Harga Sewa'] = inputHargaBaru
           
        funcShowUpdate()    

    elif menuUpdateAdmin == '9':
        funcMenuAdmin()
    elif menuUpdateAdmin == '0':
        funcMenuStart()

    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcUpdateAdmin()



# SECTION PILIHAN MENU ADMIN => UPDATE =======================================================================================================================================================================
def funcShowUpdate():
    konfirmasiTampilkanUpdate = (input('''
Tampilkan update?

1. Ya
2. Tidak

Pilih menu: '''))
    if konfirmasiTampilkanUpdate == '1':
        funcTampilkanSeluruhAsetMobil()

        funcUpdateAdmin()

    elif konfirmasiTampilkanUpdate == '2':
        funcUpdateAdmin()

    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcShowUpdate()



# SECTION PILIHAN MENU ADMIN => DELETE =======================================================================================================================================================================
def funcDeleteAdmin():
    inputDeleteAdmin = (input('''
----------------------
      MENU DELETE
----------------------
1. Hapus Daftar Mobil

9. Kembali ke Menu Admin
0. Kembali ke Halaman Utama

Pilih menu: '''))
    if inputDeleteAdmin == '1':
        funcTampilkanSeluruhAsetMobil()

        inputHapusPlat = input('''
Masukkan Nomor Plat Mobil yang ingin Dihapus : 
''')
        for i in range(len(daftarAsetMobil)):
            if daftarAsetMobil[i]['Nomor Plat'] == inputHapusPlat:
                print ('''
-----------------------------
 DATA MOBIL YANG AKAN DIHAPUS
-----------------------------

| Nomor Plat\t| Merek \t| Tipe    \t| Jenis \t| Warna   \t| Harga per hari
===============================================================================================
| {}\t| {} \t| {}    \t| {}   \t| {}   \t| {}'''
        .format(daftarAsetMobil[i]['Nomor Plat'], daftarAsetMobil[i]['Merek'], daftarAsetMobil[i]['Tipe'], daftarAsetMobil[i]['Jenis'], daftarAsetMobil[i]['Warna'], daftarAsetMobil[i]['Harga Sewa']))
            
                konfirmasiHapus = (input('''
Anda yakin untuk menghapus data tersebut?

1. Ya
2. Tidak, saya berubah pikiran

Pilih menu: '''))
                if konfirmasiHapus == '1':
                    del daftarAsetMobil[i]
                    del daftarMobilTersedia[i]

                    funcTampilkanSeluruhAsetMobil()
                    
                    funcDeleteAdmin()

                elif konfirmasiHapus == '2':
                    funcDeleteAdmin()

                else:
                    print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
                    funcDeleteAdmin()

    elif inputDeleteAdmin == '9':
        funcMenuAdmin()
    elif inputDeleteAdmin == '0':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcDeleteAdmin()



# SECTION VERIFIKASI ADMIN =======================================================================================================================================================================
def funcVerifikasiAdmin():
    passwordAdmin = input('''
----------------------
   VERIFIKASI ADMIN
----------------------

Masukkan password jika akan masuk sebagai Admin.
(hint! : admin123)

Masukkan disini : ''')
    if passwordAdmin == "admin123":
        funcMenuAdmin()
    elif passwordAdmin != "admin123":
        print ('''
=======>>>>>  !!!!!  <<<<<=======
PASSWORD YANG ANDA MASUKKAN SALAH 
=======>>>>>  !!!!!  <<<<<======='''
)
        funcKonfirmasiLanjut()



# SECTION KONFIRMASI MELANJUTKAN ADMIN =======================================================================================================================================================================
def funcKonfirmasiLanjut():
    inputMelanjutkanIdentifikasi = (input('''
Apakah Anda yakin untuk melanjutkan sebagai admin?

1. Ya
2. Tidak

Pilih menu: '''))
    if inputMelanjutkanIdentifikasi == '1':
        funcVerifikasiAdmin()
    elif inputMelanjutkanIdentifikasi == '2':
        funcMenuStart()
    else:
        print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)       
        funcKonfirmasiLanjut()



# SECTION START AWAL SEKALI =======================================================================================================================================================================
def funcMenuStart():
    while True:
        menuIdentifikasi = (input('''
============================== *** WELCOME TO CAR-RENT *** ==============================
                    ----------  Solusi Sewa Menyewa Mobil  ----------

----------------------
IDENTIFIKASI DIRI ANDA
----------------------
        
1. CUSTOMER
2. ADMIN
        
Pilih menu: '''))
        if menuIdentifikasi == '1':
            funcMenuCustomer()
        elif menuIdentifikasi == '2':
            funcKonfirmasiLanjut()
        else:
            print ('''
========>>>>>  !!!!!  <<<<<========
HARAP MEMASUKKAN MENU YANG TERSEDIA 
========>>>>>  !!!!!  <<<<<========'''
)
        funcMenuStart()
funcMenuStart()
