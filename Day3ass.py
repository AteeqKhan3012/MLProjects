#List creation and manupulation
list1=[2,4,6,8,10]
list1.append(22)
print(list1)
list1.insert(3,12)
print(list1)
list1.remove(8)
print(list1)
list1.sort(reverse=True)
print(list1)

#Tuple indexing and slicing
tuple=('Python','Java','C++','Ruby','Javascript')
print(tuple[2])
print(tuple[1:4])
print(tuple[0:3])
#print(tuple[1]='Go')
#we can't change the element at index 1 because tuple is immutable 

#Set Ops
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issuperset(set2))

#Dictionary Creation and Access
sdscores={"Alice":85,"Bob":90,"Charlie":78}
print(sdscores)
sdscores.update({"David":92})
print(sdscores)
sdscores["Alice"]=88
print(sdscores)
print(sdscores.get("Bob"))

#Conversion btw datatypes
mylist=[1,2,3,4,5,5,3]
# print(mylist)
# myset=set(mylist)
#print(myset)
mytuple=tuple(mylist)
print(mytuple)
'''myset=list[1,2,3,4,5,5,3]
print(myset)

print(mylist)
print(mytuple)
print(myset)'''
