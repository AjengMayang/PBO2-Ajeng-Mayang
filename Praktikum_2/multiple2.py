class Hewan:
    def __init__(self, nama, makanan):
        self.nama = nama
        self.makanan = makanan
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"makanan: {self.makanan}")

class mamalia:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat
    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")

class nokturnal:
    def __init__(self, metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat
    def display_info(self):
        print(f"Metamorfosis: {self.metamorfosis}")
        print(f"Habitat: {self.habitat}")

class kelelawar(mamalia, nokturnal):
    def __init__(self, nama, makanan, jenis, habitat, metamorfosis):
        Hewan.__init__(self, nama, makanan)
        mamalia.__init__(self, jenis, habitat)
        nokturnal.__init__(self, metamorfosis, habitat)
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"makanan: {self.makanan}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        print(f"Metamorfosis: {self.metamorfosis}")

kelelawarA = kelelawar("kelelawar ", "buah-buahan", "mamalia-nokturnal", "goa atau hutan", "tidak sempurna")
kelelawarA.display_info()