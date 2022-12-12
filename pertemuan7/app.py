from Animals import Animals


animal = Animals(["guguk", "meong", "singa"])

# Menampilkan semua data animals
animal.index()
print()

# Menampilkan animals dengan index : urutan
print("Menampilkan animals dengan index")
animal.show(2)
print()


# Menambhakan data animals
print("Menambahkan data animals")
animal.store("unta")
print()

# Mengubah data animal
print("Mengubah data animal")
animal.update(1, "gorila")
print()


# Menghapus data animal
print("Menghapus data animal")
animal.delete(0)
print()
