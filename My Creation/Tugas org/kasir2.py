# membuat variabel menu dengan dictionary

menu = {
    "mie ayam"      : 15000,
    "mie ayam baso" : 25000,
    "baso"          : 10000,
    "jasmine tea"   :  5000,
    "coca-cola"     :  5000,
}

print("="*30, " daftar menu ","="*30)

# menampilkan menu dengan looping for
while True:
    for i in menu:
        print("daftar menu : ", i, "\t  harga \t: ", menu[i])
    print("pembelian diatas 100k mendapatkan diskonn 25%")
    print("pembelian diatas 50k mendapatkan diskonn 15%")
    print("="*50)

# proses input pembeli 

    print("makanan")
    makanan = input("Pilih Menu : ")
    jumlah1 = int(input("Jumlah Pesanan : "))
    bayar1 = jumlah1 * menu[makanan]
    print()
    print("minuman")
    minuman = input("Pilih Menu : ")
    jumlah2 = int(input("Jumlah Pesanan : "))
    bayar2 = jumlah2 * menu[minuman]

    bayar3 = bayar1+bayar2
    # proses diskon
    if bayar3 > 100000:
        diskon = bayar3*25//100
        total = bayar3 - diskon

    elif bayar3 >50000: 
        diskon = bayar3 * 15//100
        total = bayar3 - diskon
    else:
        total = bayar3



    print("="*25,"detail pembayaran","="*25)
    print("menu yang di pesan       : ", makanan,"dan", minuman)
    print("jumlah pesanan           : ", jumlah1 + jumlah2)
    print("total biaya              : ", bayar3)
    print("total yang harus dibayar : ", total, "\n")
    print("="*30,"Terima Kasih","="*30)
    print()

    status = input("lanjut memesan : ")
    if status == "n":
        break
    elif status == "y":
        print("silahkan pesan kembali")
    else :
        break
4.000
9.000
7.000
8.000
9.000
6.000
9.000
9.000
8.000
8.000
6.000
8.000
8.000
6.000
8.000