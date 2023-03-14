class PesawatTerbang:
    def __init__(self, maskapai, tujuan, kodepenerbangan):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.kodepenerbangan = kodepenerbangan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nkodepenerbangan: {self.kodepenerbangan}")
pesawatA = PesawatTerbang("Lion Air", "Jakarta - Bali", "JT/LNI")
pesawatA.info()
