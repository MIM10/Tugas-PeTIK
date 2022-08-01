# def salam(nama):
#     print("Hello....")
#     # print("Selemat datang..", nama)
#     print("Apa kabar?", nama)

# salam("Abdullah Qa'id Mu'aadz")
# print()
# salam("Miski Khitami Mubarok")
# print()
# salam("Muhammad Dzaky Dzaky")


# def luas_persegi_panjang(panjang, lebar):
#     print("menghitung luas persegi panjang")
#     rumus = panjang * lebar
#     print("Panjang : ", panjang)
#     print("Lebar : ", lebar)

# luas_persegi_panjang(10, 23)



# def luas_persegi_panjang(panjang, lebar):
#     print("menghitung luas persegi panjang")
#     rumus = panjang * lebar
#     return rumus

# # print(luas_persegi_panjang(8, 6))
# luas_persegi_panjang(8, 6)


# def func1(): # Fungsi void
#     x = 100
#     print(x)

# def func2(): # Fungsi normal
#     x = 1000
#     return x

# void = func1()
# normal = func2()

# print("Fungsi Void Nilainya : ", void)
# print("Fungsi Normal Nilainya : ", normal)


# def tambah(a, b, c):
#     hasil = a + b + c
#     hasil1 = a - b / c
#     return hasil, hasil1

# x, y = tambah(5, 7, 9)
# print(x)
# print(y)


# # angka1, angka2 = parameter biasa
# # angka3 = parameter default
# def tes(angka1, angka2, angka3):
#     print(angka1)
#     print(angka2)
#     print(angka3)

# tes(9, 2, 5)


def persegi():
    sisi = int(input("Masukan Sisi : "))
    rumus = sisi * sisi
    print("Hasil : ", rumus)
    return rumus

persegi()


def lingkaran():
    jari = int(input("Masukan Jari-jari : "))
    rumus = 3.14 * jari * jari
    print("Hasil : ", rumus)
    return rumus
lingkaran()

# def salam(nama):
#     print("assalamualaikum ", nama)


# def parameter_keyword(teks1, teks2, teks3):
#     parameter_keyword(teks2,teks1, teks3)