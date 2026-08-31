
# int, float, bool
# str
# list - everything
# set - no dup , frozenset
# dict - key: value
# tuple

# tuple is like a list --> cannot be modified

t1 = ('a', 'b', 'c')
t2 = ('d', 'e', 'f')

print(t1, t2)
print(t1[0])
print(t2[0])
print(t2[-1])
print(t2[::-1])

t3 = (0, 1, 2, 3, 4, 5)
# Items at index 1, 2, 3
print(t3[1:4])

t = (1, 2, 2, 3, 2, 4, 2)
n = t.count(2)
print(t, 't.count(2)=', n)

t = ('cat', 'dog', 'bird', 'dog')
print(t, 't.index("dog")=', t.index('dog'))

a = (1, 2, 3)
b = (4, 6, 1)
result = a + b
print(a, '+', b, '=', result)

print(sorted(b, reverse=True))
print(tuple(sorted(b, reverse=True)))

t = ('apple', 'banana', 'cherry')
print(('apple', 'banana', 'cherry'), "banana in t?", 'banana' in t)
# → True
print(('apple', 'banana', 'cherry'), "mango not in t?", 'mango' not in t)
# → True

t = (3, 1, 4, 1, 5, 9)
# → 6
print(t, 'len(t)', len(t))
# → 1
print(t, 'min(t)', min(t))
# → 9
print(t, 'max(t)', max(t))
# → 23
print(t, 'sum(t)', sum(t))

# t[0] = 1  # ERROR
d = {(1, 2): ('a', 'b')}  # tuple could be used as key in dict

# [1,2,3]
# ('a', [1,2,3], 12)

data = ['poker app', 2.12]
data[1] = 2.14

print(d)
print(d[ (1,2) ])

a = [1,2]
tup = (a, 12)
print(tup)

a.clear()

print(tup)

# tup = ([3, 4], 12)
# d1 = {tup: 2}  # Error

print(tup)
tup[0].clear()
print(tup)

t = ('apple', 'banana', 'cherry')
for fruit in t:
    print(fruit, end=" ")
print()

####################
# 1 create a tuple with the numbers 10, 20, 30, 40
# 2 create a tuple with your name ,age city i.e. "danny", "cohen", 29, "tel aviv"
# 3 function get_positive that gets a tuple of numbers and return a new tuple
#   from only positive numbers
#   print(get_positive( (-5, 8, -2, 10, 0, 3) ) ) --> (8, 10, 3)
# 4 function get_z should return a new tuple containing only the words that start with the letter "z"
#   print(get_z( ("zebra", "apple", "zero", "banana", "zoo") ) ) --> ("zebra", "zero", "zoo")
# 5 function should return a new tuple where each element is the sum of the elements at the
#   same index in the two tuples
#   tuple1 = (10, 20, 30, 40)
#   tuple2 = (1,  2,  3,  4)
#   Output: (11, 22, 33, 44)

# function that gets tuple return new tuple only from even numbers
def get_even(tup):
    result = []
    for num in tup:
        if num % 2 == 0:
            result.append(num)
    result_tup = tuple(result)
    return result_tup

input_fun = (1, 2, 4, 7, 9, 10, 14)
print(input_fun)
print(get_even(input_fun))