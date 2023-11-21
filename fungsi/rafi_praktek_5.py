# Nama      : Muhamad Rafi kafka
# kelas     : XI TKJ 2
# No. Absen : 22
# Soal      : Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibo(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n -1) + fibo(n -2)

n = 20
hasil = fibo(n)
print(f'bilangan fibonanci ke-{n} adalah {hasil}')