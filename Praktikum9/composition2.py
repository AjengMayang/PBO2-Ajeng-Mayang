class mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
class kelompokKKM:
    def __init__(self, fakultas, mahasiswa):
        self.fakultas = fakultas
        self.mahasiswa = mahasiswa
    def daftar_mahasiswa(self):
        for mahasiswa in self.mahasiswa:
            print(mahasiswa.nama, mahasiswa.nim, kelompokKKM.fakultas)
mahasiswa1 = mahasiswa("Ajeng:", (210511130))
mahasiswa2 = mahasiswa("Bayu:", (142110020))

kelompokKKM = kelompokKKM("fakultas teknik", [mahasiswa1, mahasiswa2])
kelompokKKM.daftar_mahasiswa()
