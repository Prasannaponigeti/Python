    #Strings#
s='prasanna'
print(s[0])    #indexing#
print(s[1])
print(s[-1])


#slicing#
a= 'prasanna'
print(s[1:4])   #ras#
print(s[2:5])   #asa#
print(s[:3])     #pra#
print(s[:])      #prasanna#
print(s[:-2])    #prasan#
print(s[-3:])    #nna#
print(s[: :3])   #psn#
print(s[::-1])   #annasarp



#string concatenation by using '+'#
s1='love'
s2='you'
print(s1+" "+s2) #if we put quotes it gives some space- love you#
print(s1+s2)      #without quotes-loveyou#

s1="welcome"
s2="to"
s3="programming"
print(s1+" "+s2+" "+s3)

#repetation of strings using '*'#
string="prasanna"
print(string * 3)

#stringcase conversion#
String='PrasANNa'
print(string.lower())
print(string.upper())

#swapcase#
String='prasanna'
print(string.swapcase())

#title#
a="iam a codegnan student"
print(a.title())

#capitalize#
a="iam a codegnan student"
print(a.capitalize())


#removing white spaces by using strip(), lstrip(), rstrip()#
a='    prasanna    '
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a='$$$love$you$$$'
print(a.strip('$'))

#split#
string="I am a python programmer"
print(string.split())
print(string.split('a'))
print(string.split('x'))

#join#
lst=['I', 'am', 'a', 'python', 'programmer']
print(''.join(lst))
print(' '.join(lst))
print('_'.join(lst))
print('#'.join(lst))

#find,index(sub_string),replace#
string="I am a python programmer"
print(string.find('p'))
print(string.find('z'))
print(string.index('p'))

# String comparision#
a='acdf'
b='abdg'
print(a>b)
print(a<b)

a="Prasanna"
print(a.upper().replace('p','@'))

a="prasanna reddy"
print("_".join("prasanna reddy".split()))

l=list('codegnan')
print(l)
print("@".join(list('codegnan')))

#checking functions#
txt = "PrasannaX"
p = txt.isalpha()
print(p)

txt = "Prasanna10"
p = txt.isalpha()
print(p)

txt = "Prasanna10"
p = txt.isalnum()
print(p)

txt = "Prasanna 10"
p = txt.isalnum()
print(p)

txt = "1209"
a = txt.isdigit()
print(a)

txt = "1049@abs"
x = txt.isdigit()
print(x)
