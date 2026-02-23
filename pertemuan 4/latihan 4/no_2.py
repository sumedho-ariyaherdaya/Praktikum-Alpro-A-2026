try: 
    angka_1 = float(input("Masukkan angka pertama: "))
    angka_2 = float(input("Masukkan angka kedua: "))
    hasil = angka_1/angka_2
except ValueError:
    print("Harus bilangan bulat atau float")
except ZeroDivisionError:
    print("Angka pembagi tidak boleh nol")
else:
    print(f"Hasilnya: {hasil}")
finally:
    print("Selesai.")
