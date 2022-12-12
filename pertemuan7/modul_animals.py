class Animals:
    # Property animals dengan type: List
    animals = []


    '''
        * __init__ :=> constructor di Javascript
        * __init__ :=> Digunakan untuk menyimpan data ke dalam class
    '''
    def __init__(self, animals):
        self.animals = animals

    '''
        * Menampilkan seluruh data animals
    '''
    def index(self):
        # Perulangan
        for animal in self.animals:
            print(f"Nama hewan: {animal}")
    
    '''
        * Menampilkan data animal dengan index
    '''
    def show(self, position):
        print(f"Menampilkan animal ke - {position}: {self.animals[position]}")

    '''
        * Menyimpan data animals
    '''
    def store(self, animalName):
        self.animals.append(animalName)

        self.index()

    
    '''
        * Mengubah data animals
    '''
    def update(self, position, animalName):
        self.animals[position] = animalName

        # panggil fungsi index
        self.index()


    '''
        * Menghapus data animal
    '''
    def delete(self, position):

        # Cara hapus data animal ke 1
        del self.animals[position]

        # Cara hapus data animal ke 2
        # self.animals.remove(position)
