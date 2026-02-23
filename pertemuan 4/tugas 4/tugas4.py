print("=== REGISTRASI PESERTA SEMINAR ===")

class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama {nama} terlalu pendek! Minimal 3 karakter")

    def validasi_nama(self, nama):
        #Melarang penggunaan karakter-karakter berikut dalam menginput nama        
        not_allowed_name = "-*+,./:()!@#$%^&_+\}{'"";><?][|0123456789"
        for i in nama:
            if i in not_allowed_name:
                raise ValueError
        #Nama harus >= 3 karakter
        if len(nama) < 3:
            raise NamaError(nama)
        return True

class UmurError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur tidak memenuhi persyaratan! (17-60 tahun!)")

    #Umur harus diantara 17-60
    def validasi_umur(self, umur):
        if umur < 17 or umur > 60:
            raise UmurError(umur)
        return True
    
class EmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Nama email tidak valid! Harus mengandung '@', > 13 karakter dan mengandung 'gmail.com'")

    #Nama email harus mengandung '@', > 13 karakter dan mengandung 'gmail.com'
    def validasi_email(self, email):
        if "@" not in email or "gmail.com" not in email or len(email) < 13:
            raise EmailError(email)
        return True
    
class NoHPError(Exception):
    def __init__(self, no_HP):
        self.no_HP = no_HP
        super().__init__(f"Nomor handphone {no_HP} tidak valid! Harus terdiri dari 10-13 digit angka")

    
    def validasi_no_HP(self, no_HP):
        #No HP harus menggunakan angka 0-9
        allowed_number = "0123456789" 
        for i in no_HP:
            if i not in allowed_number:
                raise ValueError
        #No HP harus terdiri dari 10-13 digit angka
        if len(no_HP) <10 or len(no_HP) >13:
            raise NoHPError(no_HP)
        return True

#Pengecekan input-an nama    
try:
    while True:    
        try:
            data_nama = input("Masukkan nama Anda: ")
            validator_nama = NamaError("")
            #Akan menyimpan input yang sesuai kriteria ke final_nama
            if validator_nama.validasi_nama(data_nama):
                final_nama = data_nama

        #Akan dijalankan jika tidak sesuai kriteria(error)
        except NamaError as n:
            print(f"Error: {n}")
        except ValueError:
            print("Error: Masukkan huruf saja!")
        #Looping akan berhenti jika sesuai kriteria        
        else:
            break

    while True: 
        try:
            data_umur = int(input("Masukkan umur Anda (17-60): "))
            validator_umur = UmurError("")
            #Akan menyimpan input yang sesuai kriteria ke final_umur
            if validator_umur.validasi_umur(data_umur):
                final_umur = data_umur

        #Akan dijalankan jika tidak sesuai kriteria(error) 
        except UmurError as u:
            print(f"Error: {u}")
        except ValueError:
            print("Erorr: Umur harus bilangan bulat dan tidak boleh negatif!")
        #Looping akan berhenti jika sesuai kriteria
        else:
            break

    while True: 
        try:
            data_email = input("Masukkan Email anda: ")
            validator_email = EmailError("")
            #Akan menyimpan input yang sesuai kriteria ke final_email
            if validator_email.validasi_email(data_email):
                final_email = data_email

        #Akan dijalankan jika tidak sesuai kriteria(error) 
        except EmailError as e:
            print(f"Error: {e}")
        #Looping akan berhenti jika sesuai kriteria
        else:
            break

    while True: 
        try:
            data_no_HP = input("Masukkan Nomor handhpone anda: ")
            validator_no_HP = NoHPError("")
            #Akan menyimpan input yang sesuai kriteria ke final_no_HP
            if validator_no_HP.validasi_no_HP(data_no_HP):
                final_no_HP = data_no_HP

        #Akan dijalankan jika tidak sesuai kriteria(error) 
        except NoHPError as nh:
            print(f"Error: {nh}")
        except ValueError:
            print("Erorr: Nomor handphone tidak valid! Harus bilangan bulat dan tidak boleh negatif")
        #Looping akan berhenti dan mencetak "Proses input selesai." jika sesuai kriteria
        else: 
            break
finally:
    print("Proses input selesai.")

print(f"""
=== DATA PESERTA ===
Nama      : {final_nama}
Umur      : {final_umur} tahun
Email     : {final_email}
No HP     : {final_no_HP}
Status    : TERDAFTAR
""")