import numpy as np

m1=np.array([[2,3], [4,5]])
m2=np.array([[1,0],[0,1]])
o1=np.ones(1)
o2=np.ones(2)
o3=np.ones((2,2))
o4=np.ones((1,2))
o5=np.ones((2,1))

print(f"\n#MATRIXS")
print(f"matrices1:\n",m1)
print(f"matrices2:\n",m2)
print(f"ones1=np.ones(1):\n",o1)
print(f"ones2=np.ones(2):\n",o2)
print(f"ones3=np.ones(2,2):\n",o3)
print(f"ones4=np.ones((1,2)):\n",o4)
print(f"ones5=np.ones((1,2)):\n",o5)

print(f"\n#OPERATION")
print(f"+:\n",m1+m2)
print(f"-:\n",m1-m2)
print(f"*:\n",m1*m2)
print(f"\nmatrices1 * 2 :\n",m1*2)
print(f"\nmatrices1 * ones1 :\n",m1*o1)
print(f"\nmatrices1 * ones2 :\n",m1*o2)
print(f"\nmatrices1 * ones3 :\n",m1*o3)
print(f"\nmatrices1 * ones4 :\n",m1*o4)
print(f"\nmatrices1 * ones5 :\n",m1*o5)

print(f"\n#INDEX")
my_matrix=np.array([[1,2,3],[4,5,6]])
print(f"((row=2,column=3)) => np.ones((2,3)):\n",np.ones((2,3)))
print(f"\nmy_matrix() == [[1,2,3],[4,5,6]]:\n",my_matrix)
print(f"\nmy_matrix[0][0]:",my_matrix[0][0])
print(f"my_matrix[0][1]:",my_matrix[0][1])
print(f"my_matrix[1][2]:",my_matrix[1][2])
print(f"my_matrix[1]:",my_matrix[1])

print(f"\n#DOT PROCUCT")
m_1=np.array([1,2,3])
m_2=np.array([[1,2],[10,20],[100,200]])
print(f"m1(row=1,column=3):\n",m_1)
print(f"\nm2:(row=3,column=2):\n",m_2)
print(f"\nm1.dot(m2):\n",m_1.dot(m_2))


print(f"\n#FUNCTIONS")

print(f"my_matrix>2:\n",my_matrix>2)
print(f"\nmy_matrix[my_matrix>2]:\n",my_matrix[my_matrix>2])

print(f"\nmy_matrix.shape():\n",my_matrix.shape)
print(f"my_matrix.transpose() OR my_matrix.T:\n",my_matrix.transpose())
print(f"\nmy_matrix.reshape((row=1,column=6)):\n",my_matrix.reshape((1,6)))

#EXTRA
#z_score=(matrix-matrix.mean(AVG))/np.std(matrix)
