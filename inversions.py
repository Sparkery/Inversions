#Yavor Ilija
#July 28, 2013
#Counting Inversions

def inversions(array):
    if len(array) <= 1:
        return 0
    middle = int(len(array) / 2)
    left = array[:middle]
    right = array[middle:]
    
    a = inversions(left)
    b = inversions(right)
    c = split(left, right)

    return a + b + c

def split(left, right):
    count = 0
    i, j = 0, 0
    lleft = len(left)
    lright = len(right)
    while i < lleft and j < lright:
        if left[i] <= right[j]:
            i += 1
        else:
            count += lleft - i
            j += 1
            
    return count

array = [1, 3, 5, 2, 4, 6]

print(inversions(array))
