#PYTHON CLASS PROPERTIES
#Class Properties
class Person:
  def __init__(self, name, age):
    self.name = name #-> properti nama
    self.age = age # -> properti umur

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#Access Properties
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand) #-> mengakses properti brand pada objek car1
print(car1.model) #-> mengakses properti model pada objek car1

#Modify Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print("Umur sebelum diubah:")
print(p1.age)

p1.age = 26 #-> mengubah nilai properti age menjadi 26
print("Umur setelah diubah:")
print(p1.age)

#Delete Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # Akan mencetak nama
# print(p1.age) # Akan error karena properti age sudah dihapus

#Class Properties vs Object Properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#Modifying Class Properties
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

#Add New Properties
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25 #-> menambahkan properti age ke objek p1
p1.city = "Oslo" #-> menambahkan properti city ke objek p1

print(p1.name) #-> mencetak nilai properti name yang ada pada objek p1
print(p1.age) #-> mencetak nilai properti age yang ada pada objek p1
print(p1.city)#-> mencetak nilai properti city yang ada pada objek p1