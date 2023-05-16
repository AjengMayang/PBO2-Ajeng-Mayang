try:
    file = open("file.txt", "r")
    num = int(file.readline())
except ValueError:
    print("Error: Input tidak valid!")
finally:
    file.close()



try:
    x = "Hello"
    y = x + 5
except TypeError:
    print("Terjadi kesalahan tipe data, pastikan variabel yang digunakan sudah benar!")