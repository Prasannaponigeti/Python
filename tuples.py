      #Tuples#
t=(1,2,3,'a','b','prassu',[4,5,6])
print(t)


#index based& slicing#
t=(1,2,'prassu',[2,4,5],1.5)
print(t[4])
print(t[-3])
print(t[-1])
print(t[2:-3:1])
print(t[-2:4:1])
print(t[-2:4:-1])
print(t[3:100])


#empty tuple#
t1=()
t2=tuple()
#tuple with multiple values#
t3=(1,2,3.5,"prassu")
print(t3)
#tuple with single value#
t4=(43, )
print(t4)
print(type(t1),type(t2),type(t3),type(t4))


#tuple concatenation using+#
t1=(2,3,"prassu")
t2=(1.5,4,"codegnan")
print(t1+t2)


#tuple repetation using *#
t1=(2,3,"prassu")
print(t1*2)

#tuple methods#
t=(1,2,3,'a','b',"love you",[1,3,5,6],2,5,1.5)
ind=t.index('a')
count_1=t.count(2)
print(ind)
print(count_1)

#sorted#
t=(3,4,78,9,6,43,87)
new_t=sorted(t,reverse=True)
print(new_t)


#built in functions#
#min(),max(),sum(),length()#
p=(1,3,4,6,89,96,5)
min_val=min(p)
max_val=max(p)
sum_tuple=sum(t)
length= len(p)
print(min_val, max_val, sum_tuple, length)
