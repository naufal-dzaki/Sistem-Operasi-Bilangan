import numpy as np

matrix1 = np.array([[5,9,4,2,4,8],
                    [7,5,3,1,1,4],
                    [7,8,2,0,1,7],
                    [5,6,9,3,4,4],
                    [0,9,7,2,3,7]])

matrix2 = np.array([[1,2,9,0,4,7],
                    [7,7,1,2,7,3],
                    [9,2,2,1,1,7],
                    [3,3,7,9,0,9],
                    [1,0,8,7,8,9]])


result = np.add(matrix1, matrix2)
print(result)