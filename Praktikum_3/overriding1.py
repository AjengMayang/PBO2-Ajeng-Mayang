class singa:
    def bersuara(self):
        print("rawrrr")
class kambing:
    def bersuara(self):
        print("mbee mbee")
def cetak_suara(objek):
    objek.bersuara()
singa = singa()
kambing = kambing()
cetak_suara(singa) # Output: rawrrr
cetak_suara(kambing) # Output: mbee mbee