from typing import List # tuple, Set, etc...
"""
if we want to get the average number pass by sequence parameters
!!! we cannot do it as it shown below !!!
"""
def list_avg(sequence):
    return sum(sequence) / len(sequence)
    #hint if you passed the integer number to sequnce it will be shown an error

# print(list_avg(1234)) # return TypeError: 'int' object is not iterable
# print(list_avg(sequence=[1,2,3,4,5])) # it has to be grouped as a list

"""
Best option using type_hinting
"""
def list_avg_fixed(sequence: List) -> float:
    return sum(sequence) / len(sequence)

print(list_avg_fixed(12345))