#1 
name = 'Jayesh'
age = 24
easily readable
print('My name is %s and my age is %d' %(name,age))

#messy to read
print('My name is '+name+ ' and my age is '+str(age))

--------------------------------------------------
# 2 list Comprehention
list = [x**2 for x in range(0,4)]
print(list)

#alternate 
l1 = []
for i in range(0,4):
  l1.append(i**2)

#output --> [0, 1, 4, 9]

--------------------------------------------------
#3 string slicing
#str[start:end:step]
str = 'jAyesh'
print(str[::-2]) # -->heA
print(str[::-1]) #-->hseyAj
print(str[::])   #-->jAyesh

---------------------------------------------------





