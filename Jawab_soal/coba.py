kata1 = input("Masukkan kata pertama: ").strip().lower()
kata2 = input("Masukkan kata kedua: ").strip().lower()
jumlah = kata2.count(kata1)
print(f"Kata '{kata1}' muncul sebanyak {jumlah} kali dalam kata kedua.")
