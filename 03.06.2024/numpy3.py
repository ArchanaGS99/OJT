import numpy as np
#create an orginal array
orginal_array = np.array([1,2,3,4,5,6])
print("orginal array:", orginal_array)

#create a view for the array
view_array = orginal_array.view()
print('view of the orginal array is :', view_array)

view_array[2] = 30
print('modified view of the array:', view_array)
print('original array after modifying the view:', orginal_array)

#create a copy of orginal array
copy_array = orginal_array.copy()
print('copy Array:', copy_array)

#modify element in copy array
copy_array[0] = 10
print('modified copy array:', copy_array)
print('orginal array after modifying the copy array:', orginal_array)