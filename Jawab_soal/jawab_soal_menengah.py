import os
import subprocess
from datetime import datetime
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

# No.21
def no21():
    harga = 100000
    diskon = 15/100
    print("Halo Kami memiliki produk seharga:\nRp. 100000")
    while True:
        try:
            user_input = input(f"Kami juga memiliki sebuah diskon sebesar 15% apakah anda tertarik?\n [y/n]")
            if user_input == "y":
                break
            elif user_input == "n":
                exit()
            else:
                print("pilihannya hanya [y/n]")
                continue
        except ValueError:
            print("ERROR\nTolong periksa kembali inputan anda!")
            continue
        break
    harga_akhir = int(harga - (harga * diskon))
    print(f"Harga produk saat ini menjadi {harga_akhir}")
    input("Tekan Enter")
    clear_terminal()
    return
# No.22
def no22():
    now = datetime.now()
    while True:
        clear_terminal()
        try:
            print("Halo, untuk daftar KTP tolong masukkan tahun, bulan dan tanggal lahir anda:")
            birth_year = int(input("Tahun Lahir: "))
            birth_month = int(input("Bulan Lahir: "))
            birth_day = int(input("Tanggal Lahir: "))
        except ValueError:
            clear_terminal()
            print("ERROR\nTolong periksa kembali inputan anda!")
            input("Tekan Enter")
            continue
        while birth_year > now.year:
            clear_terminal()
            print("Pastikan tahun lahir anda tidak lebih besar dari tahun sekarang")
            birth_year = int(input("Tahun Lahir: "))
        clear_terminal()
        if birth_year < now.year:
            if birth_month == now.month:
                if birth_day < now.day:
                    umur_user = now.year - birth_year - 1
                elif birth_day >= now.day:
                    umur_user = now.year - birth_year
            elif birth_month < now.month:
                umur_user = now.year - birth_year - 1
            elif birth_month > now.month:
                umur_user = now.year - birth_year 
        elif birth_year == now.year:
            print("FITUR PERHITUNGAN UMUR BERDASARKAN BULAN BELUM DI BUAT!!!")
            input("Tekan Enter!!!")
            continue
        print (f"Umur Anda saat ini adalah {umur_user} tahun")
        break
    return
# No.23
def no23():
    code_name = "Isla"
    reverse = code_name[::-1]
    return reverse
# No.24
def no24():
    print("Menghitung angka 1 hingga n buah angka: ")
    n = int(input("Masukkan angka n: "))
    while n <= 0:
        print("Maaf, n harus lebih besar dari 0")
        continue
    total = 0
    for i in range (1, n + 1):
        total += i
    print(total)
# No.25
def no25():
    print("Masukkan 3 buah angka: ")
    while True:
        try:
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            angka3 = int(input("Masukkan angka ketiga: "))
        except ValueError:
            print("Masukkan hanya angka!")
            continue
        break
    average = (angka1 + angka2 + angka3) / 3
    averagee = (angka1 + angka2 + angka3) // 3
    print(f"Rata-rata dari 3 angka tersebut adalah:\n{angka1} + {angka2 } + {angka3} : 3 = {average}")
    print(f"Jika dibulatkan adalah = {averagee}")
    return
# No.26
def no26():
    while True:
        try:
            celcius = int(input("Input sebuah suhu (°C): "))
            print("Suhu akan diubah ke fahrenheit (°F)")
        except ValueError:
            print("Masukkan hanya angka!")
            continue
        break
    print(f"Suhu {celcius}°C = {celcius * 9/5 + 32}°F")
    print("FYI 1°C = 1,8°F dan 0°C = 32°F")
# No.27
def no27():
    import random
    import string
    random_letter = random.choice(string.ascii_letters)
    print(f"Huruf acak = {random_letter}")
    input_user = input("Masukkan sebuah kata acak yang anda inginkan:\nKata Acak: ")
    print(f"Huruf acak yang anda inginkan = {input_user}")
    output = random_letter + input_user[1::]
    print(f"Karakter pertama dari {input_user} ditukar dengan {random_letter}")
    print(f"Menghasilkan : {output}")
