class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

dosenA = Dosen("Ajeng", 29, "123456")
dosenA.berbicara() # Output: Ajeng sedang berbicara.
dosenA.mengajar() # Output: Ajeng dengan NIP 123456 sedang mengajar.