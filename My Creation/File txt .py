# input output file 

# mode teks file argumen pada bahasa python
"""
w = write mode / mode menulis dan menghapus file lama, jika file tdk ada maka akan di buat file baru
x = create / 
r = read mode only / hanya bisa baca saja
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
t = membuka file

"""
# membuat file txt
# klo open jangan lupa buat di close juga akhirnya okee
file = open("Data.txt", 'w')

file.write("ini adalah data teks yang di buat menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close()

# membaca file teks

file2 = open("Data.txt", 'r')

# membaca
print(file2.read(10))
''' membaca 1 baris '''
print(file2.readline())

file2.close()


# appending mode

file3 = open("Data.txt", 'a')

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()