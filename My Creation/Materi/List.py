# List mirip dengan Array

# Kita punya list nama-nama buah
buah = ["Apel", "Anggur", "Mangga", "Jeruk"]
#          0        1         2         3   = adalah nama indeks
# Misal kita ingin mengambil mangga
# Maka indeks nya adalah
print(buah[2])


# Mengganti item dari list
buah = ["Apel", "Anggur", "Mangga", "Jeruk"]
#          0        1         2         3   = adalah nama indeks
# Mengganti Indeks 2(Mangga) menjadi >> "Kelapa"
buah[2] = "Kelapa"
print(buah)


# Mengganti item dari list
buah = ["Apel", "Anggur", "Mangga", "Jeruk"]
#          0        1         2         3   = adalah nama indeks
# menambahkan Manggis
buah.append("Manggis")
print(buah)


# Menambah item List menggunakan Insert() 
buah = ["Jeruk", "Apel", "Mangga", "Duren"]
#          0        1        2         3   = adalah nama indeks
# Menambah nilai indeks ke-2 dengan nama item "Manggis"
buah.insert(2, "Manggis")
print(buah)


# Menghapus item di List
# Membuat list
todo_list = [
    "Belajar Python",           # 0
    "Belajar HTML",             # 1
    "Belajar Java Script",      # 2
    "Belajar Sulap",            # 3
    "Belajar PHP",              # 4
]                              
            # Adalah nama indeks /\
# Misalkan kita ingin menghapus "Belajar Sulap" yang berada di indeks ke-3
del todo_list[3]
print(todo_list)


# Menghapusitem di List menggunakan remove()
vokal = ["a", "i", "e", "o"]
# Kemudian kita hapus i
vokal.remove("i")
print(vokal)


# Memotong item pada List
warna = ["Merah", "Hijau", "Kuning", "Biru", "Pink", "Ungu"]
# #         0        1        2         3       4       5   = adalah nama indeks
# Kita potong dari indeks ke-1 dan ke-5
print(warna[1:5])


# 
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es kopi", "ES Campur", "Es Teler"]
]
# Cara mengakses list Mulitidimensi
# misalkan ingin mengambil "es kopi"
print(list_minuman[1][2])