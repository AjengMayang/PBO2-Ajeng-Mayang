class binatang:
    def __init__(self, nama):
        self.nama = nama
    def bicara(self):
        print(f"{self.nama} bicara")

class kucing(binatang):
    def __init__(self, nama, keturunan):
        super().__init__(nama)
        self.keturunan = keturunan
    def turunan(self):
        print(f"{self.nama} sejenis kucing anggora {self.keturunan}")

class kucinganggora(kucing):
    def __init__(self, nama, keturunan, asal):
        super().__init__(nama, keturunan)
        self.asal = asal
    def bicara(self):
        print(f"{self.nama} adalah {self.asal} kucinganggora berasal dari turki")
kucinganggora = kucinganggora("dodo", "turki", "meraung")
kucinganggora.bicara() # Output: dodo adalah kucinganggora berasal dari turki
kucinganggora.turunan() # Output: dodo sejenis kucing anggora


