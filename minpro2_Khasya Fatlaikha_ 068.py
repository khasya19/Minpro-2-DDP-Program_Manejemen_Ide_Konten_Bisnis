
# ==========================================================
# PROGRAM MENEJEMEN DATA IDE KONTEN UNTUK BISNIS
# ==========================================================

import os
import time
import pwinput

user = {
    "admin": {"password": "khasya567", "role": "admin"},
    "user": {"password": "khasya123", "role": "user"}
}
daftar_ide = [
    ("video review produk skincare", "TikTok","belum di eksekusi"),
    ("Testimoni pelanggan", "Instagram", "Sedang Dijalankan")
]
status_opsi = {
    "1": "belum dieksekusi",
    "2": "sedaang dijalankan",
    "3": "selesai",
    "4": "dibatalkan"
}

def tampilkan_header(judul):
    print("\n" + "=" * 55)
    print (judul.center(55))
    print("=" * 55)

def tampilkan_menu():
    tampilkan_header("MENU MENEJEMEN IDE KONTEN BISNIS")
    print("1. Tambah data ide: ")
    print("2. Tampilkan seluruh data ide: ")
    print("3. ubah data ide: ")
    print("4. hapus data ide: ")
    print("5. keluar ")
    print("-"*55)

def tampilkan_data():
    tampilkan_header("DAFTAR IDE KONTES BISNIS SAAT INI")
    if len(daftar_ide) == 0:
        print("belum ada data ide")
        return

    print(f"{'No':<4}{'judul ide':<32}{'platfrom':<14}{'status':<20}")
    print("-" * 70)
    for i, ide in enumerate(daftar_ide, start=1):
        judul, platfrom, status = ide
        print(f"{i:<4}{judul:<32}{platfrom:<14}{status:<20}")
        print("-" * 70)
        print(f"total ide: {len(daftar_ide)}")

def input_status():
    """Meminta input status dengan validasi (1-4) samapai benar."""
    while True:
        print("pilih status ide: ")
        print("1. belum dieksekusi")
        print("2. sedang dijalankan")
        print("3. selesai")
        print("4. dibatalkan")
        pilihan = input("masukkan pilihan (1-4): "). strip()
        if pilihan in status_opsi:
            return status_opsi[pilihan]
        else:
            print(">> Input tidak valid! Harap masukkan angka 1-4.\n")

def tambah_data():
    tampilkan_header("TAMBAH DATA IDE KONTEN BISNIS")
    #validasi judul ide tidak boleh kosong
    while True:
        judul = input("masukkan judul ide konten: ").strip()
        if judul == "":
            print(">> Judul tidak boleh kosong! coba lagi.\n")
        else:
            break

    #validasi platform tidak boleh kosong
    while True:
        platform = input("masukkan platfrom (TikTok/Instagram/Youtube/blog/dll): ").strip()
        if platform == "":
            print(">> Platform tidak boleh kosong! coba lagi.\n")
        else:
            break

    status = input_status()

    ide_baru = (judul, platform, status)
    daftar_ide.append(ide_baru)

    print("\n>> Data berhasil ditambahkan!")
    print(f" Data baru: {ide_baru}")

def ubah_data():
    tampilkan_header("UBAH DATA IDE  KONTES BISNIS")

    if len(daftar_ide) == 0:
        print("belum ada data untuk diubah.")
        return

    tampilkan_data()

    while True:
        pilihan = input("\nMasukkan nomor ide yang ingin  diubah (atau 0 untuk batal): ").strip()

        if not pilihan.isdigit():
            print(">> Input harus berupa angka! coba lagi.\n")
            continue

        pilihan = int(pilihan)

        if pilihan == 0:
            print(">> Proses ubah data dibatalkan")
            return
        elif 1 <= pilihan <= len(daftar_ide):
            break
        else:
            print(">> Nomor tidak ditemukan dalam daftar! coba lagi.\n")

    index = pilihan - 1
    data_lama = daftar_ide[index]
    print(f"\nData lama : {data_lama}")

    judul_baru = input(f"Judul ide baru (kosongkan jika tidak diubah) [{data_lama[0]}]: ").strip()
    if judul_baru == "":
        judul_baru = data_lama[0]

    platfrom_baru = input(f"platfrom baru (kosongkan jika tidak diubah) [{data_lama[1]}]: ").strip()
    if platfrom_baru == "":
        platfrom_baru = data_lama[1]  

    print("ubah status ide?")
    status_baru = input_status()

    daftar_ide[index] = (judul_baru, platfrom_baru, status_baru)

    print("\n>> Data berhasil diubah!")
    print(f" data lama : {data_lama}")
    print(f" data baru : {daftar_ide[index]}")

def hapus_data():
    tampilkan_header("HAPUS DATA IDE KONTEN BISNIS")
    if len(daftar_ide) == 0:
        print("belum ada data untuk dihapus. ")
        return
    
    tampilkan_data()

    while True:
        pilihan = input("\n>>Masukkan nomor ide  yang ingin di hapus (atau 0 untuk batal): ").strip()

        if not pilihan.isdigit():
            print(">> Proses hapus data dibatalkan. ")
            continue

        pilihan = int(pilihan)

        if pilihan == 0:
            print(">> Proses hapus data dibatalkan. ")
            return
        elif 1 <= pilihan <= len(daftar_ide):
            break
        else:
            print(">> Nomor tidak ditemukan dalam daftar! coba lagi.\n")

    index = pilihan - 1
    daftar_terhapus = daftar_ide.pop(index)

    print("\n>> Data berhasil dihapus!")
    print(f" Data yang dihapus: {daftar_terhapus}")

def main():
    tampilkan_header("SELAMAT DATANG DI PROGRAM IDE KONTEN BISNIS")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if not pilihan.isdigit():
            print(">> Input tidak Valid! Harap masukkan angka 1-5.\n")
            continue

        pilihan = int(pilihan)
        if pilihan  == 1:
            tambah_data()
        elif pilihan == 2:
            tampilkan_data()
        elif pilihan == 3:
            ubah_data()
        elif pilihan == 4:
            hapus_data()
        elif pilihan == 5:
            print("\nTerima kasih telah program Manejemen ide konten bisnis!")
            print("sampai jumpa lagi.")
            break
        else:
            print(">> Pilihan tidak tersedia! Harap masukkan angka  1-5.\n")

def bersih():
    os.system("cls" if os.name == "nt" else "clear")
    
def login():
    "Login maksimal 3x, mengembalikan role (admin/user) atau None"
    tampilkan_header("LOGIN")
    percobaan = 0
    while percobaan < 3:
        username = input("username: ").strip()
        password = pwinput.pwinput("password: ").strip()

        if username in user and user[username]["password"] == password:
            print(f"\n>> Login berhasil! selamat datang, {username}")
            time.sleep(1)
            return user[username]["role"]
        else:
            percobaan += 1
            print(f">> Username atau password salah!({percobaan}/3)\n")

    print(">> Kesempatan login habis!")
    time.sleep(1)
    return None

def menu_user():
    """Menu hanya ditambahkan & dilihat datanya."""
    while True:
        tampilkan_header("MENU USER")
        print("1. Tambah data ide: ")
        print("2. tampilkan seluruh data ide: ")
        print("3. keluar")
        print("-"*55)
        pilihan = input("pilih menu (1-3): ").strip()

        if not pilihan.isdigit():
            print(">> input tidak valid! harap masukkan angka 1-3.\n")
            continue

        pilihan = int(pilihan)
        if pilihan == 1:
            tambah_data()
        elif pilihan == 2:
            tampilkan_data()
        elif pilihan == 3:
            print(">> Anda sudah keluar.")
            time.sleep(1)
            break
        else:
            print(">> Pilihan teidak tersedia! harap masukkan angka 1-3.\n")

def menu_awal():
    """Menu awal: login dulu, lalu diarahkan sesuai role."""
    while True:
        bersih()
        tampilkan_header("PROGRAM IDE BISNIS")
        print("1. LOGIN ")
        print("2. KELUAR ")
        print("-" * 55)
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            role = login()
            if role == "admin":
                main()
            elif role == "user":
                menu_user()
            else:
                print(">> Login gagal. Silakan coba lagi.")
        elif pilihan == "2":
            print("\nTerima kasih, sampai jumpa lagi.")
            break
        else:
            print("\n>> Pilihan tidak tersedia! Harap masukkan angka 1-2")
            time.sleep(1)

if __name__ == "__main__":
    menu_awal()