# SETS are unordered and unique collection of items, no repetition the same elements is seen in Set

fruits = {"apple","banana", 23}

print(fruits)

print(type(fruits))

fruits.add(7.00)
fruits.add(True)
fruits.add("TAmma")
fruits.add(2341)

print(fruits)

fruits.remove(7.00)
print(fruits)

#The discard() method in Python removes a specified element from a set if it exists. 
# Unlike remove(), it does not raise an error if the element is absent.

numbers = {1, 2, 3, 4, 5}

numbers.discard(3)  # Removes 3 from the set
print(numbers)  # Output: {1, 2, 4, 5}

# numbers.remove(10) this will throw an error
numbers.discard(10)  # No error, even though 10 is not in the set
print(numbers)  # Output: {1, 2, 4, 5}

numbers.pop()
print(numbers) # removes random element from the set
