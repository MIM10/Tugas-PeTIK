# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
    
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))

# a = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
# print("Deret Fibonacci")
# for i in range(a):
#     print(fibonacci(i), end=' ')

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

a = int(input("\nMasukan Panjang Deret : "))
for i in range(a):
    print(fibonacci(i), end=' ')


# nilai = int(input("Masukan nilai n : "))
# faktorial = 1

# for i in range(1, nilai + 1):
#     faktorial *= i

# print(f'{nilai}! = {faktorial}')


# no = [5, 10, 15, 20, 25, -30, -35]

# print(no)
# print("Nilai Terbesar :", max(no))
# print("Nilai Terkecil :", min(no))
