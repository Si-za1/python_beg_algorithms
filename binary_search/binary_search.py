# steps to follow : binary sarch 

# finding the midpoint 
# if the target value is equal to midpoint, return the index
# if the target is greater than midpoint, moving to the right side with the midpoint+1
# if target is less than the midpoint, moving to the left with midpoint-1
# if none of the above condition return -1

# let's start doing the basic search 

# to search the number, the number is compared with each number present in the list 

def basic_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

if __name__ == "__main__":
    l=[3,5,4,6]
    target = 10
    result = basic_search(l,target)
    print("The basic search:", result)

# now the binary search 
