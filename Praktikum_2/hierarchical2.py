class kedelai:
    def __init__(self, gizi, vitamin):
        self.gizi = gizi
        self.vitamin = vitamin
    def get_gizi(self):
        return self.gizi
    def get_vitamin(self):
        return self.vitamin
    
class fermentasi(kedelai):
    def __init__(self, gizi,vitamin, ragi):
        super().__init__(gizi,vitamin)
        self.ragi = ragi
    def get_ragi(self):
        return self.ragi
    
class tempe(kedelai):
    def __init__(self, gizi,vitamin, teksturtempe):
        super().__init__(gizi,vitamin)
        self.teksturtempe = teksturtempe
    def get_teksturtempe(self):
        return self.teksturtempe
    
# Hierarchical Inheritance
class tempegoreng(fermentasi):
    def __init__(self, gizi,vitamin, ragi, tempegorengtepung):
        super().__init__(gizi,vitamin, ragi)
        self.tempegorengtepung = tempegorengtepung
    def get_tempegorengtepung(self):
        return self.tempegorengtepung