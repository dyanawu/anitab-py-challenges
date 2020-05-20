#!/usr/bin/python

str_list = set(input().split())
ch = input()

words_count = zip(str_list, [word.count(ch) for word in str_list])

output = []
for (word, count) in words_count:
    for x in range(count):
        output.append(word)

print(output)
