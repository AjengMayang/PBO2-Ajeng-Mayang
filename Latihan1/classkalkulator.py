class kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('tidak dapat membagi nol!')
        return x / y 
    
# memanggil metode statis add() dan subtract() di dalam class math
print(kalkulator.add(3, 8))          # output: 11
print(kalkulator.subtract(8, 3))     # output: 5

# memanggil metode statis multiply() dan divide() di dalam class math
print(kalkulator.multiply(3, 8))          # output: 24
print(kalkulator.divide(8, 3))            # output: 2.7