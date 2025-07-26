         #dictionaries#

d={"name": "Prassu","age": 22,"school": "codegnan"}
print(d)

#dictionary values access by using keys#
print(d['name'])
print(d['school'])


#methods#-keys(),values(),items()#
d={"name": "Prassu","age": 22,"school": "codegnan"}
keys=d.keys()
values=d.values()
items=d.items()
print(keys)
print(values)
print(items)

#pop(key),item#
d={"name": "Prassu","age": 22,"school": "codegnan"}
val=d.pop('age')
print(val)
print(d)

item=d.popitem()
print(item)
print(d)


#accessing & updating the values#
d={"name": "Prassu","age": 22,"school": "codegnan"}
d['name']='laddu'
d['school']='institute'
print(d)


#getvalue,update(),clear()

d={"name": "Prassu","age": 22,"school": "codegnan"}
val=d.get('age')
print(val)
val=d.get('z',10)
print(val)

#update#
d1={'name':'prasanna','age': 22}
d2={'name':'bittu','school':'codegnan'}
d2.update(d1)
print(d1)
print(d2)
