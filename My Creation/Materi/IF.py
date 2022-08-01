# One-Why if Statement

# Membuat variabel angka1
angka1 = int(input("Masukan Bilangan : "))

# Jika angka1 lebih dari 5 makan akan true
if angka1 > 5 :
    # Jika true makan akan mencetak "Bener"
    print("Benar")



# Two-Way if Statement

# Membuar variabel
sepeda_saya = 5

# Jika sepeda saya kurang dri 2
if sepeda_saya <= 2:
    # print cukup
    print("Sepeda saya cukup")

# Selain itu
else:
    # print lebih
    print("Sepeda saya lebih")

# Keterangan kelulusan Mahasantr/i



# Membuat variabel namaSaya
print()
print("Keterangan Kelulusan Mahasasantri PeTIK II Jombang")
print()

namaSaya = input("Masukan nama lengkap : ")

# Membuat variabel jumlahSetoran
jumlahSetoran = int(input("Masukan Jumlah Setoran : "))

if jumlahSetoran < 2:
    print()
    print("Nama : ", namaSaya)
    print("Jumlah Hafalan : ", jumlahSetoran)
    print("Keterangan Kelulusan : Tidak lulus")
    print()
else:
    print()
    print("Nama : ", namaSaya)
    print("Jumlah Hafalan : ", jumlahSetoran)
    print("Keterangan Kelulusan : lulus")
print()



# Multi-Way if Statement

nilaiUjian = int(input("Nilai ujian saya "))

if nilaiUjian < 30:
    print("Peringkat D")

elif nilaiUjian < 60:
    print("Peringkat C")

elif nilaiUjian < 80:
    print("Peringkat B")

else:
    print("Peringkat A")




print("--------------------------------------------")
print("-- GRADE NILAI MAHASANTRI PETIK 2 JOMBANG --")
print("--------------------------------------------")

namaSaya = input("Nama Lengkap : ")
nilaiSaya = float(input("Nilai Kamu : "))

print("Nama : ", namaSaya)

if nilaiSaya < 30.0:
    print("GRADE : D")

elif nilaiSaya < 60.0:
    print("GRADE : C")

elif nilaiSaya < 80.0:
    print("GRADE : B")

elif nilaiSaya > 100:
    print("ERROR")

else:
    print("GRADE : A")



print("--------------------------------------------")
print("-- GRADE NILAI MAHASANTRI PETIK 2 JOMBANG --")
print("--------------------------------------------")


while (True) :
    namaSaya = input("Nama Lengkap : ")
    nilaiSaya = float(input("Nilai Kamu : "))
    gradeSaya = ""

    if nilaiSaya < 30.0:
        gradeSaya = "D"

    elif nilaiSaya < 60.0:
        gradeSaya = "C"

    elif nilaiSaya < 80.0:
        gradeSaya = "B"

    else:
        gradeSaya = "A"

    print()
    print("Nama : ", namaSaya)
    print("Nilai : ", nilaiSaya)
    print("Grade : ", gradeSaya)
    print()

    status = input("Apakah masih ada yang ingin di input? (y = Ya, n = Tidak)? ")
    if status == "n":
        break
    elif status == "y":
        print()
        print("Silahkan masukan input data lagi")
    else :
        print("Inputan tidak dikenali \n")
        break


# TUGAS KELOMPOK
# SILAHKAN BUAT SATU APLIKASI SEDERHANA (CTH. KALKULATOR, DLL)
# HARUS ADA = IF ELSE, WHILE/FOR, INPUT/OUTPUT
# TULIS KOMENTAR DISETIAP BLOK/STATEMENT APLIKASI
# PRESENTASIKAN KODINGAN
# DEMO-KAN APLIKASI TERSEBUT