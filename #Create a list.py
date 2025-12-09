#Create a list
exampleList = ["friday", "saturday", "sunday"]
print()

#append adds item to the end of the list
exampleList.append("monday")
print(exampleList)
print()

#insert adds an item to a list using index numbers
exampleList.insert(0, "tuesday")
print(exampleList)
print()

#pop remove an item from the end of the list
exampleList.pop()
print(exampleList)
print()

#sorts a list in alphabetic order - string only
exampleList.sort()
print(exampleList)
print()

#remove the first occurrence of a specified value
exampleList.remove("saturday")
print(exampleList)
print()

#Revers sorts a list or strings or other data types in reverse order - not alphabetic order.
exampleList.reverse()
print(exampleList)
print()

#in keyword is used to check if a value is present in the list - True or False
print ("Friday" in exampleList)
print ("Tuesday" in exampleList)
print()

#len conts and prints the length or number of items in the list 
print(len(exampleList))
print()

#copy makes a copy of the list 
exampleListCopy = exampleList.copy()
print("exampleList")
print(exampleList)
print("exampleListCopy")
print(exampleListCopy)
print()

#chante an item in the list
exampleList[0] = "sun."
exampleList[1] = "Sat."
exampleList[2] = "Fri."
print(exampleListCopy)

#print only certain list items
print(exampleList[0:2])
print()

#clear removes all items from the list
exampleListCopy.clear()
print (exampleListCopy)

