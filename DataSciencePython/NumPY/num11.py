import numpy as np 
# print(np.__version__)
# my_list = [1,3,2,5]
# # my_list = my_list * 2
# array = np.array(my_list)
# array *= 2
# print(array)
# print(type(array))

# array = np.array([[(1,3,5,8),(5,3,25,4)],
#                   [(1,3,5,8),(5,3,25,4)], #every list or array of data should be equal and in sequence
#                   [(1,3,5,8),(5,3,25," ")]  #else value error if no data then should add place holder
#                   ])

# print(array.ndim)
# print(array)
# print()
# print(array.shape)  
# print(array[2][0][3]) #this is chainindexing 
# print(array[2,0,3]) #this is multidimensional indexing

# number = array[1,1,2] + array[0,1,3] + array[2,1,3] + array[0,0,0] # addition or can be called concatination
# print(number)

#slicing in numpy array 

# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])

# print(array)
# print(array.ndim)

#array[slice expression] array slicing is same as string slicing 
# array[start:end:step]

# print(array[::-1]) # reversing an array in numpy  this is row selection 

#column selection in nparray 

# print(array[:,0]) #prints all the column in a row 
# print(array[:,-1]) #can also do in negative 
# print(array[:,2])
# print(array[:,3])

# print(array[:,0:4:3]) # step slicing in column 
# print(array[:,0:4:2])

# print(array[:2, :2])
# print(array[1:,2:])

# print(array[1:3,1:3])
 

# Scalar Arithmetic

# array = np.array([1,2,3])
# print(array ** 2) # simple arithmetic work can be done simply like this in an array of numpy 
# print(array - 5)
# print(array + 100)
# print(array / 5)

# Vectorized math functions -> vector = single dimension and scalar = single value

# array = np.array([4.5,9.3,5.8])
# np.set_printoptions(precision=2, floatmode='fixed') # python numpy function for setting precision while printing 
# print(np.sqrt(array)) # numpy also has many functions like math in C for various operations
# print(np.round(array)) # this gives 4. cause np tries to make the value compact and short 
# print(np.pi)

#EXERCISE   
radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# Element-wise arithmetic 
