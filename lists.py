     #LISTS#
#Indexed based#
lst=[1,2,3,'hi','a','b',23.5,1,2]
print(lst[0])
print(lst[-1])
lst[0]=100
print(lst)

#creating empty list#
lst=[]
lst1=list()
print(type(lst))
print(type(lst1))


#string to list type case conversion#
a='prasanna'
l=list(a)
print(type(a),type(l))
print(l)


#list concatenation#
l1=[1,2,3]
l2=['a','b','c']
print(l1+l2)


#reading list of integers from user#
#lst=list(map(int,input().split()))
#print(lst)

#list repetation#
l1=['prasanna']
print(l1*4)

#list methods#
l=[1,2,3,5.5,'a','b',1,2,3]
l.append(100)
print(l)
l.extend([200,300])
print(l)
l.insert(4,'codegnan')
print(l)

#remove(),pop(),clear(),del()#
l=[1,2,3,5.5,'prasanna','a','b',1,2,3]
print("original list:",l)
l.remove(3)
print(l)
l.pop()
print(l)
l.pop(2)
print(l)
del l[0]
del l[2:5]
print(l)

#min(),max(),sum()
l=[1,2,15,7,23,32,5]
min_val=min(l)
max_val=max(l)
sum_list=sum(l)
print("min value in the list:",min_val)
print("max value in the list:",max_val)
print("sum value in the list:",sum_list)

#sort(),reverse()#
a=[2,34,45,29,99,5,87]
a.sort()
print(a)

a=[2,34,45,29,99,5,87]
a.sort(reverse=True)
print(a)


a=[2,34,45,29,99,5,87]
b=a.copy()
print(b)

#count(),index()
l=[1,3,4,5,50,67,84,532,97,34,3,2,3]
count_2=l.count(67)
print(count_2)
ind=l.index(84)
print(ind)

l=[1,3,4,5,50,67,84,532,97,34,3,2,3]
length=len(l)
print(length)


