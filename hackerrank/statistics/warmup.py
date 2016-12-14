"""
https://www.hackerrank.com/challenges/stat-warmup

BRIEF:
Calculate mean, median, mode, standard deviation and 95% CI given an array.
"""
# performing integer division, fixed in Python3, but do float/int in 2.7

def mean(array):
    return float(sum(array))/len(array)

def median(array):
    array = sorted(array)
    if len(array)%2==0:
        middle = array[len(array)/2 -1]
        next_to_middle = array[len(array)/2]
        median = round(float(middle+next_to_middle)/2, 1)
    else:
        middle = (len(array)-1)/2 -1
        median = array[middle]
    return median

def mode(array):
    most = max(list(map(array.count, array)))
    return min(list(set(filter(lambda x: array.count(x) == most, array))))

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    pvar = ss/n # the population variance
    return round(pvar**0.5, 1)

def ci(array):
    n = len(array)
    mean_ = mean(array)
    sdev = pstdev(array)
    lower = round(mean_ - (1.96*(sdev/n**(1.0/2))), 1) # 1.96 for 95% CI
    upper = round(mean_ + (1.96*(sdev/n**(1.0/2))), 1) 
    return lower, upper
    
    
n = int(raw_input().strip())
A = map(int, raw_input().strip().split())

print mean(A)
print median(A)
print mode(A)
print pstdev(A)
print ci(A)[0], ci(A)[1]
