# 🔐 Sistem Registrasi & Login Menggunakan SHA-256
Tugas Mata Kuliah Kriptografi

## 📋 Identitas

| Keterangan | Isi |
|---|---|
| Nama | Muh. As’ad Habib |
| No. Urut | 04 |
| Mata Kuliah | Kriptografi |
| Universitas | Universitas Muhammadiyah Makassar |

---

## 📖 Deskripsi Program

Program ini dibuat untuk menerapkan konsep keamanan password menggunakan algoritma SHA-256 pada sistem registrasi dan login user. Password yang dimasukkan pengguna akan diproses menjadi hash sebelum disimpan sehingga data password lebih aman dan tidak tersimpan dalam bentuk asli.

---

## ✅ Fitur Program

- Registrasi user
- Login user
- Hash password menggunakan SHA-256
- Penyimpanan username dan hash password
- Verifikasi password saat login
- Menampilkan status login
- Menampilkan daftar user yang tersimpan

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Keterangan |
|---|---|
| Bahasa Pemrograman | Python |
| Library | hashlib |
| Algoritma | SHA-256 |

Library yang digunakan merupakan library bawaan Python sehingga tidak memerlukan instalasi tambahan.

---

## 🚀 Cara Menjalankan Program

### Clone Repository

```bash
git clone https://github.com/Muh-Asad-Habib/sha256-auth-system.git
cd sha256-auth-system
```

### Jalankan Program

```bash
python sha256_auth_system.py
```

---

## 🔄 Cara Kerja Program

### Registrasi User

1. User memasukkan username dan password
2. Password diubah menjadi hash SHA-256
3. Username dan hash password disimpan ke database sementara

### Login User

1. User memasukkan username dan password
2. Password login diubah menjadi hash SHA-256
3. Hash hasil login dibandingkan dengan hash yang tersimpan
4. Sistem menampilkan status login berhasil atau gagal

---

## 🔒 Tentang SHA-256

SHA-256 merupakan algoritma hash yang digunakan untuk menjaga keamanan data dengan menghasilkan output unik sepanjang 64 karakter hexadecimal. Algoritma ini banyak digunakan dalam sistem keamanan modern karena sulit dibalik ke bentuk aslinya dan memiliki tingkat keamanan yang tinggi.

---

## 📝 Tujuan Pembuatan

Program ini dibuat sebagai tugas implementasi kriptografi untuk memahami penggunaan algoritma hash SHA-256 dalam pengamanan password pada sistem login sederhana.
