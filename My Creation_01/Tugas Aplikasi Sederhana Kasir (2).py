# Membuat perulangan while
while (True):
    # Mencetak Toko saya
    print()
    print("+++++++++++++++++++++++++")
    print("++ Warung Makan Padang ++")
    print("+++++++++++++++++++++++++")
    print()

    # Mencetak Pilih menu
    print("Pilih Menu : ")

    # Mencetak menu
    print("1. Perkedel      -> Rp. 4000")
    print("2. Gurami        -> Rp. 15000")
    print("3. Ayam Goreng   -> Rp. 7000")
    print("4. Rendang       -> Rp. 8000")

    print()
    # Membuat opsi inputan Pilih menu
    opsi = input("Pilih Menu     : ")

    # Membuat opsi pertama
    if opsi == "1":
        jumlah = int(input("Jumlah         : "))
        uangKamu = int(input("Uang Kamu      : "))
        harga = 4000
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
    elif opsi == "2":
        jumlah = int(input("Jumlah         : "))
        uangKamu = int(input("Uang Kamu      : "))
        harga = 15000
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
    elif opsi == "3":
        jumlah = int(input("Jumlah         : "))
        uangKamu = int(input("Uang Kamu      : "))
        harga = 7000
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
    elif opsi == "4":
        jumlah = int(input("Jumlah         : "))
        uangKamu = int(input("Uang Kamu      : "))
        harga = 8000
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