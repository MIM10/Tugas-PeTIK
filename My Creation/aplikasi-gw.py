from os import system, name

def clear():

    # jika os windows
    if name == 'nt':
        _ = system('cls')

    # jika os mac / linux
    else:
        _ = system('clear')


def getHarga():

    # inisiasi variable falid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # meminta user untuk menginput jumlah password yang ingin dibuat
            # jumlah = int(input("\t[?] Masukkan Jumlah Password : "))

            menuMakan = int(input("\nPilih Menu Makanan   : "))
            jumlahMakan = int(input("Jumlah Pesanan : "))
            hargaMakanan = menuMakan * jumlahMakan
            menuMinum = int(input("Pilih Menu Minuman    : "))
            jumlahMinum = int(input("Jumlah Pesanan : "))
            hargaMinuman = menuMinum * jumlahMinum

            harga = hargaMakanan + hargaMinuman

            # mengganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False

        # jika input user tidak sesuai
        except ValueError:
            print("[!] Input salah! silahkan ulangi!")

    # mengembalikan nilai jumlah
    return harga

def cetakBon(hargaFinal):
    fileBon = open("bon.txt","w")
    isi = hargaFinal
    fileBon.writelines(str(isi))
    fileBon.close()

def cetakMenu():
    # Membuat variabel harga
    menuMakanan =  [
        ["Perkedel",4000], 
        ["Gurami",9000], 
        ["Ayam Goreng",7000], 
        ["Rendang",8000], 
        ["Bakso",15000],
    ]

    menuMinuman =  [
        ["Es Teh",6000], 
        ["Es Leci",9000], 
        ["Es Dawet",9000], 
        ["Es Cincau",8000], 
        ["Es Jeruk",8000], 
    ]

    menuMinumanHot =  [
        ["Teh Hangat",6000], 
        ["Tora Bika Cappucino",8000], 
        ["Wedang Jahe",8000], 
        ["Kopi Hitam",6000], 
        ["Good Day Cappucino",8000]
    ]

    # Mencetak Toko saya
    print("=" * 39) # print pattern
    print("+"*5,"\tWarung Makan Padang\t","+"*5)
    print("=" * 39)

    # Mencetak menu
    print("=" * 39)
    print("              Menu Makanan            ", "\t" )
    print("=" * 39)

    print ("\n\t{:<20} {:<30}\n".format('Menu','Harga'))

    for v in menuMakanan:
        x, y = v
        print ("\t{:<20} {:<30}".format(x, y))

    print("=" * 39)
    print("          Menu Minuman Dingin         ")
    print("=" * 39)

    print ("\n\t{:<20} {:<30}\n".format('Menu','Harga'))

    for v in menuMinuman:
        x, y = v
        print ("\t{:<20} {:<30}".format(x, y))

    print("=" * 39)
    print("          Menu Minuman Panas          ")
    print("=" * 39)

    print ("\n\t{:<20} {:<30}\n".format('Menu','Harga'))

    for v in menuMinumanHot:
        x, y = v
        print ("\t{:<20} {:<30}".format(x, y))

def main():
    clear()
    cetakMenu()
    hargaFinal = getHarga()
    cetakBon(hargaFinal)

main()