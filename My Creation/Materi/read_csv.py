import os
os.system('cls')

# import csv

# data = []

# with open('data.csv') as baca_csv:
#     csv_baca = csv.reader(baca_csv)
#     print(csv_baca)
#     for row in csv_baca:
#         data.append(row)
# print(data)

# baca_csv.close()



# import csv

# data = []

# with open('data.csv') as baca_csv:
#     csv_baca = csv.reader(baca_csv)
#     for row in csv_baca:
#         data.append(row)

# header = data.pop(0)

# print(header)
# print(data)

# baca_csv.close()




# import csv

# data = []

# with open('data.csv') as baca_csv:
#     csv_baca = csv.reader(baca_csv)
#     for row in csv_baca:
#         data.append(row)

# header = data.pop(0)

# print(header[0], '\t', header[1], '\t', header[2])
# print("-"*42)
# for data in data:
#     print(data[0], '\t', data[1], '\t', data[2])

# baca_csv.close()



""
# import csv

# data = []

# with open('data.csv') as baca_csv:
#     csv_baca = csv.reader(baca_csv)
#     for row in csv_baca:
#         data.append(row)

# header = data.pop(0)

# print(f'{header[0]} \t {header[1]} \t {header[2]}')
# print("-"*42)
# for data in data:
#     print(f'{data[0]} \t {data[1]} \t {data[2]}')

# baca_csv.close()



# "Parsing CSV jadi Dictionary"
# import csv

# data = []

# with open('data.csv') as baca_csv:
#     csv_baca = csv.DictReader(baca_csv)
#     for row in csv_baca:
#         data.append(row)

# print(data)

# baca_csv.close()


# "cara menulis data list ke file CSV"
# import csv


# with open('data.csv', 'a') as baca_csv:
#     # membuat objek writer
#     writer = csv.writer(baca_csv, quoting=csv.QUOTE_MINIMAL)
#     # menulis baris ke file CSV
#     writer.writerow(["6","Mamat","Jombang"])
#     writer.writerow(["7","Ode","Ambon"])

# print("Writing Done!")

# baca_csv.close()




import csv


with open('data.csv', 'a') as baca_csv:
    # menentukan header
    fieldnames = ['No','Nama','Alamat']

    # membuat objek writer
    writer = csv.DictWriter(baca_csv, fieldnames=fieldnames)

    # menulis baris ke file CSV
    writer.writerow({'No' : '6','Nama' : 'Mamat','Alamat' : 'Jombang'})
    writer.writerow({'No' : '7','Nama' : 'Ode','Alamat' : 'Ambon'})

print("Writing Done!")

baca_csv.close()