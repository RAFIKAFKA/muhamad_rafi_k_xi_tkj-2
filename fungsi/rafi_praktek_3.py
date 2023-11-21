# Nama      : Muhamad Rafi kafka
# kelas     : XI TKJ 2
# No. Absen : 22
# Soal      : Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def pangkat(bil, ekspo):
    hasil = bil ** ekspo
    return hasil

bil = 5
ekspo = 8
hasil = pangkat(bil, ekspo)
print(f"hasil pangkat dari {bil} dengan eksponen {ekspo} adalah {hasil}")