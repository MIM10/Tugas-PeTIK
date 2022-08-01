buah = "ini adalah nama-nama buah yang mengandung Vitamin C \n"
buah_list = """    
~ Nanas
~ Mangga
~ Kiwi
~ Jeruk
~ Jambu Biji
"""

f = open("buah.txt", "w")
f.write(buah)
f.writelines(buah_list)
