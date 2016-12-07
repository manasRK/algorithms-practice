'''
https://www.hackerrank.com/challenges/insertionsort1

Sorting 
One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.

Insertion Sort 
These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with an already sorted list.

Insert element into sorted list 
Given a sorted list with an unsorted number  in the rightmost cell, can you write some simple code to insert  into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of  to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until  can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with .

Input Format 
There will be two lines of input:

SIZE  - the size of the array
ARR - the unsorted array of integers

Output Format 
On each line, output the entire array every time an item is shifted in it.

'''
import sys

def insertion_sort(ar):
    if len(ar) == 1:
        print(' '.join(map(str, ar)))
        return(ar)
    else:
        x = ar[-1]
        for i in reversed(range(len(ar) - 1)):
            if x < ar[i]:
                ar[i + 1] = ar[i]
                print(' '.join(map(str, ar)))
                if i == 0:
                    ar[0] = x
                    print_list(ar)
                    break
            else:
                ar[i + 1] = x
                print_list(ar)
                break
        return(ar)
                
if __name__ == '__main__':
    s = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    
    inserti
