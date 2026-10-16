class Buku:
    def __init__(self, judul, penulis="Tidak diketahui", tahun_terbit="Tidak diketahui"):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self):
        print(f"Judul   : {self.judul}")
        print(f"Penulis : {self.penulis}")

buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama")
buku2 = Buku("Struktur Data", "Siti Aminah")
buku3 = Buku("Basis Data", "Budi Santoso")
buku4 = Buku("Algoritma Pemrograman")

buku1.info()
buku2.info()
buku3.info()
buku4.info()