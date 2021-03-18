# Find median from data set

# import rounding functions
from math import ceil, floor

# median function
def median(data):
    length = len(data)
    # check if length of data set is odd
    if length%2 != 0:
        mid = floor(length/2)
        print(data[mid])
    else:
        # if length of data set is even
        # rounding mid value
        top = ceil((length+1)/2)
        bot = floor((length+1)/2)
        topv = data[top-1]
        botv = data[bot-1]
        print((topv + botv) / 2)

# calling median function
median([1,2,3,4,5,6,7,8,9,10])
