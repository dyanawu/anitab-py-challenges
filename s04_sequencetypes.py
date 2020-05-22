#!/usr/bin/python3

l1 = [2, 3, 4, 5, 8, 4, 3, 5, 2, 1, 8, 8, 6, 3, 4, 5, 7, 9]
str1 = "hello python three"

# 1. get only unique elements in L1
uniq1 = set(l1)
print(f'Number of unique elements in list: {len(uniq1)}')

# 2. get only unique/odd elements from the results above
odd1 = filter(lambda i: i % 2 == 1, uniq1)
print(list(odd1))

# 3. replace text, convert to upper
str2 = str1.replace("three", "3")
str3 = str2.upper()
print(str3)

# 4. tuples are not changeable:
t1 = tuple(l1)

# e.g. they do not support item assignment (below code errors)
#t1[3] = 2

# they do not support insert/delete functions (all below code will error)
#t1.append(6)
#t1.insert(9, 2)
#t1.remove(2)
#t1.pop()
#t1.push(2)
#t1.clear()
