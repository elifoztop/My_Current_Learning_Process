import numpy as np

m1=np.array([[2,3], [4,5]])
m2=np.array([[1,0],[0,1]])
o1=np.ones(1)
o2=np.ones(2)
o3=np.ones(2,2)

print(f"matrices1:\n",m1)
print(f"matrices2:\n",m2)
print(f"ones1=np.ones(1):\n",o1)
print(f"ones2=np.ones(2):\n",o2)
print(f"ones3=np.ones(2,2):\n",o3)

print(f"+:\n",m1+m2)
print(f"-:\n",m1-m2)
print(f"*:\n",m1*m2)
print(f"\nmatrices1 * 2 :\n",m1*2)
print(f"\nmatrices1 * ones1 :\n",m1*2)

