import numpy as np
print("Create a 1D array of numbers from 0 to 9 hint: look up np.arange")
arr = np.arange(10)
print(arr)

print("Reshape it into a 2D array with 2 rows and 5 columns (hint: look up .reshape).")
arr = np.array([1,2,3,4,5,6,7,8,9,10])

New_arr = arr.reshape(2,5)
print(New_arr)

print("Print the new array, and print its .shape and .dtype.")
print(New_arr.shape)
print(New_arr.dtype)

print("Using the 2D array from Drill 1, extract and print the element in the 2nd row, 3rd column. (Remember: Python is zero-indexed, so this is index [1, 2]).")
print(New_arr[1][2])

print("Extract and print the entire first column. (Hint: use slicing like [:, 0]).")

print(New_arr[:,0])

print("Create an array of 10 random integers between 1 and 100 (hint: look up np.random.randint).")
array = np.random.randint(1,101,size=10)
print(array)

print("Write a condition to extract and print only the numbers greater than 50. (Hint: arr[arr > 50]).")

result = array[array>50]
print(result)

print("Create a 3x3 matrix of all ones (hint: np.ones).")
matrix = np.ones((3,3))
print(matrix)

print("Create a 1D array [10, 20, 30].")
arra = np.array([10,20,30])
print(arra)

print("Add the 1D array to the 3x3 matrix and print the result. Look at how the [10, 20, 30] automatically applied to every row. This is called broadcasting, and it is how neural networks add bias to batches of data.")
matrix = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
bias = np.array([10,20,30])

result = matrix + bias
print(matrix)
print(bias)
print(result)

print("Create two 2x2 matrices.")
arr1 = np.array([[1,2],
         [4,5]])

arr2 = np.array([[11,12],
         [14,15]])
print(arr1)
print(arr2)

print("Compute their dot product using the @ operator (e.g., result = matrix_a @ matrix_b).")
result1 = arr1 @ arr2
print(result1)