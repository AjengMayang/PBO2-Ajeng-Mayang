class penulis:
    def __init__(self, nama, penerbit):
        self.nama = nama
        self.penerbit = penerbit
class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def daftar_penulis(self):
        for penulis in self.penulis:
            print(penulis.nama, penulis.penerbit, buku.judul)
penulis1 = penulis("Andrea Hirata:","BENTANG PUSTAKA")

buku = buku("Laskar Pelangi", [penulis1])
buku.daftar_penulis()
