#PY LIST
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"] #A list can contain different data types

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # list () constructor
print(thislist)


#ACCES ITEM LIST
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #2 batas bawah (include index 2), 5 batas atas (index 5 ga include)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#CHANGE LIST VALUE
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Item (menambahkan sebuah nilai setelah nilai yang disebutkan)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #"apple", "banana", "watermelon", "cherry" 
print(thislist)

#Add
#Append (Menambahkan item ke indeks terakhir)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Insert (Menambahkan item ke indeks yang ditentukan)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Extend(Menambahkan element dari list lain)
thislist = ["apple", "banana", "mango"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) 

#Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)