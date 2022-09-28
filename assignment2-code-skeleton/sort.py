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


def merge(lowIndex, lastIndex, mid, a, b):
    i= lowIndex
    j= mid+1
    k=lowIndex
    while i <= mid and j <=lastIndex:
        if a[i] <= a[j]:
            b[k]=a[i]
            i+=1
        else:
            b[k]=a[j]
            j+=1
        k+=1

    if i > mid:
        while j<=lastIndex:
            b[k]=a[j]
            j+=1
            k+=1
    else:
        while i<=mid:
            b[k]=a[i]
            i=i+1
            k=k+1
    for k in range(lowIndex, lastIndex+1, 1):
        a[k]=b[k]




def mergesort1(firstIndex, lastIndex, a , b):
    if firstIndex >= lastIndex:
        return
    else:
        mid = math.floor((firstIndex + lastIndex) / 2)
        mergesort1(firstIndex, mid, a , b)
        mergesort1(mid + 1, lastIndex, a , b)
        merge(firstIndex, lastIndex, mid, a , b)


def mergesort(a):
    firstIndex = 0
    lastIndex = len(a)-1
    b=[]
    for element in a:
        b.append(element)
    mergesort1(firstIndex, lastIndex, a, b)
    return b





def run_mergesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing mergesort
    # Call your mergesort implementation here
    s=mergesort(a)

    # output nums_sorted.txt
    nums_sorted = open('mergesorted.txt', 'w')
    for element in s:
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

    #run_bubblesort()
    run_mergesort()
    # run_quicksort()
    # run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
