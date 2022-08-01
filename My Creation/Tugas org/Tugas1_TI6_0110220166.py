def hasilnilai() :
	nilai_kuis = 0.15 * int(input("Nilai Kuis : "))
	nilai_tugas1 = 0.15 * int(input("Nilai Tugas 1 : "))
	nilai_tugas2 = 0.20 * int(input("Nilai Tugas 2 : "))
	nilai_uts = 0.25 * int(input("Nilai UTS : "))
	nilai_uas = 0.25 * int(input("Nilai UAS : "))
	nilai_akhir = float(nilai_kuis + nilai_tugas1 + nilai_tugas2 + nilai_uts + nilai_uas)
	return nilai_akhir

def hasilgrade(nilai_akhir):
	if ( nilai_akhir >= 85 and nilai_akhir <= 100) :
		huruf_grade = "A"
		angka_grade = 4.00
	elif ( nilai_akhir >= 70 and nilai_akhir < 85) :
		huruf_grade = "B"
		angka_grade = 3.00
	elif ( nilai_akhir >= 55 and nilai_akhir < 70) :
		huruf_grade = "C"
		angka_grade = 2.00
	elif ( nilai_akhir >= 40 and nilai_akhir < 55) :
		huruf_grade = "D"
		angka_grade = 1.00
	elif ( nilai_akhir < 40) :
		huruf_grade = "E"
		angka_grade = 0.00
	elif ( nilai_akhir > 100) :
		huruf_grade = "S"
		angka_grade = 5.00
	return huruf_grade, angka_grade

def matakuliah(jns_matkul) :
	bbn_sks_anda = int(input("Beban SKS mata kuliah: "))
	nilai_akhir_anda = hasilnilai()
	huruf_grade_anda, angka_grade_anda = hasilgrade(nilai_akhir_anda)
	hasil_akhir = bbn_sks_anda * angka_grade_anda
	print("Nilai Grade untuk",jns_matkul,":",nilai_akhir_anda,"(",huruf_grade_anda,")")
	print()
	return hasil_akhir, bbn_sks_anda

def tampilkan() :
	print()
	print("=======Fitur Input Data=======")
	print("Nama : Ahmad Fauzan")
	print("NIM : 0110220166")
	print("==============================")
	print()

def perangkat_utama():
    tampilkan()
    nim = input("Masukkan NIM (0110220XXX) : ")
    jml_matkul = int(input("Masukkan Jumlah Matkul (1-8) : "))
    if (jml_matkul > 8) :
	    print("Jumlahnya melebihi batas!")
    else :
	    print()
	    sks = 0
	    index = 0.0
	    for i in range (1, 1+jml_matkul) :
		    y = sks
		    x = index
		    print("Mata Kuliah ",i)
		    matkul = input("Nama mata kuliah : ")
		    index, sks = matakuliah(matkul)
		    sks = sks + y
		    index = index + x
	    print("----Rangkuman----")
	    print("NIM :",nim)
	    print("Total SKS :",sks)
	    print("Indeks Prestasi :",index/sks)

perangkat_utama() 