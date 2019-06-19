from math import floor

def readFile():
    file = open('input3.txt','r')
    lst = list(map(int,file.readline().split()))
    return lst

def findInversion(lst):
    lst,inversions = findInversionHelper(lst) # calls helper method for finding inversions 
    return inversions
def findInversionHelper(lst):

    length = len(lst)

    if length < 2: #returns zero if the list has less than two elements
        return lst,0

    mid = floor(length / 2)#nearest integer to the halfway point
    leftArr = lst[:mid]
    rightArr = lst[mid:]

    leftArr,leftInverions = findInversionHelper(leftArr) #retirns the sorted sub array and inversions for the left side
    rightArr,rightInversions = findInversionHelper(rightArr) #returns the sorted sub array and inversions for the right side
    c,counter = merge(leftArr,rightArr) #merges the two sub array returns the inversions

    return  c,counter+leftInverions+rightInversions

def merge(leftArr,rightArr):

    merged = []
    counter = 0
    mid = len(leftArr)
    leftIndex = 0
    rightIndex=0
    while len(leftArr)>leftIndex and len(rightArr)>rightIndex:
        if leftArr[leftIndex] <= rightArr[rightIndex]: #if the number in the left array is less than the right array put it into the main array
            merged.append(leftArr[leftIndex])
            leftIndex+=1
        else:
            counter += (mid - leftIndex) #f the right one is bigger increase the number of inverions
            merged.append(rightArr[rightIndex])
            rightIndex+=1
    while len(leftArr)>leftIndex:#add elements on from the left until the left array is empty 
        merged.append(leftArr[leftIndex])
        leftIndex+=1
    while len(rightArr)>rightIndex:
        merged.append(rightArr[rightIndex])#add elements on from the right until the right array is empty 
        rightIndex+=1
    return merged, counter


lst = readFile()
print(findInversion(lst))