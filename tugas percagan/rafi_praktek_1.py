# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen: 22
# soal: Deskripsi Pekerjaan: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarka jumlah total belanjaan pelanggan,

total_belanjaan = float(input("Total belajaan Anda:"))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"Total pembayaran setelah diskon: {total_pembayaran}")