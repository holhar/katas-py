"""
Detect Pangram (https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python)

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
def is_pangram(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    char_array = [*str(s).lower()]
    char_set = [*set(char_array)]
    count = 0
    for l in char_set:
        if (l in letters):
            count += 1
    return count == 26