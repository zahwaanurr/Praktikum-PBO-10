from prakpbo10 import Persegi, PersegiPanjang, Segitiga, JajarGenjang, Lingkaran
import math

print("=============================")
nama = "Zahwa Nur Azkia Putri   |"
nim = "064002300038             |"
print("Nama:", nama)
print("NIM:", nim)
print("=============================")

# Fungsi untuk menampilkan luas dari sebuah bangun datar
def tampilkan_luas(bangun_datar, nama_bangun):
    print(f"Luas {nama_bangun}: {bangun_datar.hitung_luas()}")

# Contoh penggunaan
persegi = Persegi(7)
persegi_panjang = PersegiPanjang(7, 4)
segitiga = Segitiga(8, 6)
jajar_genjang = JajarGenjang(8, 6)
lingkaran = Lingkaran(math.sqrt(314.159 / math.pi))

tampilkan_luas(persegi, "Persegi")
tampilkan_luas(persegi_panjang, "Persegi Panjang")
tampilkan_luas(segitiga, "Segitiga")
tampilkan_luas(jajar_genjang, "Jajar Genjang")
tampilkan_luas(lingkaran, "Lingkaran")
