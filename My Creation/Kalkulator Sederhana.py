while (True):
    print()
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("++         Kalkulator Sederhana        ++")
    print("++     By : Abdullah Qaid Mu'aadz      ++")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print() 

    print("1. Perkalian")
    print("2. Pembagian")
    print("3. Pertambahan")
    print("4. Perkurangan")
    print()

    ch=int(input("Masukan Pilihan (1-4) : "))


    if ch==1:
        print()
        a=int(input("Masukan angka pertama : "))
        b=int(input("Masukan angka kedua : "))
        c=a*b
        print()
        print("Hasil dari perkalian", a, "dan", b, "adalah : ", c)
        print()

    elif ch==2:
        print()
        a=int(input("Masukan angka pertama : "))
        b=int(input("Masukan angka kedua : "))
        c=a/b
        print()
        print("Hasil dari pembagian", a, "dan", b, "adalah : ", c)
        print()

    elif ch==3:
        print()
        a=int(input("Masukan angka pertama : "))
        b=int(input("Masukan angka kedua : "))
        c=a+b
        print()
        print("Hasil dari pertambahan", a, "dan", b, "adalah : ", c)
        print()

    elif ch==4:
        print()
        a=int(input("Masukan angka pertama : "))
        b=int(input("Masukan angka kedua : "))
        c=a-b
        print()
        print("Hasil dari perkurangan", a, "dan", b, "adalah : ", c)
        print()

    else:
        print("Maaf tidak ada pilihan seperti itu di atas :( ")

    status = input("Apakah masih ada inputan? (y = Ya, n = Tidak)? ")
    if status == "y":
        print()
        print("Silahkan masukan input data lagi")

    elif status == "n":
        break

    else:
        print("Maaf inputan tidak dikenal \n")
        break