#Nested Data Structures
studs=[{'name':'Alice','age':20,'grade':'A'},{'name':'Bob','age':22,'grade':'B'}]
print(studs)
studs.append([{'name':'Tenson','age':23,'grade':'C'}])
print(studs)
studs[1]['grade']='A'
print(studs)
studs.remove(studs[0])
print(studs)

