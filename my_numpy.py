import numpy as np
import time
l=range(100)
print(l)

myarray=np.arange(1000)
print(myarray.size*myarray.itemsize)

a=np.array([[5,4,3],[7,8,9]])
print(a[1,1])

a = np.arange(12).reshape(3,4)
print(a)

for i in a:
    print (i)

SIZE = 100000000

l1=range(SIZE)
l2=range(SIZE)

a1=np.arange(SIZE)
a2=np.arange(SIZE)

#python list

start=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print(f'El tiempo total es {(time.time()-start)*1000}')

#numpy array
start=time.time()
result=a1+a2
print(f'El tiempo total es {(time.time()-start)*1000}')

print()
print()
print()

z=np.array([3,1,4])
arr = np.array([[4,3],[2,5],[6,8]])
print(z)
print(arr)
print(z.dot(arr)) #Multiplicacion matricial es distinta que z * arr hay que cumplir la regla de que #cols de "z" es igual al #rows de "arr", por eso esta operacion no funcionaria en viceversa
