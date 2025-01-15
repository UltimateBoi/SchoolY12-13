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
  merged_dict = dict1.copy()  # Start with dict1's keys and values
  merged_dict.update(dict2)   # Update with dict2's keys and values, overwriting duplicates from dict1
  return merged_dict

merged_dict = mergeDictionaries(dict1, dict2)
print(merged_dict)