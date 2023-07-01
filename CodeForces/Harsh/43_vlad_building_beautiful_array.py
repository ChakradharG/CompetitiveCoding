import math
n = int(input())
 
while (n > 0):
    size = int(input())
    nums = [int(x) for x in input().split(" ")]
    
    min_num = math.inf
    even,odd = True, True
    
    for i in nums:
        if i%2 == 1:
            min_num = min(min_num, i)
 
    for i in nums:
        if (i%2 == 1) and (i<=min_num):
            odd = False
            break
        
    for i in nums:
        if (i%2 == 0) and (i<=min_num):
            even = False
            break
        
    if even or odd:
        print("Yes")
    else:
        print("No")
        
    
    n -= 1