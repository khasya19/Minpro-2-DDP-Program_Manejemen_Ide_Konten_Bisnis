# Minpro-2-DDP-Program_Manejemen_Ide_Konten_Bisnis
**A. PENJELASAN PROGRAM MANEJEMEN DATA IDE KONTENTEN BISNIS****

Program ini adalah aplikasi manejemen catatan ide konten yang khusus dibuat untuk keperluan promosi/branding bisnis pribadi.

Data ini setiap ide disimpan sementara dalam bentuk list berisi tuple dengan format: (judul_ide, platfrom, status)

program ini menyediakan menu berulang (looping dengan while) yang akan terus berjalan sampai pengguna memilih menu keluar. setiap input divalidasi menggunakan conditional statement, sehingga jika pengguna memasukkan data yang salah/tidak sesuai, program tidak akan crash melainkan meminta pengguna mengulang input. dan sudah menyediakan 2 role yaitu admin dan user dengan hak akses yang berbeda.

**B. FLOWCHART ALUR PROGRAM**

   <img width="667" height="465" alt="Screenshot 2026-10-06 183928" src="https://github.com/user-attachments/assets/c3835f0a-1495-46f3-a51a-062de2451712" />

  1. program di mulai deri menu awal (1. login, 2. keluar). pilihan kedua untuk mengakhiri program.

  2. pada login, pengguna mengisi username dan password. jika salah, pengguna boleh mengulang sampai 3 kali, lalu kembali ke menu awal

  3. jika benar, program akan mengecek role

  4. admin masuk ke menu dengan CRUD lengkap: tambah, tampilkan, ubah, dan keluar

  5. user masuk ke menu terbatas: tambah, tampilkan, dan keluar

  6. setiap input divalidasi. jika tidak valid, pengguna diminta mengulang

  7. setelah satu proses selesai, program kembali ke menu role masing-masing. dan jika memilih keluar akan kembali lagi ke menu awal

**C. DOKUMENTASI PROGRAM DAN OUTPUT**

a. Library dan Dictionary - menambahakan os, time, pwinput di import. dictionary user untuk menyimpan password dan role tiap akun, status_opsi menyimpan pilihan status ide, dan daftar_ide menyimpan data ide.

<img width="663" height="259" alt="image" src="https://github.com/user-attachments/assets/a12c9550-3850-4aec-8a1d-daf79ef190a2" />


b. login - meminta username dan password (pwinput berguna untuk menyembunyikan password), lalu cek ke dictionary user. salah sampai 3 kali login akan di tolak. kalau benar, fungsi akan mengembalikan role

<img width="667" height="280" alt="image" src="https://github.com/user-attachments/assets/daa81caf-0412-419b-81e1-f9c0141b2590" />


c. menu awal - menampilkan menu login/keluar. role hasil login di cek dengan if/elif: admin ke main(), user ke menu_user()

<img width="675" height="342" alt="image" src="https://github.com/user-attachments/assets/a1f2f715-8781-476c-8b58-5584de4d9ee6" />


d. menu admin - menu 5 pilihan dengan validasi isdigit(). tiap pilihan memanggil CRUD yang sesuai


<img width="836" height="122" alt="image" src="https://github.com/user-attachments/assets/1c97a163-6f12-4e2e-b5c0-22d2c8a8418b" />
<img width="822" height="376" alt="image" src="https://github.com/user-attachments/assets/5d1d46d1-9ed2-4c74-bf4b-9674df296443" />


e. input status dan tambah data - judul dan platfrom tidak boleh kosong, status diambil dari status_opsi. data di simpan dengan append()

<img width="836" height="452" alt="image" src="https://github.com/user-attachments/assets/82dc1a1d-5c02-4412-a7bc-55b257345beb" />
<img width="832" height="157" alt="image" src="https://github.com/user-attachments/assets/f12f819c-3609-4a11-b6c2-f4c3fbc7e9bb" />


f. tampilkan data - jika data kosong tampil pesan, jika tidak data dilooping dengan enumeret() dan di tampilkan dalam tabel beserta totalnyaa


<img width="822" height="191" alt="image" src="https://github.com/user-attachments/assets/7fd6ef3e-e001-4e38-8d09-02e2d02a3c5b" />


g. ubah data - validasi nomor ide (angka 0= batal,harus ada di daftar). kolom yang dikosongkan tidak diubah. data di ganti lewat index

<img width="838" height="199" alt="image" src="https://github.com/user-attachments/assets/23db9edd-b8ae-4947-b96c-5d36a373e02e" />
<img width="839" height="470" alt="image" src="https://github.com/user-attachments/assets/aeb6e680-c73c-48a2-93c0-5307584bc88c" />


h. hapus data - validasinya sama dengan ubah. data di hapus dengan pop(index) dan yang terhapus di tampilkan

<img width="842" height="436" alt="image" src="https://github.com/user-attachments/assets/67120118-47d8-4dd5-bcca-b261e2b4d5e0" />


i. menu user - menu terbtas hanya ada tambah dan tampilkan

<img width="841" height="370" alt="image" src="https://github.com/user-attachments/assets/116ea1dd-194e-401f-ab56-d70c8ed00734" />


**OUTPUT**

a. user

<img width="329" height="455" alt="image" src="https://github.com/user-attachments/assets/189efeac-9ce8-4630-94f9-4bb325ed41cd" />


b. admin

<img width="329" height="439" alt="image" src="https://github.com/user-attachments/assets/ed4cf1ce-92ee-4ffc-b7e4-4780b8c2a4d6" />


D. PENERAPAN NILAI TAMBAH
1. sudah menggunakan library pwinput, os, dan time

Nama: Khasya Fatlaikha

NIM: 2609116068





