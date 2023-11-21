# Nama      : Muhamad Rafi kafka
# kelas     : XI TKJ 2
# No. Absen : 22
# Soal      : Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def fac(x):
    if x  == 0:
        return 1
    else:
        return x * fac(x - 1)

x = 5
hasil = fac(x)
print(f"faktorial dari {x} adalah {hasil}")