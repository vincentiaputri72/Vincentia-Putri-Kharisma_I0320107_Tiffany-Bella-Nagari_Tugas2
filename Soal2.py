# Vincentia Putri Kharisma
# I0320107
# Kelas C
# Soal 2

l1 = "H"
l2 = "a"
l3 = "l"
l4 = "o"
nama = "Vincentia Putri Kharisma"
tempat_lahir = "Tangerang"
tanggal_lahir = float(8)
bulan_lahir = float(7)
tahun_lahir = float(2002)
tinggi_badan = 156
ukuran_sepatu = 40
alamatDesa = "Rangkah"
alamatRT = "01"
alamatRW = "04"
alamatKecamatan = "Buayan"
alamatKabupaten = "Kebumen"
alamatProvinsi = "Jawa Tengah"
kode_pos = 54474
tanggal_sekarang = 13
bulan_sekarang = 3
tahun_sekarang = 2021
hobi = "membaca, menonton anime, tidur"
semester = "Semester 2"
program_studi = "Teknik Industri"
perguruan_tinggi = "UNS"
w1 = l1 + l2 + l3 + l4
w2 = "Terima kasih"
salam_pembuka = w1
salam_penutup = w2
umur = float((tanggal_sekarang - tanggal_lahir) + ((bulan_sekarang - bulan_lahir) * 30) + ((tahun_sekarang-tahun_lahir) * 365))
pendidikan = semester + program_studi + perguruan_tinggi

print(salam_pembuka)
print("Nama saya", nama)
print("Saya lahir di", tempat_lahir)
print("Saat ini, saya tinggal di", "Desa", alamatDesa, "RT", alamatRT, "/ RW", alamatRW, ", Kecamatan", alamatKecamatan, ", Kabupaten", alamatKabupaten, ", Provinsi", alamatProvinsi, kode_pos)
print("Saya berusia", umur, "hari")
print("Saat ini saya menempuh pendidikan", semester, program_studi, perguruan_tinggi)
print("Tinggi badan saya", tinggi_badan, "cm")
print("Ukuran sepatu saya adalah", ukuran_sepatu)
print(salam_penutup)