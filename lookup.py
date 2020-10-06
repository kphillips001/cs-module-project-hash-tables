import math
​
sqrt_table = {}
​
def compute_inverse_square(n):
    # fairly expensive
    result = 1 / math.sqrt(n)
    return result
​
# As engineers we only need to find the inverse square of numbers less than 1000
​
def build_lookup_table():
    for i in range(1, 1000):
        sqrt_table[i] = compute_inverse_square(i)
    
​
def faster_compute_square(n):
    return sqrt_table[n]
​
​
build_lookup_table()
print(sqrt_table)