import numpy as np

print("\nARRAY ENTRANCE")
my_list = [1, 2, 3, 4, 5]
my_array=np.array(my_list)
print(f"MY ARRAY: {my_array}")
print(type(my_array))
print(f"list(range(0,10)):{list(range(0,10))}")
print(f"np.arange(0,10):{np.arange(0,10)}")
print(f"np.random.randint(1,100,5):{np.random.randint(1,100,5)}")
print(f"np.random.randn(4):{np.random.randn(4)}")
print(f"\nnp.random.randn(4,4):{np.random.randn(4,4)}")



print("\nARRAY TYPE")
one_array=np.ones(5)
print(one_array)
zero_array=np.zeros(5)
print(zero_array)
random_array=np.random.random(5)
print(random_array)

print("\nARRAY ARITHMETIC")
a=np.array([1,2])
b=np.array([3,4])
print(f"Array1:{a}")
print(f"Array2:{b}")
print(f"+:{a+b}")
print(f"-:{a-b}")
print(f"*:{a*b}")
print(f"/:{np.round(a/b,2)}") #digit show set
print(f"//:{a//b}")
print(f"\nArray1 * 1.6 :{a*1.6}")
print(f"ERORR== Array1 * np.array[1,2,3]")

print("\nARRAY INDEXING")
print(f"MY ARRAY: {my_array}")
print(f"my_array[0]: {my_array[0]}")
print(f"my_array[2]: {my_array[2]}")
print(f"my_array[0:2]: {my_array[0:2]}")
print(f"my_array[2:]: {my_array[2:]}")
print(f"my_array[::-1]: {my_array[::-1]}")
print(f"my_array[0:2:2]: {my_array[0:2:2]}")

print("\nARRAY FUNCS")
print(f"MY ARRAY: {my_array}")
print(f"MAX:{my_array.max()}")
print(f"MIN:{my_array.min()}")
print(f"SUM:{my_array.sum()}")
print(f"AVG(mean):{my_array.mean()}")





