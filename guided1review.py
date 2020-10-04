class HashTable:

  def __init__(self, capacity):
    self.hash_array = [None] * capacity
  # Need to array to store items (some use self.storage)
  # A hash function needs to take a string and return a single number
  # It must be deterministic (i.e the same result every time given the same input)
  
  def hash_fn(self, s): #O(n) where n is length of string
    # convert the string to a UTF-8 (Unicode) representation
    encoded_string = s.encode() # 0(1)
    result = 0
    # every character is now a number based off UTF-8 rules
    for byte_char in encoded_string:
      # simply add the numbers up to get one single new number
      result += byte_char
    
    return result

  def hash_index(self, key):
    hash_value=self.hash_fn(key)
    index = hash_value % len(self.hash_array)
    return index
    # To insert a key an value to this hash_table
    # - hash the key to convert it to a number
    # - take that number and MOD it by the size of hash_table
    # - insert the VALUE into the index given by the MOD operation
  def put(self, key, value):
    index = self.hash_index(key)
    self.hash_array[index] = (key, value)

  # To retrieve a value given a specific key from a hash_table
  # - hash the key to convert it to a number
  # - use MOD to find index within the underlying array
  # - use this new index to find the value in the array
  # get function
  def get(self, key):
    index = self.hash_index(key)
    return self.hash_array[index]

table = HashTable(4)
table.put('banana', 'banana is yellow')
print(table.hash_array)