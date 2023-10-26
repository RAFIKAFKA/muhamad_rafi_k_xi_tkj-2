# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen:22
# soal: Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
# - Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
# - Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
# - Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

penjualan_produk =float(input("masukan jumlah penjualan di bulan ini: "))

if  penjualan_produk > 1000:
    print("produk populer")
else :
    print("produk biasa")