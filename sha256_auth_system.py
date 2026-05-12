import hashlib

users_db = {}

# Fungsi hash SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registrasi user
def registrasi():
    print("\n=== REGISTRASI USER ===")

    username = input("Masukkan username : ").strip()

    if not username:
        print("❌ Username tidak boleh kosong!")
        return

    if username in users_db:
        print("❌ Username sudah terdaftar!")
        return

    password = input("Masukkan password : ").strip()

    if not password:
        print("❌ Password tidak boleh kosong!")
        return

    hashed_pw = hash_password(password)

    # Simpan user
    users_db[username] = hashed_pw

    print("\n✅ Registrasi Berhasil")
    print(f"Username      : {username}")
    print(f"Hash Password : {hashed_pw}")

# Login user
def login():
    print("\n=== LOGIN USER ===")

    username = input("Masukkan username : ").strip()

    if username not in users_db:
        print("❌ Username tidak ditemukan!")
        return

    password = input("Masukkan password : ").strip()

    # Verifikasi password
    hashed_input = hash_password(password)

    print("\n=== VERIFIKASI ===")
    print(f"Hash Input     : {hashed_input}")
    print(f"Hash Tersimpan : {users_db[username]}")

    if hashed_input == users_db[username]:
        print("\n✅ Status Login : BERHASIL")
    else:
        print("\n❌ Status Login : GAGAL")

# Tampilkan data user
def tampilkan_user():
    print("\n=== DATA USER ===")

    if not users_db:
        print("Belum ada user.")
        return

    print(f"{'No':<5}{'Username':<20}Hash Password")
    print("-" * 80)

    for i, (username, hashed_pw) in enumerate(users_db.items(), start=1):
        print(f"{i:<5}{username:<20}{hashed_pw}")

# Main Program
def main():

    print("========================================")
    print(" SISTEM REGISTRASI & LOGIN SHA-256 ")
    print("========================================")

    while True:

        print("\n=== MENU ===")
        print("1. Registrasi")
        print("2. Login")
        print("3. Tampilkan User")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4) : ").strip()

        if pilihan == "1":
            registrasi()

        elif pilihan == "2":
            login()

        elif pilihan == "3":
            tampilkan_user()

        elif pilihan == "4":
            print("\nProgram selesai.")
            break

        else:
            print("❌ Pilihan tidak valid!")


if __name__ == "__main__":
    main()