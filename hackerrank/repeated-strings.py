"""
https://www.hackerrank.com/challenges/repeated-string

Lilah has a string, "a" , of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first  letters of Lilah's infinite string.
"""


s = raw_input().strip()
n = long(raw_input().strip())


print s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
