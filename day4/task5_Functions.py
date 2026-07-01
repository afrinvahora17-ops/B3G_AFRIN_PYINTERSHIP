from functools import reduce

num = [11,22,33,44,55,66,77]

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

max_num = reduce(find_max, num)

print("List of Number:", num)
print("Maximum Number in the List is:", max_num)