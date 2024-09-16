import math

#fungsi untuk menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

#input dari pengguna
jari_jari = float(input("masukkan jari-jari lingkaran:"))

#menghitung luas lingkaran
hasil = luas_lingkaran(jari_jari)

#menampilkan hasil
print(f"luas lingkaran dengan jari-jari{jari_jari} adalah {hasil:.2f}")