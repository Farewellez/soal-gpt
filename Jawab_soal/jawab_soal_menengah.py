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
# No.28
def no28():
    clear_terminal()
    while True:
        input_user = input("Masukkan sebuah kalimat atau kata random: ")
        import shlex
        jumlah_kata = shlex.split(input_user)
        total_kata = len(jumlah_kata)
        print(f"Jumlah kata dalam kalimat tersebut adalah {total_kata}")
        print("Kata yang terdapat dalam kalimat tersebut adalah = ",end="")
        for i, kata in enumerate(jumlah_kata):
            if i == total_kata - 1:
                print(kata)
            else:
                print(kata,end=",")
        print("\nApakah ada yang salah?\nMohon maaf jika ada yang salah, Mungkin system menganggap Sebuah kalimat yang memiliki spasi terhitung sebagai 2 kalimat")
        print("\nOlehkarena itu jika ada kata yang mengandung spasi namun itu adalah satu kata, contoh:\n bersuka cita = 1 kata (namun mengandung spasi)\n Tolong tambahkan 'bersuka cita' pada input\n Contoh: Aku 'Bersuka Cita' = 2 kata")
        looping = input("Apakah mau mengulang? [y/n]: ")
        looping2 = looping.lower() 
        if looping2 == "y":
            continue
        elif looping2 == "n":
            break
        else:
            print("Otomatis mengulang")
            continue
    return
# No.29
def no29():
    clear_terminal()
    import random
    angka_random = round(random.uniform(-999,999), 2)
    bulat_kebawah = int(angka_random)
    bulat_keatas = int(angka_random + 1)
    print("Angka desimal acak = " + str(angka_random))
    print(f"\nPembulatan kebawah = {bulat_kebawah}\nPembulatan keatas = {bulat_keatas}")
    return
# No.30
def no30():
    clear_terminal()
    acak = "AHBBHBDNANCbbnbkchbadhBFLABDhlfblnjnj3h47398h8fh83n83tZetaahbfhbfbilbrgbzcbvbaubrubugburbgbzjsguorgorosgjZetaayifyoivvofayeyioirg78g47gbf8h2p4hg9834h80h4t0Zetaaaaaaabuibfieyoboybfoeaoyf73i64t618t666403t14t3180t4"
    print(acak)
    zeta = acak.count("Zeta")
    print("\nTebak ada berapa kata Zeta di kalimat itu: ")
    while True:
        print("Jangan lupa input angka ya...😸")
        tebak = int(input("Tebak (Cluenya adalah Farell <3 Zeta): "))
        match tebak:
            case 3:
                clear_terminal()
                print(f"Yap bener banget jawabannya adalah {zeta}\n3 = <3 Zeta😻")
                break
            case _:
                clear_terminal()
                print("Yah salah banget! Masa cewe secantik zeta ga keliatan😾")
                break
        break
    return
# No.31
def no31():
    while True:
        clear_terminal()
        try:
            print("Masukkan sebuah bilangan bulat")
            print("Ingat ya...Hanya bilangan bulat😾")
            input_user = int(input("Bilangan bulat: "))
            break
        except ValueError:
            continue
    if input_user%2 == 0:
        print(f"{input_user} adalah angka genap")
    else:
        print(f"{input_user} adalah angka ganjil")
    return
# No.32
def no32():
    while True:
        clear_terminal()
        try:
            print("Masukkan sebuah bilangan bulat")
            print("Ingat ya...Hanya bilangan bulat😾")
            input_angka = int(input("Input User: "))
            input_angka2 = int(input("Input angka kedua: "))
        except ValueError:
            continue
        while True:
            clear_terminal()
            print("masukkan operasi dari kedua bilangan [ + / - / x / : ]")
            print("------------------(Masukkan hanya yang ada di dalam pilihan ya!!!😾)------------------")
            operator = input("Pilih: ")
            if operator == "+":
                print(f"{input_angka} + {input_angka2} = {input_angka + input_angka2}")
            elif operator == "-":
                print(f"{input_angka} - {input_angka2} = {input_angka - input_angka2}")
            elif operator == "x":
                print(f"{input_angka} x {input_angka2} = {input_angka * input_angka2}")
            elif operator == ":":
                print(f"{input_angka} : {input_angka2} = {input_angka / input_angka2}")
            else:
                continue
            break
        break
    return
# No.33
def no33():
    while True:
        try:
            clear_terminal()
            n = int(input("Masukkan sebuah bilangan bulat: "))
        except ValueError:
            continue
        break
    print(f"Mengitung faktorial dari {n} = {n}!")
    angka = 1
    for i in range(1, n + 1):
        angka *= i
    return angka
# No.34
def no34():
    while True:
        clear_terminal()
        import random
        try:        
            n = int(input("Berapa angka random yang kamu inginkan?\ninput: "))
        except ValueError:
            continue
        break
    # Membuat list dari inputan user dengan tipe data string
    list_angka = []
    for _ in range(n):
        angka_random = random.randint(-999,999)
        list_angka.append(str(angka_random))
    # Proses validasi isi dari list 
    print(f"Memasukkan {n} angka random (Tipe String) ke dalam list: {list_angka}")
    # Proses Casting Tipe data string menjadi integer
    for index, number in enumerate (list_angka):
        print(str(index + 1) + "." ,number,type(number))
    print("\nMengubah tipe data menjadi integer: ")
    cast_number = []
    for new_number in list_angka:
        cast_number.append(int(new_number))
    list_angka.clear()
    list_angka.extend(cast_number)
    print(f"list hasil casting: {list_angka}")
    for new_index,finish in enumerate (list_angka):
        print(str(new_index + 1) + ".",finish,type(finish))
