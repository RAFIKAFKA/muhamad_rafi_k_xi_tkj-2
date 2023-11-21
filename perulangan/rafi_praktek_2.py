#Nama           : Muhamad Rafi kafka
#Kelas          : XI TKJ 2
#Nomer Absen    : 22
#Soal           : Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak_awal= 5
jarak_target= 10
minggu = 0

while jarak_awal < jarak_target:
    jarak_awal = jarak_awal + 0.10 * jarak_awal
    minggu += 1
    print(f'jarak {jarak_awal} kilometer pada minggu ke {minggu}')

print(f'Dibutuhkan {minggu} minggu unutk pelari mencapai lebih dari 10 kilometer')