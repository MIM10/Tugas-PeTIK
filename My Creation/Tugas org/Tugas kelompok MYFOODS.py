# Membuatkan Varibael Untuk memilih makanan 
total = 0 
barang = []
harga = []

# Menampilkan Tampilan Selamat datang
print('='*25)
print("SELAMAT DATANG\nDI MYFOODS")
print('='*25,'\n')

# Menampilkan Daftar Menu
while True:
    print("=====Daftar menu=====\n""Makanan\n1. Nasi Goreng Rp. 10.000,00", "\n2. Nasi Mawut Rp. 7.000,00", "\n3. Nasi Kuning Rp. 5.000,00","\n4. Mie Goreng Rp. 10.000,00","\n5. Bakso Rp. 6000,00","\n6. Mie Ayam Rp. 8000,00\n"
    "\nMimunan","\n7. Teh Hangat Rp 3.000,00""\n8. Jeruk Hangat Rp. 4000,00""\n9. Es Teh Rp. 4000,00""\n10. Es jeruk Rp. 5000,00")

# Memasukan Inputan untuk memilih dan menentukan jumlah menu yang dipesan
    kode = int(input("\nMasukan kode makanan/minuman : "))
    jumlah = int(input("Jumlah yang dipesan          : "))
    if kode == 1:
        barang.append('Nasi Goreng')
        harga.append(10000)
        total += jumlah * 10000
    elif kode == 2:
        barang.append('Nasi Mawut')
        harga.append(7000)
        total += jumlah * 7000
    elif kode == 3:
        barang.append('Nasi kuning')
        harga.append(5000)
        total += jumlah * 5000
    elif kode == 4:
        barang.append('Mie Goreng')
        harga.append(10000)
        total += jumlah * 10000
    elif kode == 5:
        barang.append('Bakso')
        harga.append(6000)
        total += jumlah * 6000
    elif kode == 6:
        barang.append('Mie Ayam')
        harga.append(8000)
        total += jumlah * 8000
    elif kode == 7:
        barang.append('Teh Hangat')
        harga.append(3000)
        total += jumlah * 3000
    elif kode == 8:
        barang.append('Jeruk Hangat')
        harga.append(4000)
        total += jumlah * 4000
    elif kode == 9:
        barang.append('Es Teh')
        harga.append(4000)
        total += jumlah * 4000
    elif kode == 10:
        barang.append('Es Jeruk')
        harga.append(5000)
        total += jumlah * 5000
    else:
        print('kode tidak valid')

# Mengeluarkan outputan untuk pilihan lanjut atau tidak
    lanjut = input('\nlanjut belanja (y/t)         : ')
    if lanjut == 'y':
        print("")
    else :
        break

# Menampilkan Total Pesanan
print('\nbarang yang dibeli       :',barang)
print('harga barang             :',harga)
print('total yang harus dibayar : Rp.',total,'\n')
print("-"*50)

#MengInput Nama dan alamat penerima
nama = input("\nMasukan Nama Penerima    : ")
alamat = input("Masukan alamat penerima  : ")

# Mengeluarkan Output metode pembayaran
print("\nPilih metode pembayaran : ","\n1. MYFOODS PAY","\n2. Tunai","\n3. Dana","\n4. Ovo")
metode = int(input("Pilih metode pembayaran dengan memasukan kode pembayaran : "))

# Pembeli menginputkan/memilih pilihan pembayaran dan lanjut ke pembayaran, dan menampilkan struk pembayaran
if metode == 1:
    user = input("\nMasukan Username MYFOODS anda  : ")
    nmr = int(input("Masukan nomor MYFOODS PAY anda : "))
    print("\n-----Pembayaran via MYFOODS PAY----- \nDengan Total Pembayaran  : Rp. ", total, "\nAtas Nama               : ",user , "\nPembayaran dengan nomor : ", nmr, "\nNama Penerima           : ", nama, "\nAlamat penerima         : ",alamat)
elif metode == 2:
    print("\n-----Pembayaran Tunai----- \nNama Penerima   : ", nama ,"\nAlamat penerima : ", "\nDengan Total Pembayaran : Rp. ", total, alamat,"\nHarap menggunakan uang pas !!!")
elif metode == 3:
    userDana = input("\nMasukan Username Dana anda : ")
    noDana = input("Masukan Nomor Dana anda    : ")
    print("\n-----Pembayaran via Dana------ \nDengan Total Pembayaran :  Rp.", total, "\nAtas Nama               : ", userDana, "\nPembayaran dengan nomor : ", noDana, "\nNama Penerima           : ", nama ,"\nAlamat penerima         : ",alamat)
elif metode == 4:
    userOvo = input("\nMasukan Username Ovo anda : ")
    noOvo= input("Masukan Nomor Ovo anda    : ")
    print("\n-----Pembayaran via Ovo------ \nDengan Total Pembayaran :  Rp. ", total, "\nAtas Nama               : ", userOvo, "\nPembayaran dengan nomor : ", noOvo, "\nNama Penerima           : ", nama , "\nAlamat penerima         : ",alamat)
else:
    print('menu tidak tersedia')

# Menampilkan output terima kasih telah memesan makanan
print()
print('='*45)
print(" Terima Kasih telah pesan makanan di MYFOODS")
print("      Pesanan anda akan segera diantar")
print('='*45)