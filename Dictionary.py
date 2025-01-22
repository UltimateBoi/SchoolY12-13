#  Write a function that takes a dictionary and a value as input and returns True if the value is present in the dictionary, otherwise False.

my_dict = {'a': 1, 'b': 2, 'c': 3}
value_to_check = 2


def valueInDict(dictionary, value):
    return value in dictionary.values() # values() returns view object from a dictionary

print(valueInDict(my_dict, value_to_check))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key in thisdict:
    print(key.title()+ ":", thisdict[key])

# Write a function that takes a dictionary and a key as input and returns True if the key is present in the dictionary, otherwise False.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

def keyInDict(dictionary, key):
  return key in dictionary

print(keyInDict(my_dict, key_to_check))

# Write a function that takes two dictionaries as input and returns a new dictionary containing key-value pairs from both dictionaries. If a key is present in both dictionaries, use the value from the second dictionary.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

def mergeDictionaries(dict1, dict2):
  merged_dict = dict1.copy() # Start with dict1's keys and values
  merged_dict.update(dict2) # Update with dict2's keys and values, overwriting duplicates from dict1
  return merged_dict

merged_dict = mergeDictionaries(dict1, dict2)
print(merged_dict)

# Write a function that takes a dictionary as input and returns the number of key-value pairs in the dictionary. 

my_dict = {'a': 1, 'b': 2, 'c': 3}
def countKeyValuePairs(dictionary):
  return len(dictionary)

print(countKeyValuePairs(my_dict))

# Write a function that takes a dictionary and a key as input and returns the value associated with that key. If the key is not present, return None.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_access = 'b'

def getValue(dictionary, key):
  return dictionary.get(key) # get() returns the value of the specified key

print(getValue(my_dict, key_to_access))

# Write a function that takes a dictionary as input and returns a list containing all the values in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}

def getAllValues(dictionary):
  return list(dictionary.values()) # values() returns a list of all the values in the dictionary and the list() function converts it into a list

print(getAllValues(my_dict))

# Write a function that takes a dictionary, a key, and a new value as input and updates the value associated with that key in the dictionary. 

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_update = 'b'
new_value = 5

def updateValue(dictionary, key, value): # Function to update the value associated with the key
  dictionary[key] = value # Update the value associated with the key

updateValue(my_dict, key_to_update, new_value) # Update the value associated with the key 'b' to 5
print(my_dict)

# Write a function that takes a dictionary and a key as input and removes the key-value pair from the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

def removeKey(dictionary, key):
  if key in dictionary:
    del dictionary[key] # Remove the key-value pair from the dictionary if the key is present

removeKey(my_dict, key_to_remove)
print(my_dict)

# Write a function that takes a dictionary, a key, and a value as input and adds the key-value pair to the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4
def addKeyValuePair(dictionary, key, value):
  dictionary[key] = value # Add the key-value pair to the dictionary

addKeyValuePair(my_dict, new_key, new_value)
print(my_dict)

# Write a function that takes a dictionary as input and returns a list containing all the keys in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
def getAllKeys(dictionary):
  return list(dictionary.keys()) # keys() returns a list of all the keys in the dictionary and the list() function converts it into a list

print(getAllKeys(my_dict))

