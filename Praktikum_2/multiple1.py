class karyawan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
    def pergikekantor(self):
        print(self.nama, "sedang pergi ke kantor")

class kantor:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")

class karyawankantor(karyawan, kantor):
    def __init__(self, nama, alamat, pekerjaan):
        karyawan.__init__(self, nama, alamat)
        kantor.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

kry_kantor = karyawankantor("Bayu", "Majalengka", "Programmer")
kry_kantor.pergikekantor() # output: Bayu sedang pergi ke kantor
kry_kantor.bekerja() # output: Bayu sedang bekerja
kry_kantor.bersosialisasi() # output: Bayu sedang bersosialisasi