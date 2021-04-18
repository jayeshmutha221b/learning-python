tup = (1,2,3,[1,2,3,4])
tup[0] = 2
print(tup)

#output --> Error
#TypeError: 'tuple' object does not support item assignment


tup = (1,2,3,[1,2,3,4])
tup[3][0] = 5
print(tup)

#output --> list within tuple is mutable
#(1, 2, 3, [5, 2, 3, 4])

tup = (1,2,3,[1,2,3,4])
tup[3].append(5) 
print(tup)


#output --> since list within tuple is mutable, we can even add elements :)
(1, 2, 3, [1, 2, 3, 4, 5])

#Remember two things. First, immutability is not magic -- it is merely the absence of mutating methods. 
#Second, objects don't know what variables or containers refer to them -- they only know the reference count.
