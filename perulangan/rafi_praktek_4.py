#Nama           : Muhamad Rafi kafka
#Kelas          : XI TKJ 2
#Nomer Absen    : 22
#Soal           : Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

apel_awal = 100
target_sisa = 20
hari = 0

while apel_awal > target_sisa:
    apel_awal = apel_awal - 0.10 * apel_awal
    hari += 1
    print(f'Sisa apel {apel_awal} pada hari ke {hari}')

print(f'Dibutuhkan {hari} hari agar sisa apel mencapai 20')