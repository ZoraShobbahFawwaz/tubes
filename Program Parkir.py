import os, time

def view_menu():
    print("SELAMAT DATANG DI")
    print("      PARKIR     ")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Cek Harga")
    print("4. Sort Data")
    print("5. Update Data")
    print("6. Delete Data")

def create_data():
    jenis_kendaraan = input("Masukkan Jenis Kendaraan\t: ") + " "*20
    plat_kendaraan = input("Masukkan Nomor Kendaraan\t: ") + " "*20
    waktu = time.strftime("%d%H%M") + " "*20

    data = f"{jenis_kendaraan},{plat_kendaraan},{waktu}\n"

    with open("data.txt","a",encoding="utf-8") as file:
        file.write(data)

def read_data():
    with open("data.txt","r") as file:
        data = file.readlines()

        no = "No"
        jenis = "Jenis Kendaraan"
        waktutgl = "Waktu dan Tanggal Masuk"
        plat = "Plat Nomor"

        ### Atas 
        print("="*61)
        print(f"{no:2} | {plat:10} | {jenis:15} | {waktutgl:20} |")
        print("="*61)
        
        ### Kontent
        for index,content in enumerate(data):
            konten = content.split(",")
            
            jenis = konten[0]
            nopol = konten[1]
            waktutgl = konten[2]

            print(f"{index+1:2} | {nopol:.10} | {jenis:.15} | {waktutgl:.20}\n", end="")    

        ### bawah
        print("="*61)   

def cari_data(no_data):
    with open("data.txt","r") as file:
        content = file.readlines()
        pilih = content[no_data-1]

        return pilih

def cek_harga():
    read_data()

    no_data = int(input("Masukkan Nomor\t: "))

    pilih = cari_data(no_data)
    pilih = pilih.split(",")
    jenis = pilih[0]
    jenis = jenis.replace(" ","")

    print(len(str(pilih)))

    jam_pelanggan = pilih[2]
    jam_pelanggan = int(jam_pelanggan.replace(" ",""))

    jam_sekarang = time.strftime("%d%H%M")

    total_waktu = abs(jam_sekarang - jam_pelanggan)

    if total_waktu <= 60 and jenis == "mobil":
        os.system("cls")
        print("="*30)
        print(f"Lama Parkir    : {total_waktu}")
        print(f"Tagihan Parkir : Rp 1.000.000")
        print("="*30)
    elif total_waktu <= 60 and jenis == "motor":
        os.system("cls")
        print("="*30)
        print(f"Lama Parkir    : {total_waktu}")
        print(f"Tagihan Parkir : Rp 2.000.000") 
        print("="*30)
   
def update():
    read_data()
    usr_option = int(input("Masukkan Nomor Data Yang Ingin Di Update\t: "))
    
    data = cari_data(usr_option)
    data = data.split(",")
    jeniskendaraan = data[0]
    jeniskendaraan = jeniskendaraan.replace(" ","")
    platnomor = data[1]
    platnomor = platnomor.replace(" ","")
    waktu = data[2]
    waktu = waktu.replace(" ","")

    print("Pilih Data Yang Ingin Di Update\n1. Jenis Kendaraan\n2. Plat Nomor")
    opsi_update = input("Pilihan [1,2]\t: ")

    match opsi_update:
        case "1" : jeniskendaraan = input("Masukkan Jenis Kendaraan\t: ")
        case "2" : platnomor = input("Masukkan Nomor PLat\t:")

    data_str = f"{jeniskendaraan + ' '*20},{platnomor + ' '*20},{waktu + ' '*20}\n"

    pjng_data = len(data_str * (usr_option - 1))
    print(pjng_data)

    with open("data.txt","r+",encoding="utf-8") as file:
        file.seek(pjng_data*(usr_option-1))
        file.write(data_str)

os.system("cls")
view_menu()

user_option = input("Masukkan Opsi\t: ")

match user_option:
    case "1" : create_data()
    case "2" : read_data()
    case "3" : cek_harga()
    case "4" : print("Hello World")
    case "5" : update()
    case "6" : print("Hello World")
