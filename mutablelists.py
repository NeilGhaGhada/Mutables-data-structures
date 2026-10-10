# list methods
# 1. Splits : converts string to list
# 2. append : takes everthing as string
# 3. extend : takes everthing as an object
# ***Note : if we given single object it conert in to list of letters of that give object
# 4. insert(index,value) : place the val at given index increase index of prev by 1
# ***Note : if index is out range and neg the it places at 0th and for pos it places at last
# ***** it add [...] if insert whole list at particular point that can also be remove by using remove()
# 5 count(var) : count the given var (only one var allowed)
# 6. index(var,start,end) : returns the index of give var
# ***Note : (neg val allowed in range) gives error if not present in list
# 7. remove : remove given element (only one var allowed) return error if not there
# 8. pop : pop last element by default other works as remove by give index (return error if empty)
# 9. reverse : reverse (returns no error if empty)
# 10. sort : by default it arranges in acesding if write reverse=True the works as reverse
#
#

#
#

"""
1. splits in list
s = "python is very easy to understand . . . ."
l1 = s.split(" ")
# print(l[89]) it throws an errow bc index is out of range
print(l1[:len(l1)-1])
print(l1[0:-1])



error case 1 :
l2 = []
l2[0] = True
print(l2)
# above l2 will throw an error bc l2 is empty

error case 2 :
l4 = ["dua","tay","ari","doja"]
l4.extend("billie","lady")
print(l4)
# bc bracket is needed



other case 1 :
below code will give you none l3.append("billie") [same apply for extend] return "None"
l3 = ["dua","tay","ari"]
l3 = l3.append("billie")
l3 = l3.extend("billie")
print(l3)



2. Append in list
(below same code differs if we use extend instead of append)
l3 = ["dua","tay","ari"]
l3.append("billie")
l3 = l3 + ["gaga"]
print(l3)

(below same code differs if we use extend instead of append)
l4 = ["dua","tay","ari","doja"]
l4.append(("billie","lady"))
l5 = ["olivia","zara","sabrina"]
l4.append(l5)
print(l4)



3. Extend in list
(below same code differs if we use append instead of extend)
l4 = ["dua","tay","ari","doja"]
l4.extend(("billie","lady"))
l5 = ["olivia","zara","sabrina"]
l4.extend(l4)
print(l4)

(below same code differs if we use append instead of extend)
l6 = ["dua","tay","ari"]
l6.extend("billie")
l6 = l6 + ["gaga"]
print(l6)



4. insert in list
l7 = [0,1,3,4,5,6,7]
l7.insert(2,"2")
print(l7)

l7 = [0,1,3,4,5,6,7]
l7.insert(-2,"5.n")
print(l7)

l7 = [0,1,3,4,5,6,7]
l7.insert(-8888,"5.n")
print(l7)

l7 = [0,1,3,4,5,6,7]
l7.insert(8888,"5.n")
print(l7)



5. count in list
l8 = [1,2,2,2,2,4,5,5,2,7,8,8,8,]
print(l8.count(2))



6. index in list
l9 = [1,2,3,3,3,4,4,4,5,6]
print(l9.index(5,-3,-1))
print(l9.index(4))
print(l9.index(3))



7. remove in list
l10 = [True,False,True,False,"False",None]
l10.remove(True)
print(l10)
l10.insert(88,l10)
print(l10)
l10.remove(l10)
print(l10)



8. pop in list
l11 = [True,False,True,False,"False",None]
print(l11.pop())
l12=[]
print(l12.pop())



9. reverse in list
l13=[1,2,4,5,True,"t",7,8,9,10,12,13,11]
l13.reverse()
print(l13)
l14=[True,False,'true','flase']
l15=l14
l14.reverse()
print(l14)
l14.reverse()
l14.reverse()
print("yes" if l15 == l14 else "no")



10. sort in list
"""

l16 = [0,1,3,45,66,55]
l16.sort()
l16.sort(reverse=True)
print(l16)

l17 = [0,1,2,3,4,]
l18 = l17
l17.sort()
print(l17)
print(l18)
print(l17 == l18.sort())
print("yes" if l18 == l17.sort(reverse=False) else "no")