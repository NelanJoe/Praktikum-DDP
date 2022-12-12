class Person:
    # Property :=> variable
    nama = ""
    alamat = ""
    jurusan = ""

    # Method :=> function
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Jurusan: {self.jurusan}")


# Instance Object
person = Person()

# Assignment => isi nilai / value dalam property
person.nama = "Budi"
person.alamat = "Jakarta"
person.jurusan = "Teknik Informatika"

# Panggil method / fungsi
person.tampilkan_data()

print()

person2 = Person()

person2.nama = "Joko"
person2.alamat = "Depok"
person2.jurusan = "Sistem Informasi"

person2.tampilkan_data()