import os
import array
import sys
import math
# Bubble Sort Implementation

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False



def run_bubblesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing bubblesort
    bubblesort(a)

    # output nums_sorted.txt
    nums_sorted = open('bubblesorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def merge(firstIndex, lastIndex, mid, a, b):
    leftPointer= firstIndex
    rightPointer= mid+1
    k=firstIndex
    # compare until there are elements in
    # both left array and right array
    while leftPointer <= mid and rightPointer <=lastIndex:
        if a[leftPointer] <= a[rightPointer]:
            b[k]=a[leftPointer]
            leftPointer+=1
        else:
            b[k]=a[rightPointer]
            rightPointer+=1
        k+=1
    #copy all remaining elements from right array
    # when there are no any elements in left array
    if leftPointer > mid:
        while rightPointer<=lastIndex:
            b[k]=a[rightPointer]
            rightPointer+=1
            k+=1
    #copy all remaining elements from left array
    # when there are no any elements in right array
    else:
        while leftPointer<=mid:
            b[k]=a[leftPointer]
            leftPointer+=1
            k=k+1
    #copy sorted element to original array
    for k in range(firstIndex, lastIndex+1, 1):
        a[k]=b[k]


def recursivemergesort(firstIndex, lastIndex, a , b):
    #do nothing when there is single element
    if firstIndex >= lastIndex:
        return
    #divide array into two equal halves and
    #merge sorted array recursively
    else:
        mid = math.floor((firstIndex + lastIndex) / 2)
        recursivemergesort(firstIndex, mid, a , b)
        recursivemergesort(mid + 1, lastIndex, a , b)
        merge(firstIndex, lastIndex, mid, a , b)

def mergesort(a):
    firstIndex = 0
    lastIndex = len(a)-1
    b=[]
    #create identical array
    for element in a:
        b.append(element)
    recursivemergesort(firstIndex, lastIndex, a, b)
    return b

def run_mergesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing mergesort
    # Call your mergesort implementation here
    sortedArray=mergesort(a)

    # output nums_sorted.txt
    nums_sorted = open('mergesorted.txt', 'w')
    for element in sortedArray:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    # quicksort(a)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    # heapsort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    run_bubblesort()
    run_mergesort()
    # run_quicksort()
    # run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
