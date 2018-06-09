#Q1
a=(1,4,5,6,'a','b')
print(a)
print(len(a))

#Q2

b = [19,28,37]
print(max(b))
print(min(b))

#Q3
c=[4*5*6]
print(c)

#Q4(a)
s1 = set([1,2,3,4,5,6,9])
s2 = set((2,9,7))
s3 = s2-s1
s4 = s1-s2
print(s3)
print(s4)
#(b)
a1 = set((1,2,3,4,5,6,7,8))
a2 = set((2,4,5,6))
a3=a1>=a2
print("a1 is super set of a2")
print(a3)
a4=a1<=a2
print("a1 is subset of a2")
#(c)
a5 = a1&a2
print(a5)

#Q5
a=input("enter the name")
b=input("enter marks")
d={'name':a,'marks':b}
print(d)

#Q6

#Q7

l=('mississippi')
a=l.count('m')
b=l.count('i')
c=l.count('s')
d=l.count('p')
d={'number of m':a,'number of i':b,'number of s':c,'number of p':d}
print(d)
