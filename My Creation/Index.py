# # Menerima inputan
# angka1 = int(input("Masukan angka Pertama : "))
# angka2 = int(5)

# # Proses Penjumlahan
# hasil = angka1 + angka2

# # Proses Output
# print(hasil)
# hasil2 = (4 + hasil)
# print(float(hasil2))
# print(int(hasil2))


# # sep/pemisah
# print('A', 1, 'XYZ', 2, sep='#')


# print('ini pesan pertama', end=' - ')
# print("ini pesan kedua")


# # for
# angka = 1
# for i in range(10):
#     print(angka)


# angka = 5
# for i in range(10):
#     print('no:', i, 'berisi', angka)


# # Membuat array mobil
# index 0 = Honda Jazz
# index 1 = Avanza
# index 2 = Kijang

# mobil = ['Honda Jazz', 'Avanza', 'Kijang']
# # print(mobil[1])
# # print(mobil)

# for i in range(3):
#     print(mobil[i])

# # Membuat array buah buahan
# buah = ['mangga', 'apel', 'anggur', 'jeruk', 'pisang', 'nanas', 'ceri']

# # melakukan perulangan for
# for buah_buahan in buah:
#     # mencetak buah buahan
#     print("nama buah : ", buah_buahan)
# print(buah[3])


# nomor = []
# for n in nomor:
#     print(n)


# for m in range(4, 10, 2):
#     print(m)



# buah[2] = 'stowberry'
# print(buah [2])

# # print manual
# print("nama buah : ", buah[0])
# print("nama buah : ", buah[1])
# print("nama buah : ", buah[2])
# print("nama buah : ", buah[3])
# print("nama buah : ", buah[4])
# print("nama buah : ", buah[5])
# print("nama buah : ", buah[6])


# # Membuat program biodata

# # Membuat variabel nama_saya yang menerima inputan
# nama_lengkap = input("Masukan Nama Lengkap : ")

# # Membuat variabel asal_daerah yang menerima inputan
# asal_daerah = input("Masukan Asal Daerah : ")

# # Membuat Array biodata untuk mengumpulkan hasil inputan
# biodata = [ nama_lengkap, asal_daerah ]

# no = 0
# for isi_biodata in biodata :
#     print(biodata[no])
#     no = no + 1



# while (1 + 2 == 3):
#     print('halo dunia')
#     print('halo dunia2')




# # Perulangan For menggunakan bentuk perulangan While
# i = 0

# while i <= 5:
#     print(i)
#     i = i + 1



# # Perulangan While untuk list
# listKota = [
#     'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#     'Jogjakarta', 'Semarang', 'Makassar'
# ]

# # Bermain indeks
# i = 0
# while i < len(listKota):
#     print(listKota[i])
#     i += 1



# # Perulangan While untuk list
# a = int(input('Masukan bilangan ganjil lebih dari 25 : '))

# while a % 2 != 1 or a <= 25:
#     a = int(input('Salah, masukan lagi : '))

# print('Benar')
























# Membuat perulangan while
while (True):
    # Membuat variabel harga
    harga01 = 4000
    harga02 = 9000
    harga03 = 7000
    harga04 = 8000
    harga05 = 9000

    harga06 = 6000
    harga07 = 9000
    harga08 = 9000
    harga09 = 8000
    harga10 = 8000

    harga11 = 6000
    harga12 = 8000
    harga13 = 8000
    harga14 = 6000
    harga15 = 8000

    # Mencetak Toko saya
    print()
    print("=" * 38)
    print("++       Warung Makan Padang        ++")
    print("=" * 38)
    print()


    # Mencetak menu
    print()
    print("=" * 39)
    print("              Menu Makanan            ", "\t" )
    print("=" * 39)
    menu01 = print("[1] Perkedel               -> Rp.", harga01)
    menu02 = print("[2] Gurami                 -> Rp.", harga02)
    menu03 = print("[3] Ayam Goreng            -> Rp.", harga03)
    menu04 = print("[4] Rendang                -> Rp.", harga04)
    menu05 = print("[5] Pecel Lele             -> Rp.", harga05)
    
    print()
    print("=" * 39)
    print("          Menu Minuman Dingin         ")
    print("=" * 39)
    menu06 = print("[6] Es Teh                 -> Rp.", harga06)
    menu07 = print("[7] Es Leci                -> Rp.", harga07)
    menu08 = print("[8] Es Dawet               -> Rp.", harga08)
    menu09 = print("[9] Es Cincau              -> Rp.", harga09)
    menu10 = print("[10] Es Jeruk              -> Rp.", harga10)

    print()
    print("=" * 39)
    print("          Menu Minuman Panas          ")
    print("=" * 39)
    menu11 = print("[11] Teh Hangat            -> Rp.", harga11)
    menu12 = print("[12] Tora Bika Cappucino   -> Rp.", harga12)
    menu13 = print("[13] Wedang Jahe           -> Rp.", harga13)
    menu14 = print("[14] Kopi Hitam            -> Rp.", harga14)
    menu15 = print("[15] Good Day Cappucino    -> Rp.", harga15)
    print()
    print()

    # Membuat opsi inputan Pilih menu, jumlah pesanan
    menuMakan = input("Pilih Menu    : ")
    jumlahMakan = int(input("Jumlah Pesanan : "))
    bayar1 = menuMakan * jumlahMakan
    menuMinum = input("Pilih Menu    : ")
    jumlahMinum = int(input("Jumlah Pesanan : "))
    bayar2 = menuMinum * jumlahMinum

    bayar3 = bayar1 + bayar2

    menuMakan == menu01
    