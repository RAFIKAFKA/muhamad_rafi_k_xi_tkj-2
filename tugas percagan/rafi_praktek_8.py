# nama: muhamad rafi kafka
# kelas: XI TKJ 2
# nomor absen:22
# soal: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."
 
persiapan_proyek = input("apakah proyek sudah siap untuk diluncurkan? (siap/belum): ")
if persiapan persiapan_proyek.lower() == "siap":
    print("proyek sudah siap untuk diluncurkan.")
else:
    print("proyek belum siap untuk diluncurkan.")