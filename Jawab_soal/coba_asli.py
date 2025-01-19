from blessed import Terminal

def no42():
    term = Terminal()
    input_text = ""  # Menyimpan seluruh input user
    
    with term.cbreak():
        print(term.clear)  # Bersihkan terminal
        print("The Format Is YYYY-MM-DD")
        
        while True:
            print(term.move_xy(0, 2) + "> ", end="")  # Prompt tetap di posisi
            # Bentuk format dinamis berdasarkan panjang input
            display = (
                f"{input_text[:4]:<4}"  # Bagian YYYY
                + "-"
                + f"{input_text[4:6]:<2}"  # Bagian MM
                + "-"
                + f"{input_text[6:8]:<2}"  # Bagian DD
            )
            print(display + term.clear_eol, end="", flush=True)
            
            key = term.inkey()  # Baca satu karakter input
            
            print(f"\n[DEBUG] Key pressed: {repr(key)}")  # Debugging output
            
            if key.name == "KEY_ENTER":  # Tekan Enter untuk menyelesaikan
                if len(input_text) == 8:  # Pastikan format lengkap
                    break
            
            elif key.name == "KEY_BACKSPACE":  # Backspace untuk menghapus
                if input_text:
                    input_text = input_text[:-1]
            
            elif len(input_text) < 8 and key.isdigit():  # Batasi input hanya 8 digit angka
                input_text += key
            
        # Hasil akhir
        print("\nFinal Input:", f"{input_text[:4]}-{input_text[4:6]}-{input_text[6:8]}")

# Jalankan fungsi
no42()
