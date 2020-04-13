from copy import copy, deepcopy

# LIST does not contain any real objects, it contains references to the objects


x1 = [1, 2, 3, 4, 5]
x2 = x1  # The code does not create new list, it is just another reference to the same list
x1[0] = 10  # we just make reference to another object 10 here, we do not put change value of any object
x2[0] = 100  # here is the same
print(x1, x2)  # Result: [100, 2, 3, 4, 5] [100, 2, 3, 4, 5]


# Here we create a new object list, so if we change reference in x4 it will not affect reference in x3
x3 = [1, 2, 3, 4, 5]
x4 = copy(x3)
x3[0] = 10
x4[0] = 100
print(x3, x4)  # Result: [10, 2, 3, 4, 5] [100, 2, 3, 4, 5]


# GREAT difference between copy and deepcopy if list contains object which contains references like list

x5 = [1, [1, 2], 5]
x6 = copy(x5)

x5[0] = 0
x6[0] = 100

x5[1][0] = 800
x6[1][0] = 900

print(x5, x6)  # Result: [0, [900, 2], 5] [100, [900, 2], 5]

# Pay attention that x5[1][0] = x6[1][0], this is because x5[1] and x6[1] are actually references to the the same list


# In case of deepcopy:

x7 = [1, [1, 2], 5]
x8 = deepcopy(x7)

x7[0] = 0
x8[0] = 100

x7[1][0] = 800
x8[1][0] = 900

print(x7, x8)  # Result: [0, [800, 2], 5] [100, [900, 2], 5]

# Two different lists were actually created that is why if we change reference in on list to another object,
# it will not affect references in another list in any way.
