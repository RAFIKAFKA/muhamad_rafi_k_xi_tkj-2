#Nama           : Muhamad Rafi kafka
#Kelas          : XI TKJ 2
#Nomer Absen    : 22
#Soal           : Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

jumlah_awal_ayam = 100
target_akhir_ayam = 200
bulan = 0

while jumlah_awal_ayam <= target_akhir_ayam:
    bulan += 1
    pertambahan_ayam = jumlah_awal_ayam * 0.05
    jumlah_awal_ayam += pertambahan_ayam
    print(f'pertumbuhan ayam {jumlah_awal_ayam} pada bulan ke {bulan}')
print(f'Dibutuhkan {bulan} bulan agar jumlah ayam melebih {target_akhir_ayam} ekor.')