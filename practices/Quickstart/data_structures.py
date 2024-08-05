print("Data Structures")

# Lists
my_lists= [1,2,3,4]
print(my_lists)

my_lists = [1,2,3,4, "test", "test2", False, True,]

my_lists = [[1,2,4], [False, True], []]

print(len(my_lists))


# Sets
my_set = {1,2,3,4}
print(my_set)

print(type(my_set))

print(len(my_set))

print([1,2] == [2,1])

print({1,2} == {2,1})

# Tuples

my_tuple = (1,2,3,4)

print(len(my_tuple))
print(my_tuple.append(5))

print((1,2) == (2,1))

my_lists.append(66)

# you can't modify a tuple
# why we use the tuple? because it's faster than a list

# Dictionaries
my_dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York" 
}

print(my_dictionary["name"])
