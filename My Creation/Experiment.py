from os import system, name

def clear():

    # Jika os Windows
    if name == 'nt':
        _ = system('cls')

    # Jika os Mac / Linux
    else:
        _ = system('clear')


def cetakMenu():
    menuMakan = [
        ["[1] Nasi Goreng", 10000],
        ["[2] Nasi Uduk", 7000],
        ["[3] Nasi India", 12000],
        ["[4] Nasi Bakar", 15000],
        ["[5] Nasi Kuning", 7000]
    ]

    print("=" * 29)
    print("+++++\tWarung Nasi\t+++++")
    print("=" * 29)

    print("\n{:<20} {:<30}\n".format('Menu','Harga'))

    for v in menuMakan:
        x, y = v
        print("{:<20} {:<30}".format(x, y))


def getHasil():
    valid = True
    while valid:
        try:
            menu = int(input("\nSilahkan Pilih Menu (1 s/d 5) : "))

            if menu == 1:
                jumlah = int(input("Jumlah Pesanan : "))
                uangu = int(input("Masukan Jumlah Uang Kamu : "))
                harga = 10000
                total = harga * jumlah
                kembalian = uangu - total

                print("\nKembalian :", kembalian)
                print("Total : ", total)

            elif menu == 2:
                jumlah = int(input("Jumlah Pesanan : "))
                uangu = int(input("Masukan Jumlah Uang Kamu : "))
                harga = 10000
                total = harga * jumlah
                kembalian = uangu - total

                print("\nKembalian :", kembalian)
                print("Total : ", total)

            elif menu == 3:
                jumlah = int(input("Jumlah Pesanan : "))
                uangu = int(input("Masukan Jumlah Uang Kamu : "))
                harga = 10000
                total = harga * jumlah
                kembalian = uangu - total

                print("\nKembalian :", kembalian)
                print("Total : ", total)

            elif menu == 4:
                jumlah = int(input("Jumlah Pesanan : "))
                uangu = int(input("Masukan Jumlah Uang Kamu : "))
                harga = 10000
                total = harga * jumlah
                kembalian = uangu - total

                print("\nKembalian :", kembalian)
                print("Total : ", total)

            elif menu == 5:
                jumlah = int(input("Jumlah Pesanan : "))
                uangu = int(input("Masukan Jumlah Uang Kamu : "))
                harga = 10000
                total = harga * jumlah
                kembalian = uangu - total

                print("\nKembalian :", kembalian)
                print("Total : ", total)

            else:
                print("[!] Input tidak dikenal, silahkan ulangi!")
                return menu

            valid = False

        except ValueError:
            print("[!] Input tidak dikenal, silahkan ulangi!")

    return menu

def ulangLagi():

    # inisiasi variable falid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # miminta input user : y / Y / n / N
            ulang = input("\n[?] Buat pesanan lagi?(y/n) : ")
            
            # jika inputan user = y / Y
            if ulang == "y" or ulang == "Y":
                main()

            # jika inputan user = n / N
            elif ulang == "n" or ulang == "N":

                # Kata penutup
                print("\t[!] Terima kasih telah menggunakan program ini!")
                print("\n\t----------------------------- # Selesai # ------------------------------\n")
            
            else:
                print("\t[!] Hanya menerima input 'y'/'n'! silahkan ulangi!")
                return ulangLagi()

            # mengganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False

        # jika input user tidak sesuai
        except ValueError:
            print("\t[!] Hanya menerima input 'y'/'n'! silahkan ulangi!")

    # mengembalikan nilai ulang
    return ulang




def main():
    clear()
    cetakMenu()
    getHasil()
    ulangLagi()

main()