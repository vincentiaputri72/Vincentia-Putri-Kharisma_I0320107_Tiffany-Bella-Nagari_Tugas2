#Vincentia Putri Kharisma
#I0320107
#Kelas C
#Soal 1

print("Mesin penghitung luas persegi panjang, luas lingkaran, dan luas kubus")
print("****")
print("****")
print("1. Penghitung luas persegi panjang")

p = float(input("panjang sisi:"))
l = float(input("lebar sisi:"))

L_pp = p * l

print("Jadi luas persegi panjang tersebut adalah", L_pp)
print("****")

print("2. Penghitung luas lingkaran")

r = float(input("jari-jari lingkaran:"))

L_o = 3.14 * (r ** 2)

print("Jadi luas lingkaran tersebut adalah", L_o)
print("****")

print("3. Penghitung luas kubus")

s = float(input("panjang sisi lingkaran:"))

L_kubus = 6 * (s ** 2)

print("Jadi luas kubus tersebut adalah", L_kubus)
print("****")


print("Mesin pengkonversi suhu (celcius-farenheit, reamur-kelvin)")
print("....")
print("....")
print("1. Pengkonversi suhu dari celcius ke farenheit")

C = float(input("suhu dalam celcius:"))

F = (C * (9 / 5)) + 32

print("Jadi suhu tersebut adalah", F, "F")
print("....")

print("2. Pengkonversi suhu dari reamur ke kelvin")

R = float(input("suhu dalam reamur:"))

K = ((5 / 4) * R) + 273

print("Jadi suhu tersebut dalam Kelvin adalah", K, "K")


