# No.41
import os
import subprocess

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')
# No.41
def no41():
    while True:
        clear()
        try:
            n = int(input("input a number of integer: "))
            if n >= 100:
                print("The limit is 99")
                input("Press Enter")
                continue
            elif 0 <= n < 2:
                print("Variables of number must be more than 2")
                input("Press Enter")
                continue
            else:
                a, b = 0, 1
                list_fibonacci = [a,b]
                print(f"F({1}) = {a}")
                print(f"F({2}) = {b}")
                for i in range(2, n):
                    next_fib = a + b
                    a, b = b, next_fib
                    print(f"F({i + 1}) = {next_fib}")
                    list_fibonacci.append(next_fib)
            break   
        except ValueError:
            print("Input must be appropriate")
            input("Press Enter")
            continue
    for char in list_fibonacci:
        print(char,end=' ')
# No.42
def no42():
    # Import Modul
    from blessed import Terminal
    term = Terminal() # Inisiasi untuk mempermudah pemanggilan modul
    Date = "" # Inisiasi untuk membuat kolom kosong
    with term.cbreak(): # Memasuki mode raw input (Setiap input langsung diterima)
        print(term.clear,end='') # Membersihkan terminal
        print("Format = YYYY - MM - DD")
        while True: # Mengkonfirmasi input
            print(term.move_xy(0,1) + "📅 > ",end='')
            display = (
                f"{Date[0:4]:<4}" + 
                " - " +
                f"{Date[4:6]:<2}" +
                " - " +
                f"{Date[6:8]:<2}"
            )
            # Visualisasi
            print(display + term.clear_eol, end='', flush=True)
            key = term.inkey() # Membaca tombol yang ditekan
            if key.name == "KEY_ENTER": 
                if len(Date) == 8:
                    break
            elif key.name == "KEY_BACKSPACE":
                if Date:
                    Date = Date[:-1]
            elif len(Date) < 8 and key.isdigit:
                Date += key
    new_display = (
        f"{Date[6:8]:<2}" +
        " - " +
        f"{Date[4:6]:<2}" +
        " - " +
        f"{Date[0:4]:<4}" 
    )
    print(term.clear,end='')
    print("Format = DD - MM - YYYY")
    print(f"📅 The Date is:\n{new_display}")
# No.43
def no43():
    clear()
    import random
    list_angka = []
    for _ in range (10):
        angka_random = random.randint(0,10)
        list_angka.append(angka_random)
    print(f"Before = {list_angka}")
    for i in range(len(list_angka)):
        # print(i)
        for j in range(0,len(list_angka) - i - 1):
            if list_angka[j] > list_angka[j+1]:
                # print(list_angka[j],">",list_angka[j+1]) 
                list_angka[j], list_angka [j+1] = list_angka[j+1], list_angka[j]
                # print(f"After = {list_angka}")
    print(f"After = {list_angka}")
    print(f"Angka terkecil = {list_angka[0]}\nAngka terbesar = {list_angka[10 - 1]}")
# No.44
def no44():
    clear()
    # Mulai Mencari Input Kata
    print("---------------💫Mencari Kata Yang Sama💫---------------")
    print("Kata 1 = ",end='') # end='' ,Agar tidak membuat line baru
    Kata1 = input('')
    print("Kata 2 = ",end='') # end='' ,Agar tidak membuat line baru
    Kata2 = input('')
    Kata1_nospace = Kata1.replace(" ","").lower() # Menghilangkan Spasi dan membuat sama rata
    Kata2_nospace = Kata2.replace(" ","").lower() # Menghilangkan Spasi dan membuat sama rata
    # Casting menjadi SET
    set_kata1 = set(Kata1_nospace)
    set_kata2 = set(Kata2_nospace)
    # Menggunakan Metode Intersection Milik SET
    huruf_sama = set_kata1.intersection(set_kata2)
    # print(huruf_sama)
    # Membuat Dictionary Kosong
    akhir = {}
    # Menghitung Huruf yang sama 
    for i in huruf_sama:
        jumlah_kata1 = Kata1_nospace.count(i)
        akhir[i] = jumlah_kata1
    # Mengiterasi isi dari Dictionary
    print("Elemen Kata 1 yang beberapa kali muncul di kata 2")
    for char,count in akhir.items():
        print(f"{char} atau {char.upper()}: {count}")
# No.45
def no45():
    clear()
    list_selalu_lower = ["di","ke","dari","dan", "yang", "dengan", "untuk", "pada","in", "on", "at", "to", "from", "and", "that", "which", "with", "for", "on", "at"]
    print("------------⭐Tabel Konversi Tittle Case⭐------------")
    kalimat = input("Masukkan sebuah judul: ").title()
    for char in list_selalu_lower:
        kalimat = kalimat.replace(char.title(),char.lower())
    print(f"'{kalimat}'\nWaw Judul yang keren bung!!!")
# No.46
def no46():
    clear()
    huruf_vokal = ["a","i","u","e","o"]
    print("------------⭐Menemukan Huruf Vokal⭐------------")
    input_user = input("Masukkan sebuah kata: ").lower()
    for char in huruf_vokal:
        if input_user.count(char):
            print(f"Mengandung huruf vokal {char} sebanyak {input_user.count(char)}")
        else:
            print(f"Tidak menemukan huruf vokal lagi")
# No 47
def no47():
    while True:
        clear()
        syarat = ["@",".com"]
        email = input("Input email anda: ")
        if email.count(syarat[0]) and email.count(syarat[1]):
            print(f"Email anda: {email.replace(" ","").lower()}")
            break
        else:
            input("Pastikan Email anda mengandung '@' dan '.com'")
            continue
# No.48
def no48():
    import sympy as sy
    while True:
        try:
            print("-------Mencari Bilangan Prima ke n-------")
            n = int(input("n: "))
            break
        except ValueError:
            input("Masukkan hanya bilangan bulat ")
            continue
    print(f"Bilangan prima ke - {n} adalah: {sy.prime(n)}")
# No.49
def no49():
    clear()
    import random
    import string
    huruf_random = [random.choice(string.ascii_letters + string.digits) for _ in range(10)]
    print(f"Sebelum Partisi:\nList 1: {huruf_random}")
    length = len(huruf_random)//2
    list_partisi = []
    for _ in range(length):
        isi_partisi = huruf_random.pop()
        list_partisi.append(isi_partisi)
    print(f"Sesudah Partisi:\nList 1: {huruf_random}\nList 2: {list_partisi[::-1]}")
# No.50
def no50():
    import string as st
    clear()
    alphabet_lower = st.ascii_lowercase
    alphabet_upper = st.ascii_uppercase
    input_user = str(input("Masukkan sebuah kata: "))
    hasil_enkripsi = []
    
    for char in input_user:
        if char in alphabet_lower:
            new_char = alphabet_lower[(alphabet_lower.index(char) + 1) % 26]
            hasil_enkripsi.append(new_char)
        elif char in alphabet_upper:
            new_char = alphabet_upper[(alphabet_upper.index(char) + 1 % 26)]
            hasil_enkripsi.append(new_char)
        elif char.isdigit():
            new_char = str((int(char) + 1) % 10)
            hasil_enkripsi.append(new_char)
        elif char.count(" "):
            new_char = " "
            hasil_enkripsi.append(new_char)
    
    output = ''.join(hasil_enkripsi[::-1])
    print(output)
