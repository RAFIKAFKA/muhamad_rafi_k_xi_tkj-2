# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen:22
# soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut:
# - Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
# - Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
# - Peminjaman lebih dari 30 hari: "Peminjaman Panjang"
pemimjaman_diperpus = float(input("memasukan lama pinjaman: "))
if peminjaman_diperpus <=7:
    print("pinjaman jangka pendek")
elif peminjaman_diperpus >30:
    print("pinjaman jangka panjang")
else:
    print("pinjaman jangka menengah")