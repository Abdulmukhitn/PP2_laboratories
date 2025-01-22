print(10 > 9)
print(10 == 9)
print(10 < 9)




a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))



bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))




def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")



print((6 + 3) - (6 + 3))


mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)




thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)




thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)




mytuple = ("apple", "banana", "cherry")



thistuple = ("apple", "banana", "cherry")
print(thistuple[1])



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


myset = {"apple", "banana", "cherry"}



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)



thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)



thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)





thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



