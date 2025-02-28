class Mahasiswa:
    def __init__(self, nama, angkatan):
        self.nama = nama
        self.angkatan = angkatan
    def tampilkan(self):
        print(f"Kenalin aku {self.nama}, dari angkatan {self.angkatan} ")

Mahasiswa1 = Mahasiswa('Salwa', 2024)
Mahasiswa1.tampilkan()

del Mahasiswa1
print("\nSetelah menggunakan keyword del:")
Mahasiswa1.tampilkan()