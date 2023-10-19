# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen: 22
# soal: Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."
estimasi_selesai = input("masukan estimasi waktu selesai proyek (tahun-bulan-tanggal): ")
tanggal_target_selesai = input("masukkan tanggal target selesai(tahun-bulan-tanggal): ")


if estimasi_selesai <= tanggal_target_selesai:
    print("tempat waktu")
else:
    print("terlambat")    