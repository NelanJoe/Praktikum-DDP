
class Person():
    # Definisikan awal variable
    name = ""
    address = ""
    age = 0

    # Constructor :=> Pembungkus
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    
    # Methond /  Function
    def sayHello(self):
        print("Hello nama saya ", self.name, "usia saya ", self.age, "alamat saya di ", self.address)


# Extend :=> nurunin sifat dari class Person
class Student(Person):
    # Manggil constructor class Person
    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(name, address, age)
        self.nim = nim
        self.jurusan = jurusan
 
# Instance object

jundi = Student("jundi", "Bogor, Jabar", 20, "0110221180", "Sistem Informasi")

jundi.sayHello()
print("Nim: ", jundi.nim)
print("Jurusan: ", jundi.jurusan)
