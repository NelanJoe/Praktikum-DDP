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