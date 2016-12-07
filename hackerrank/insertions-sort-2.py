'''
https://www.hackerrank.com/challenges/insertionsort2

In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an element with just the first element - that is already "sorted" since there's nothing to its left that is smaller.

In this challenge, don't print every time you move an element. Instead, print the array after each iteration of the insertion-sort, i.e., whenever the next element is placed at its correct position.

Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

Input Format 
There will be two lines of input:

S - the size of the array
ar - a list of numbers that makes up the array

Output Format 
On each line, output the entire array at every iteration.
'''

def insertionSort(ar):
    """The method insertionSort takes in one parameter: an unsorted array."""
    for i in range(1, len(ar), 1):
        k = ar[i]
        ix = i-1
        while ix>0 and ar[ix]>k:
            ar[ix+1] = ar[ix]
            ix-=1
        ar[ix+1]=k
    print ' '.join(map(str,ar))


def insertionSort(ar):
    if len(ar) == 1:
        print ' '.join(map(str,ar))
    else:
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                else:
                    break
            print ' '.join(map(str,ar))


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
