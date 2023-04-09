class peneliti:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
class jurnal:
    def __init__(self, judul, peneliti):
        self.judul = judul
        self.peneliti = peneliti
    def daftar_peneliti(self):
        for peneliti in self.peneliti:
            print(peneliti.nama, jurnal.judul)
peneliti1 = peneliti("Ajeng:", 20)
peneliti2 = peneliti("Bayu:", 20)

jurnal = jurnal("pelestarian lingkungan hidup", [peneliti1, peneliti2])
jurnal.daftar_peneliti()
