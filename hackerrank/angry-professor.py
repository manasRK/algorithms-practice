"""
https://www.hackerrank.com/challenges/angry-professor

BRIEF:

A Discrete Mathematics professor has a class of N students. Frustrated with their lack of discipline, 
he decides to cancel class if fewer than K students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.
"""

t = int(raw_input().strip())

for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    present = sum(1 for i in a if i<=0)
    if present>=k:
        print "NO"
    else:
        print "YES"
        
