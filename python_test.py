import numpy as np
import time
import sys


#less memory
s = range(1000)
print("range:",s)

print("list_size:", sys.getsizeof(5)*len(s))
t = np.arange(1000)
print("numpy:", t.size*t.itemsize)

# time
size = 1000000

# declaring lists
list1 = range(size)
list2 = range(size)

# declaring arrays
array1 = np.arange(size)
array2 = np.arange(size)

# capturing time before the multiplication of Python lists
initialTime = time.time()

# multiplying  elements of both the lists and stored in another list
resultantList = [(a * b) for a, b in zip(list1, list2)]

# calculating execution time
print("Time taken by Lists to perform multiplication:",
      (time.time() - initialTime),
      "seconds")

# capturing time before the multiplication of Numpy arrays
initialTime = time.time()

# multiplying  elements of both the Numpy arrays and stored in another Numpy array
resultantArray = array1 * array2

# calculating execution time
print("Time taken by NumPy Arrays to perform multiplication:",
      (time.time() - initialTime),
      "seconds")


z = np.array([1,2,3,5,0])
print(z.max())
print(z.min())
print(z.sum())


a = np.array([(1,2,3,6),(4,5,6,8)])
print(a.sum(axis=1))


a = np.array([(1,2,3,6),(4,5,6,8),(9,7,4,2)])
print(a.ndim)
print(a.size)
print(a.shape)
#Reshape
b = a.reshape(4,3)
print(b)
#slicing
print(a[0,2])
print(a[0])
print(a[0:1,3])

print("1D")
c = np.array([1,2,3])
print(c)

q = np.array([(1,2,3,4),(5,6,7,8),(8,9,0,1)])
print(q)
print(type(q))
print(q.ndim)
print(q.size)
print(q.shape)
reshapes = q.reshape(4,3)
print(reshapes)
print(reshapes.shape)
print("slcing")

a = np.array([(1,2,3,6),(4,5,6,8),(9,7,4,2)])

#slicing
print(a[0,2])
print(a[0:2,0:3])
print(a[0])
print(a[0:1,3])
print(a.max())
print(a.min())
print(a.sum())
print(a[0])
print("test")
print(a[0].sum())

