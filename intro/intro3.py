import typing_extensions


L=[1,2,3]
def pro(a):
    return a*2

a=list(map(pro,L))
#print(a)

M=["anis","Ibrahim","steve"]

def longeur(M):
    A=[]
    for i in M:
        A.append(len(i))
    return(A)

print(longeur(M))
# a = list(map())
def leng(a):
    return len(a)
#print(list(map(leng,M)))


A=[
    {"name":"ibrahim", "id":1},
    {"name":"anis","id":2},
    {"name":"ibrahim", "id":3},
    {"name":"ibrahim", "id":4}
]

def d(a):
    if(a['id']==3):
        del(a['id'])
        a['name']='test'
    return a

#print(list(map(d,A)))





def somme(a):
    return a*2

l=lambda a:a*2
#print(l(2))

L=[1000,5000,6000]

s=lambda l:l*3200

print(list(map(s,L)))