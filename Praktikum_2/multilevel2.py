class binatang:
    def __init__(self, nama):
        self.nama = nama
    def bicara(self):
        print(f"{self.nama} bicara")

class mamalia(binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama)
        self.habitat = habitat
    def hutan(self):
        print(f"{self.nama} habitat di hutan {self.habitat}")

class harimau(mamalia):
    def __init__(self, nama, habitat, makanan):
        super().__init__(nama, habitat)
        self.makanan = makanan
    def bicara(self):
        print(f"{self.nama} adalah {self.makanan} harimau menggaung")
harimau = harimau("hana", "hutan", "daging")
harimau.bicara() # Output: hana adalah harimau menggaung
harimau.hutan() # Output: habitat hana di hutan