# membuat array siswa
siswa = []

# membuat perulangan array
for i in range(2):

    # mengecek nilai indeks
    print("")
    print("ini adalah indeks ke-", i)

    # menerima inputan nama
    nama_siswa = input("Masukan nama Siswa : ")

    # menerima inputan daerah
    nama_daerah = input("Masukan nama daerah : ")

    # memasukan hasil inputan nama ke array siswa
    siswa.append(nama_siswa)

print("")

# membuat perulangan untuk mencetak data dari array siswa
for k in siswa:

    # mencetak array siswa
    print("Nama Siswa : ", k)