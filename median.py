# Find median from data set

from math import ceil, floor

def median(data):
    length = len(data)
    if length%2 != 0:
        mid = floor(length/2)
        print(data[mid])
    else:
        top = ceil((length+1)/2)
        bot = floor((length+1)/2)
        topv = data[top-1]
        botv = data[bot-1]
        print((topv + botv) / 2)

median([1,2,3,4,5,6,7,8,9,10])