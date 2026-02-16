#PYTHON __init__() METHOD
#Python __init__Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name) # merujuk kepada self.name = name
print(p1.age) # merujuk kepada self.age = age

#Tanpa metode __init__(), properti atau atribut pada objek harus diatur secara manual
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

p2 = Person()
p2.name = "Emil"
p2.age = 36

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

#Dengan __init__ method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)
p2 = Person("Emil", 36)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

#Default Values in __init__()
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#Multiple Parameters
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)