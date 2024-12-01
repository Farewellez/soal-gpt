import os
import subprocess
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

# No.1
def no1():
    clear_terminal()
    Variabel = 10
    print(Variabel,type(Variabel))
# No.2
def no2():
    clear_terminal()
    nama_depan = "Ahmad"
    nama_belakang = "Zafarell"
    namaku = nama_depan + " " + nama_belakang
    print(namaku)
# No.3
def no3():
    clear_terminal()
    Variabel1 = int(input("Masukkan Sebuah angka pertama: "))
    Variabel2 = int(input("Masukkan Sebuah angka kedua: "))
    clear_terminal()
    print("Hasil Penjumlahan: ", Variabel1 + Variabel2)
    print("Hasil Pengurangan: ", Variabel1 - Variabel2)
    print("Hasil Perkalian: ", Variabel1*Variabel2)
    print("Hasil Pembagian: ", Variabel1/Variabel2)
# No.4
def no4():
    clear_terminal()
    Variabel = 5.5
    konversi_string = f"{Variabel}"
    print(konversi_string,type(konversi_string))
# No.5
def no5():
    nama = input("Input your name: ")
    usia = int(input("Input your age: "))
    clear_terminal()
    print("Nama saya " + nama + ", saya berusia " + str(usia) + " tahun.")
# No.6
def no6():
    clear_terminal()
    ini_string = input("Ketik sesuatu: ")
    while True:
        try:
            if ini_string.count(" "):
                clear_terminal()
                tanpa_string = ini_string.replace(" ","") 
                print(f"{ini_string} memiliki panjang karakter: {len(ini_string)} (include spasi)\n")
                print(f"{ini_string} memiliki panjang karakter: {len(tanpa_string)} (exclude spasi)")
                break
            else:
                clear_terminal()
                print(f"{ini_string} memiliki panjang karakter: {len(ini_string)}")
                break
        except ValueError:
            clear_terminal()
            print("Mohon maaf ulangi inputnya")
            continue
# No.7
def no7():
    while True:
        clear_terminal()
        try:
            ini_integer = input("Masukkan Sebuah Angka: ")
            tanpa_spasi = ini_integer.replace(" ","")
            tanpa_spasi = int(tanpa_spasi)
            break
        except ValueError:
            print("Masukkan hanya sebuah bilangan bulat!!!")
            continue
    konversi_float = tanpa_spasi + 0.0
    konversi_integer = f"{tanpa_spasi}"
    clear_terminal()
    print(f'''
    Input anda ({tanpa_spasi}) telah diubah menjadi:
    {konversi_float}: Tipe = {type(konversi_float)}
    {konversi_integer}: Tipe = {type(konversi_integer)}
        ''')
# No.8
def no8():
    clear_terminal()
    while True:
        ini_string = str(input("Input sesuatu: "))
        tanpa_spasi = ini_string.replace(" ","")
        try:
            clear_terminal()
            if len(tanpa_spasi) < 5:
                print("Input harus mengandung minimal mengandung 5 Huruf/karakter: ")
                continue
            else:
                break
        except ValueError:
            print("ERROR ULANGI INPUT DENGAN BENAR!!!")
            continue
    if ini_string.count(" "):    
        clear_terminal()
        print(f"Input anda adalah: {ini_string}")
        print(f"Karakter ke-2 sampai ke-5 = {tanpa_spasi[1:5]} (Tanpa Spasi)")
        print(f"Karakter ke-2 sampai ke-5 = {ini_string[1:5]} (Dengan Spasi)")
    else:
        clear_terminal()
        print(f"Input anda adalah: {ini_string}")
        print(f"Karakter ke-2 sampai ke-5 = {tanpa_spasi[1:5]}")
# No.9
def no9():
    nama_buah = "Durian"
    print(f"{nama_buah} diubah menjadi huruf besar semua = {nama_buah.upper()}")
    print(f"{nama_buah} diubah menjadi huruf kecil semua = {nama_buah.lower()}")
# No.10
def no10():
    while True:
        nama_user = input("Input Namamu: ")
        nama_tanpa_spasi = nama_user.replace(" ","")
        if not nama_tanpa_spasi.isalpha():
            print("Nama Hanya Mengandung Huruf")
            continue
        else:
            clear_terminal()
            nama_user = str(nama_user)
            break
    while True:
        usia_user = input("Input Usiamu: ")
        usia_tanpa_spasi = usia_user.replace(" ","")
        if not usia_tanpa_spasi.isdigit():
            print("Input Hanya Angka")
            continue
        else:
            clear_terminal()
            usia_user = int(usia_user)
            break
    clear_terminal()
    print("Halo,",nama_user + "!","Kamu berusia",usia_tanpa_spasi,"tahun.")
# No.11
def no11():
    while True:
        try:
            angka_random = float(input("Masukkan sebuah angka: "))
            angka_random2 = float(input("Masukkan angka lagi: "))
            clear_terminal()
            print(f"Penjumlan dari kedua input angka adalah = {angka_random + angka_random2}")
            break
        except ValueError:
            clear_terminal()
            print("Masukkan hanya angka!!!")
            continue
# No.12
def no12():
    while True:
        try:
            angka1 = int(input("Masukkan sebuah bilangan bulat: "))
            angka2 = int(input("Masukkan bilangan bulat kedua: "))
            break
        except ValueError:
            clear_terminal()
            print("Input hanya berupa bilangan bulat, tanpa spasi dan hanya angka!!!")
            continue
    if angka1 > angka2:
        clear_terminal()
        print("Angka pertama adalah",angka1,"dan angka kedua adalah",angka2)
        print(angka1 > angka2,f"karena {angka1} lebih dari {angka2}")
    else:
        clear_terminal()
        print("Angka pertama adalah",angka1,"dan angka kedua adalah",angka2)
        print(angka1 > angka2,f"karena {angka1} tidak lebih dari {angka2}")
# No.13
def no13():
    while True:
        try:
            angka_random = float(input("Masukkan sebuah angka: "))
            angka_random2 = float(input("Masukkan angka lagi: "))
            clear_terminal()
            print(f"Pembagian dari kedua input angka adalah = {angka_random // angka_random2}")
            break
        except ValueError:
            clear_terminal()
            print("Masukkan hanya angka!!!")
            continue
        except ZeroDivisionError:
            clear_terminal()
            print("Pembagi (input kedua) tidak boleh nol!!!")
            continue
# No.14
def no14():
    while True:
        try:
            variabel = int(input("Mau melakukan perulangan berapa kali???: "))
            break
        except ValueError:
            print("Masukkan hanya bilangan bulat tanpa spasi!!!")
            continue
    for i in range(variabel):
        print("Hello")
# No.15
def no15():
    π = 22/7
    while True:
        try:
            r = float(input("Masukkan nominal radius lingkaran: "))
            break
        except ValueError:
            print("Masukkan hanya angka tanpa spasi!!!")
            continue
    print(f"Luas lingkaran adalah πr² = π dikali {r}² = {π*r**2}")
# No.16
def no16():
    print(f'''
        Variabel 1 = {"ayam",type('ayam')} ini string 
        Variabel 2 = {1,type(1)} ini integer
        Variabel 3 = {1.0,type(1.0)} ini float
        Variabel 4 = {True and False,type(False)} ini boolean
        Variabel 5 = {1j,type(1j)} ini complex number''')
# No.17
def no17():
    while True:
        angka1 = str(input("Masukkan angka 1: "))
        angka2 = str(input("Masukkan angka 2: "))
        if not angka1.isdigit and angka2.isdigit:
            print("Masukkan hanya sebuah angka tanpa spasi")
            continue
        else:
            break
    clear_terminal()
    print(f"Angka 1 = {angka1,type(angka1)}\nAngka 2 = {angka2,type(angka2)}")
    awal = 0
    akhir = 0
    for angka in angka1:
        awal = awal*10 + (ord(angka) - ord('0'))
    for char in angka2:
        akhir = akhir*10 + (ord(char) + ord('0'))
    print(f"sekarang...{awal,type(awal)} dan {akhir,type(akhir)} berubah menjadi integer")
# No.18
def no18():
    text = "Ini String"
    print(type(text),"Ini adalah string")
# No.19
def no19():
    a = True
    b = False
    print(
        f'''
        {a and b} = {a} dan {b}
        {a or b} = {a} atau {b}
        {a ^ b} = {a} XOR {b}   
        {a ^ a} = {a} XOR {a}
        ''')
# No.20
def no20():
    text = "Python"
    print(f"Karakter pertama dan terakhir dari {text} adalah {text[0:6:5]}")
