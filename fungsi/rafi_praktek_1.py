# Nama      : Muhamad Rafi kafka
# kelas     : XI TKJ 2
# No. Absen : 22
# Soal      : Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deratan(batas):
    total = 0
    for i in range(1, batas + 1):
        bil_ganjil = 2 * i -1
        total += bil_ganjil
    return total

batas = 10
hasil = total_deratan(batas)
print(f"total deret bilangan ganjil hingga batas {batas} adalah {hasil}")