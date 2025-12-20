import numpy as np 
# print(np.__version__)
# my_list = [1,3,2,5]
# # my_list = my_list * 2
# array = np.array(my_list)
# array *= 2
# print(array)
# print(type(array))

array = np.array([[(1,3,5,8),(5,3,25,4)],
                  [(1,3,5,8),(5,3,25,4)], #every list or array of data should be equal and in sequence
                  [(1,3,5,8),(5,3,25," ")]  #else value error if no data then should add place holder
                  ])
print(array[2][0][3]) #this is chainindexing 
print(array[2,0,3]) #this is multidimensional indexing
# print(array.ndim)
# print(array)
# print()
# print(array.shape)