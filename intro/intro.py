print("Hello World")
a="test"
a=a.replace("e","k")
print(a)

b="A*B*C*E"
b.split("*")
print(b)

# output
# ['A', 'B', 'C', 'E']

b="A*B*C*E"
b=b.split("*")
print(b)

#output
#['A*B*', '*E']

# s1="hello"
# A=[]
# B=[]
# for i in s1:
#     A.append(i)
# for i in range(1,3):
#     B.append(A[i])
    
# print(B)

#exercise
# liste=[17,38,10,25,72]

# liste.sort()
# print(liste)

# liste.append(12)
# print(liste)

# liste.reverse()
# print(liste)

# r=liste.index(17)
# print(r)

# liste.remove(38)
# print(liste)

# print(liste[2:4])

# print(liste[:3])

# print(liste[3::])

# print(liste[-1])




# #exercise 2


# d={'nom':'depuis','prenom':'Jacque','age':30}

# d['prenom']='Jaques'
# print(d)

# d['pays']='France'
# print(d)

# #methode1
# keys={}
# for i in d:
#     keys=d.keys()
# print(keys)

# #methode 2
# print(d.keys())

# #methode1
# values={}
# for i in d:
#     values=d.values()
# print(values)

# #methode 2
# print(d.values())

# del d['age']
# print(d)

#exercise 3

liste=[15,18,22,90,100,101]
def maximum(l):
    max=l[0]
    for i in l:
        if (i>max):
            max=i
    return max

print(maximum(liste))

def minimun(l):
    max=l[0]
    for i in l:
        if (i<max):
            max=i
    return max

print(minimun(liste))

def somme(l):
    som=0
    for i in l:
        som+=i
    return som

print(somme(liste))

def moyenne(l):
    moy=somme(l)/len(l)
    return moy

print(moyenne(liste))



             



