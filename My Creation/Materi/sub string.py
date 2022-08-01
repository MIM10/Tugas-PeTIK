import os
os.system('cls')

# memecah sub string menggunakan teknik iterasi

def substring():

    arrays = []
    s = "Selamat"
    for i in s:
        arrays.append(i)

    s = arrays[1] + arrays[0] + arrays[2] + arrays[3] + arrays[4] + arrays[5] + arrays[6]
    print(arrays)
    print(s)

def escape_character():
    s = "Pertama\nKedua" # menyisipkan baris baru
    t = "Asslamu\'alaikum" # menyisipkan
    u = "D:\\program.py" # menyisipkan
    v = "Pertama\t\tKedua" # menyisipkan

    print(s)
    print(t)
    print(u)
    print(v)

def string_index():
    s = "Hello"
    # s = "olleH"
    s = s[-1] + s[-2] + s[-3] + s[-4] + s[-5]
    # print(s[4] + s[3] + s[2] + s[1] + s[0])
    print(s)

def string_slice():
    # s = 'Hello'
    # print("=" * 20)
    # print(s[1:4])
    # print(s[1:-1])
    # print(s[:4])
    # print(s[1:])

    x = 'salam' 
    print("=" * 20)
    print(x[1:4:2])
    print(x[:4:3])
    print(x[1::2])
    print(x[::-1])

def string_methods():
    s = 'salam'
    print(s.lower())                # membuat seluruh isi string menjadi huruf kecil
    print(s.capitalize())           # membuat huruf string menjadi kapital
    print(s.upper())                # membuat seluruh isi string menjadi huruf besar
    print(s.replace('m', 'h'))      # mengganti karakter 'm' menjad 'h'
    print(s.count('a'))             # menghitung jumlah karakter 'a'
    print(s.startswith('s'))        # jika string diawali dengan huruf 's' maka nilai True
    print(s.endswith('h'))          # jika string diakhiri dengan huruf 'h' maka nilai True
string_methods()







# #    0123456789
# s = "Selamat Pagi"
# #       987654321
# print(s[-11::3])
# print(s[-9:11:2])
# print(s[2:8:3])
# print(s[3:8])
# print(s[2:-5])
# print(s[5:9])
# print(s[-8:9])


# # Python program to demonstrate
# # String slicing
# String = 'GEEKSFORGEEKS'

# # Using indexing sequence
# print(String[::5])
