class Buku:
    def __init__(self, judul, penulis, tahunterbit):
        self.judul = judul
        self.penulis = penulis
        self.tahunterbit = tahunterbit
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}\ntahunterbit: {self.tahunterbit}")
bukuA = Buku("pada senja yang membawamu pergi", "Boy Candra", "terbit tahun 2016")
bukuA.info()