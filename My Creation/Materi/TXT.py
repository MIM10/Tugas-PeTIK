# # membaca text file

# # buka file
# puisi = open("puisi.txt", "w")

# puisi.write("\nengkau bahkan bukan lagi variabel bagiku...")
# puisi.write("\nengkau adalah konstanta abadi yang tak tergantikan...")
# puisi.write("\ntidak ada yang bisa memisahkan integer dan float...\n\n")

# puisi.close()

# puisi2 = open("puisi.txt", "r")
# print(puisi2.read())
# print(puisi2.readlines())
# puisi2.close()

# puisi3 = open("puisi.txt", "a")

# puisi3.write("\n\t\tAku adalah Spyware mu")
# puisi3.write("\n\nAku adalah Spyware mu")
# puisi3.write("\nAku mencari tahu Favorites dan History mu")
# puisi3.write("\nAku melakukkan checkdisk dan diskclean up untukmu")
# puisi3.write("\nKadang RAM-ku tak cukup kuat memikirkanmu,")
# puisi3.write("\nkadang kau membuatku hang dan crashed,")
# puisi3.write("\nHardware ku selalu panas")
# puisi3.write("\nKau adalah virus firstlove.exe yang menyerang ke seluruh tubuhku")
# puisi3.write("\nAvira,AVG, Smadav ataupun antivirus terhebat sekalpun pun tak bisa me-remove mu")
# puisi3.write("\nKadang ku mau Format, bahkan install ulang diriku")
# puisi3.write("\nagar aku bisa me-remove mu dari hardisk ku")

# puisi3.close()



# f = open("puisi.txt", "r")

# print(f.read())
# # print(f.readlines())


# puici = puisi2.readlines()
# for teks in puici:
#     print(teks)



# # no_rek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))






# a = "Berikut adalah nama-nama hari dalam satu pekan"
# b = ["\n~ Senin", "\n~ Selasa", "\n~ Rabu", "\n~ Kamis", "\n~ Jum'at", "\n~ Sabtu", "\n~ Minggu"]

# c = open("Nama Hari.txt", "w")
# c.write(a)
# c.writelines(b)
# c.close()








# print("===================================")
# print("Selamat Datang Pada Program Biodata")
# print("===================================")

# biodata = open("biodata.txt", "r+")
# teks = biodata.read()

# print(teks)

# # Ambil input dari user
# name = input("Nama : ")
# age = input("Umur : ")
# address = input("Alamat : ")

# # format teks
# teks = "Nama\t: {}\nUmur\t: {}\nAlamat\t: {}\n---".format(name, age, address)

# # buka file untuk di tulis

# # tulis teks ke file
# biodata.write(teks)

# # tutup file
# biodata.close()


# 



print("===================================")
print("Selamat Datang Pada Program Biodata")
print("===================================")

# buka file untuk di tulis
biodata = open("biodata.txt", "r+")
teks = biodata.read()
print(teks)

# Ambil input dari user
name = input("Nama\t: ")
tmp = input("Tmp\t: ")
tgl = input("Tgl\t: ")
age = input("Umur\t: ")
gender = input("Gender\t: ")
gd = input("Golongan Darah\t: ")
agama = input("Agama\t: ")
kwn = input("KWN\t: ")
hp_ = input("No Hp\t: ")
email = input("Email\t: ")
address = input("Alamat\t: ")

# format teks
teks = """
Nama\t: {}
Tmp\t\t: {}
Tgl\t\t: {}
Umur\t: {}
Gender\t: {}
Golongan Darah\t: {}
Agama\t: {}
KWN\t\t: {}
No Hp\t: {}
Email\t: {}
Alamat\t: {}
---\n
""".format(name, tmp, tgl, age, gender, gd, agama, kwn, hp_, email, address)  # , address)

# tulis teks ke file
biodata.writelines(teks)

# tutup file
biodata.close()