#PYTHON IF
a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

"""
a = 33
b = 200
if b > a:
print("b is greater than a") # akan erorr kalau gada indentasi
"""

#Multiple Statements in If Block
age = 18
if age >= 18:
  print("Kamu udah dewasa")
  print("Kamu bisa ikut pemilu")
  print("Udah legal")


#PYTHON ELIF
score = 70

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


#PYTHON ELSE
a = 33.5
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#SHORTHAND IF
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#LOGICAL OPERATOR
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


#NESTED IF
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#PASS STATEMENT
age = 17

if age > 18:
  pass 
else:
  print("Akses ditolak")