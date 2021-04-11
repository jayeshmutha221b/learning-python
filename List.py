l1 = ['jayesh','Mutha']
l1.append('P')
print(l1)

#count(element) --> finds count of element in list
print('Count of Jayesh in l1 :' ,l1.count('jayesh'))

#extend(list) --> Joins two list
l2 = ['MS','CS','Python','MS']
l1.extend(l2)
print(l1)

#index(element,start_index,end_index) --> finds index of first occurance of element {start_index,end_index are optional} 
print('Index of elment MS:',l1.index('MS',3,6))

#pop(index) --> removes and returns element at given index , if index not provided returns and removes last element in list
print(l1.pop(2))
print('element at index 2 poped',l1)

#remove(element) --> removes first occurance of element
print(l1.remove('MS')) #returns none
print('item removed',l1)

#reverese 
l1.reverse()
print('reveres',l1)

#sort
l1.sort()
print('sorted list', l1)

#clear
l1.clear()
print('list after clear()', l1)


#Output :
#['jayesh', 'Mutha', 'P']
#Count of Jayesh in l1 : 1
#['jayesh', 'Mutha', 'P', 'MS', 'CS', 'Python', 'MS']
#Index of elment MS: 3
#P
#element at index 2 poped ['jayesh', 'Mutha', 'MS', 'CS', 'Python', 'MS']
#None
#item removed ['jayesh', 'Mutha', 'CS', 'Python', 'MS']
#reveres ['MS', 'Python', 'CS', 'Mutha', 'jayesh']
#sorted list ['CS', 'MS', 'Mutha', 'Python', 'jayesh']
#list after clear() []
