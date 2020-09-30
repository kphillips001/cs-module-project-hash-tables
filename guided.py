# Hashing function has to have two things
# A hash function needs to take a string and return a single number
# It must be deterministic (i.e the same result every time given the same input)
 
def hash_fn(s): #O(n) where n is length of string
  print(s)
  # convert the string to a UTF-8 (Unicode) representation
  encoded_string = s.encode() # 0(1)
  # print(encoded_string)
  
  #adds the totals of each char
  result = 0
  # every character is now a number based off UTF-8 rules
  for byte_char in encoded_string:
    # simply add the numbers up to get one single new number
    result += byte_char
  
  return result

print(hash_fn("banana")) # => 609
print(hash_fn("apple")) # => 530

# Lets map the result of hash_fn to an index in some array
# we create an array of size 8
hash_array = [None] * 8
# we can use modulo to bind the number from hash_fn to 0 -> length of the array

# Store banana inside hash_array
hash_value = hash_fn("banana") # 609
index = hash_value % len(hash_array)#gives us modulo of 1
hash_array[index] = ("banana", "banana is yellow")  
# banana is the key
# banana is yellow is the value

# Store apple inside hash_array
hash_value = hash_fn("apple") # 530
index = hash_value % len(hash_array)#gives us modulo of 2
hash_array[index] = ("apple", "apple is green")  

print(hash_array)
# Look up Banana in hash_array
# Get the index value of Banana
hash_value = hash_fn("banana") # 609 #O(N) but N === length of string is very small compared to Array
index = hash_value % len(hash_array)#gives us modulo of 1 #O(1)

print(hash_array[index]) #O(1)

# Hash function + An Array == Hash_table

# To insert a key an value to this hash_table
# - hash the key to convert it to a number
# - take that number and MOD it by the size of hash_table
# - insert the VALUE into the index given by the MOD operation
# insert function
def insert_to_table(key, value):
  hash_value=hash_fn(key)
  index = hash_value % len(hash_array)
  hash_array[index] = (key, value)

# To retrieve a value given a specific key from a hash_table
# - hash the key to convert it to a number
# - use MOD to find index within the underlying array
# - use this new index to find the value in the array
# get function
def get_from_hash_table(key):
  hash_value = hash_fn('apple')
  index = hash_value % len(hash_array) #convert the number into a new number between 0 -len(array)
  return hash_array[index]