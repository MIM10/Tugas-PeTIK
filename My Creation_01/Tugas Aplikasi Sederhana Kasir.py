# Membuat perulangan while
while (True):
    # Mencetak Toko saya
    print()
    print("=" * 38)
    print("++       Warung Makan Padang        ++")
    print("=" * 38)
    print()


    # Mencetak menu
    print()
    print("=" * 39)
    print("              Menu Makanan            ")
    print("=" * 39)
    print("[1] Perkedel               -> Rp. 4.000")
    print("[2] Gurami                 -> Rp. 9.000")
    print("[3] Ayam Goreng            -> Rp. 7.000")
    print("[4] Rendang                -> Rp. 8.000")
    print("[5] Pecel Lele             -> Rp. 9.000")
    
    print()
    print("=" * 39)
    print("          Menu Minuman Dingin         ")
    print("=" * 39)
    print("[6] Es Teh                 -> Rp. 6.000")
    print("[7] Es Leci                -> Rp. 10.000")
    print("[8] Es Dawet               -> Rp. 10.000")
    print("[9] Es Cincau              -> Rp. 8.000")
    print("[10] Es Jeruk              -> Rp. 8.000")

    print()
    print("=" * 39)
    print("          Menu Minuman Panas          ")
    print("=" * 39)
    print("[11] Teh Hangat            -> Rp. 6.000")
    print("[12] Tora Bika Cappucino   -> Rp. 8.000")
    print("[13] Wedang Jahe           -> Rp. 8.000")
    print("[14] Kopi Hitam            -> Rp. 6.000")
    print("[15] Good Day Cappucino    -> Rp. 8.000")


    print()

    print()
    # Membuat opsi inputan Pilih menu
    opsiMakan = input("Pilih Menu Makanan    : ")

    # Membuat opsi pertama
    if opsiMakan == "1":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 4000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi kedua
    elif opsiMakan == "2":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 9000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi ketiga
    elif opsiMakan == "3":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 7000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi keempat
    elif opsiMakan == "4":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 8000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi kelima
    elif opsiMakan == "5":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 9000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Mencetak Maaf tidak ada pilihan ini, dan menghentikan program dengan break
    else:
        print("Maaf tidak ada pilhan ini ")
        break


    opsiMinum1 = input("Pilih Menu Minuman    : ")
    # Membuat opsi minuman dingin pertama
    if opsiMinum1 == "6":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 6000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin Kedua
    elif opsiMinum1 == "7":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 15000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin ketiga
    elif opsiMinum1 == "8":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 7000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin keempat
    elif opsiMinum1 == "9":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 8000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin kelima
    elif opsiMinum1 == "10":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 13000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Mencetak Maaf tidak ada pilihan ini, dan menghentikan program dengan break
    else:
        print("Maaf tidak ada pilhan ini ")
        break


        # Membuat opsi minuman dingin pertama
    if opsiMinum1 == "11":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 4000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin Kedua
    elif opsiMinum1 == "12":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 15000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin ketiga
    elif opsiMinum1 == "13":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 7000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin keempat
    elif opsiMinum1 == "14":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 8000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi minuman dingin kelima
    elif opsiMinum1 == "15":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 13000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Mencetak Maaf tidak ada pilihan ini, dan menghentikan program dengan break
    else:
        print("Maaf tidak ada pilhan ini ")
        break



    print()
    # Membuat variabel status inputan "apakah masih akan melanjutkan program atau tidak"
    status = input("Apakah masih ada inputan? (y = Ya, n = Tidak)? ")
    # jika y maka program akan berlanjut
    if status == "y":
        print()
        print("Silahkan masukan input data lagi")

    # Jika n maka program akan berhenti dengan break
    elif status == "n":
        break

    # Jika memasukan komentar salah maka program akan berhenti dengan break
    else:
        print("Maaf inputan tidak dikenal \n")
        break 