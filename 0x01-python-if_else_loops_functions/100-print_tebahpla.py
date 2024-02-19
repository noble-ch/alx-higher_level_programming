#!/usr/bin/python3
def most_repeated_character(s):
    count = {}
    for i in range(len(s)):
        if isinstance(s[i], int):
            continue
        else:
            count.append(s[i])
            