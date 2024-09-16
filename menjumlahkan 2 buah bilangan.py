#minta input dari pengguna
bilangan = int(input("masukkan bilangan:"))
#cek apakah bilangan tersebut genap atau ganjil
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil")