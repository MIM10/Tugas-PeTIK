# import random
# def input_data():
#     valid = True
#     while valid:
#         print("===================================")
#         print("Selamat Datang Pada Program Biodata")
#         print("===================================")

#         # Ambil input dari user
#         name = input("Nama : ")
#         age = input("Umur : ")
#         address = input("Alamat : ")

#         # format teks
#         teks = "Nama\t: {}\nUmur\t: {}\nAlamat\t: {}\n---".format(name, age, address)

#         # buka file untuk di tulis
#         # biodata = open("biodata11.txt", "a")
#         random = []
#         nama_file = "file" + ''.join(random.choice(string.digits) for _ in range(3)) + ".txt"
#         file = open(nama_file, "a+")
#         # tulis teks ke file
#         file.write(teks)

#         # tutup file
#         file.close()

#         tnya = input("\nTekan Y untuk Lanjut / Tekan n untuk Keluar : ")
#         print("\n\n")
#         if tnya == "Y" or tnya == "y":
#             main()

#         elif tnya == "N" or tnya == "n":
#             print("===============================================")
#             print("\t\tTerima Kasih Telah Mngeisi Data di Atas\t\t")
#             print("===============================================")
#             valid = False


# def main():
#     input_data()

# main()



username = input("Masukkan Username   :   ")
status = ""

if (username.islen(username) > 10 and " " not in username) == True:
    status = "Username berhasil di validasi"
else:
    status = "Username tidak valid"

print(status)
email = input("Masukkan Email   :   ")

if ("@" and "." in email) == True:
    status = "Email berhasil di validasi"
else:
    status = "Email tidak valid"

print(status)
nomor = input("Masukkan Nomor   :   ")

if nomor.isdigit() == True:
    status = "Nomor Berhasil di validasi"
else:
    status = "Nomor tidak valid"

print(status)
print()