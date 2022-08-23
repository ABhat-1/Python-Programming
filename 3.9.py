set1=[1,2,1,3,0,0,4,7,8,6]
set2=[5,5,7,8,7,9,6,1,1,2]
s1=set(set1)
s2=set(set2)
print(s1)
print(s2)
print(s1-s2)
print(s1&s2)#intersection
print(s1|s2)#union
print(s1^s2)#numbers from s1 or s2 but not both, symmetric difference
