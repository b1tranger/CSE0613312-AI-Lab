# Lab Report 2

## Title
Python Data Structures: Sequences, Arrays, and Dictionaries

## Theory
Python provides several built-in data structures essential for managing collections of data.
- **Tuples:** Immutable sequences of objects, meaning they cannot be modified after creation.
- **Lists:** Mutable sequences capable of holding elements of varying data types.
- **Dictionaries:** Key-value stores (hash maps) that allow for highly efficient data retrieval based on unique keys rather than numerical indices.
- **Slicing:** An operation to extract a subset of elements from sequences like strings, tuples, and lists using the syntax `[start:stop:step]`.

## Algorithms
- Data retrieval using index-based slicing.
- Hash map retrieval for dictionaries.

## Code Implementation
```python
arr = (10,20,30,40,50)
print(arr[0:5:1])

list_1 = [10,20,30,"CSE","BBA",[1,2,3]]
print(list_1)
print(list_1[0:5:1])
print(list_1[0:5:2])

my_dictionary = {'10':[10,2,5],'11':[50,60,7],'12':[1,2,3]}
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
```

## Output
```
(10, 20, 30, 40, 50)
[10, 20, 30, 'CSE', 'BBA', [1, 2, 3]]
[10, 20, 30, 'CSE', 'BBA']
[10, 30, 'BBA']
{'10': [10, 2, 5], '11': [50, 60, 7], '12': [1, 2, 3]}
dict_keys(['10', '11', '12'])
dict_values([[10, 2, 5], [50, 60, 7], [1, 2, 3]])
```

## Discussion
Slicing proved to be a powerful feature for list manipulation, especially with the use of the `step` parameter to skip elements. We observed that lists can store mixed data types, including other lists. For the dictionary, using `.keys()` and `.values()` methods easily extracted specific parts of the data, showing its utility in mapping specific identifiers to complex data like arrays.

## Conclusion
Understanding these core data structures (lists, tuples, dictionaries) and how to manipulate them is crucial for handling complex datasets and state representations in AI algorithms.
