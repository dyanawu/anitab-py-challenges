#!/usr/bin/python3

example_string = "The quick brown fox jumps over the lazy dog"

def remove_vowels(str_: str) -> str:
    return "".join(
        [i for i in str_
         if i.lower() not in ('a', 'e', 'i', 'o', 'u')]
    )

print("Example string:", example_string)
print("remove_vowels:", remove_vowels(example_string))
