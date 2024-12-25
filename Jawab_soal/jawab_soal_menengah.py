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
