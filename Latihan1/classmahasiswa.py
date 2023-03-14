class mahasiswa:
    def __init__(self, nama, nim,):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"nama: {self.nama}\nnim: {self.nim}")

mahasiswaB = mahasiswa("Ajeng Mayang", "210511130")
mahasiswaB.info()      