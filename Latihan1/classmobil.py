class mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"mobil {self.merk} berwarna {self.warna}")

mobilA = mobil("BRIO", "Putih")
mobilA.info() # output: mobil BRIO berwarna Putih