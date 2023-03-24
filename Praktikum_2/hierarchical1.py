class tepung:
    def __init__(self, merek, terigu):
        self.merek = merek
        self.terigu = terigu
    def get_merek(self):
        return self.merek
    def get_terigu(self):
        return self.terigu
    
class adonan(tepung):
    def __init__(self, merek, terigu, manis):
        super().__init__(merek, terigu)
        self.manis = manis
    def get_manis(self):
        return self.manis
    
class cake(tepung):
    def __init__(self, merek, terigu, ketebalancake):
        super().__init__(merek, terigu)
        self.ketebalancake = ketebalancake
    def get_ketebalancake(self):
        return self.ketebalancake
    
# Hierarchical Inheritance
class birthdaycake(adonan):
    def __init__(self, merek, terigu, manis, blackforest):
        super().__init__(merek, terigu, manis)
        self.blackforest = blackforest
    def get_blackforest(self):
        return self.blackforest