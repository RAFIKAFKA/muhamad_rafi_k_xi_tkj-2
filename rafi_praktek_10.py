# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen:22
# soal: Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
# - Performa 5: Bonus 20% dari gaji tahunan.
# - Performa 4: Bonus 10% dari gaji tahunan.
# - Performa 3: Bonus 5% dari gaji tahunan.
# - Performa 2: Bonus 2% dari gaji tahunan.
# - Performa 1: Tidak ada bonus.
# Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.
performa = int(input("Masukkan nilai performa karyawan kalian (dari 1 - 5): "))
gaji = float(input("gaji karyawan dalam setahun ini: "))
 

if performa == 5:
    bonus = gaji * 0.20
elif performa == 4:
    bonus == gaji * 0.10
elif performa == 3:
    bonus = gaji * 0.05
elif performa == 2:
    bonus = gaji * 0.02
else:
    bonus = 0
total_gaji = bonus = gaji
print(f"total gaji setahun dari karyawan kalian: {total_gaji}")






