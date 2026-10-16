class Buku:
    def __init__(self, judul, penulis="Tidak diketahui", tahun_terbit="Tidak diketahui"):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self):
        print(f"Judul   : {self.judul}")
        print(f"Penulis : {self.penulis}")
        print(f"Tahun Terbit : {self.tahun_terbit}")

buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama", 2022)
buku2 = Buku("Struktur Data", "Siti Aminah", 2023)
buku3 = Buku("Basis Data", "Budi Santoso", 2024)
buku4 = Buku("Matematika", tahun_terbit=2025)
buku1.info()
buku2.info()
buku3.info()
buku4.info()