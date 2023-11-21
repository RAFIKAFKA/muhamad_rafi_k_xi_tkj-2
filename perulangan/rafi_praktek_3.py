#Nama           : Muhamad Rafi kafka
#Kelas          : XI TKJ 2
#Nomer Absen    : 22
#Soal           :Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

invetasi_awal = 10000
target_ivestasi = 20000
tahun = 0

while invetasi_awal < target_ivestasi:
    invetasi_awal = invetasi_awal + 0.06 * invetasi_awal
    tahun += 1
    print(f'Nilai investasi {invetasi_awal} pada tahun ke {tahun}')

print(f'Diutuhkan {tahun} tahun agar nilai investasi mencapai 20.000 dollar')