# def sum(n):
#     if n == 1:
#         return n
#     else:
#         return n + sum(n-1)

# print(sum(5))




# def ping(i):
#     if i < 0:
#         return pong(i-1)
#     else:
#         return 0
# def pong(i):
#     if i > 0:
#         return ping(i-1)
#     else:
#         return 1

# print(ping(5))




# def tampilkanAngka(batas, i = 1):
#     print(f'Perulangan ke {i}')

#     if (i < batas):
#         # Disinilah rekursif itu terjadi
#         tampilkanAngka(batas, i + 1)

# # Memanggil fungsi tampilkanAngka
# tampilkanAngka(10)




# def tampilkanAngka(batas, i = 1):

#     if (i < batas):
#         # Disinilah rekursif itu terjadi
#         tampilkanAngka(batas, i + 1)

#     print(f'Perulangan ke {i}')

# # Memanggil fungsi tampilkanAngka
# tampilkanAngka(10)




# def tampilkanAngka(batas, i = 10):
#     print(f'Perulangan ke {i}')

#     if (i > batas):
#         # Disinilah rekursif itu terjadi
#         tampilkanAngka(batas, i - 1)

# # Memanggil fungsi tampilkanAngka
# tampilkanAngka(1)




def tampilkanAngka(batas, i = 1):
    prefix = '--' * (i -1)

    print(f'{prefix} Sebelum Rekursif ({i})')
    if(i < batas):
        # Disinilah rekursif itu terjadi
        tampilkanAngka(batas, i + 1)

    print(f'{prefix} Setelah Rekursif ({i})')

# Memanggil fungsi tampilkanAngka
tampilkanAngka(5)




# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))




# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * 1
#     return result

# print(factorial(5))