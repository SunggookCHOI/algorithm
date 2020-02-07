import random

arr = [i for i in range(10)]
random.shuffle(arr)
print(arr)

def swap(a,i,j):
    temp = a[i]
    a[i]=a[j]
    a[j]=temp

def selection_sort(arr):
    for i,v in enumerate(arr):
        min_idx = i
        min_val = v
        for j in range(i+1,len(arr)):
            v2=arr[j]
            if v2 < min_val:
                min_idx = j
                min_val = v2
        swap(arr,i,min_idx)

def insertion_sort(arr):
    for i,v in enumerate(arr):
        j=i
        while j>0 and v < arr[j-1]:
            j-=1
        temp = arr.pop(i)
        arr.insert(j,temp)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)

import collections
def merge(arr, l,r):
    mid = (r+l)//2
    a=collections.deque(arr[l:mid])
    b=collections.deque(arr[mid:r])
    ans = []
    idx = l
    while a and b:
        if a[0] > b[0]:
            arr[idx] = b.popleft()
            idx += 1
        elif a[0] < b[0] :
            arr[idx] = a.popleft()
            idx += 1
        else:
            arr[idx] = a.popleft()
            idx += 1
            arr[idx] = b.popleft()
            idx += 1
    while a:
        arr[idx] = a.popleft()
        idx += 1
    while b:
        arr[idx] = b.popleft()
        idx += 1
        
#arr,0,len(arr)
def merge_sort(arr, l, r):
    mid = (r+l)//2
    if (r-l)>2:
        merge_sort(arr,l,mid)
        merge_sort(arr,mid,r)    
    merge(arr,l,r)

def quick_sort(arr,pivot_idx,l,r):
    original_l, original_r = l,r
    pivot = arr[pivot_idx]
    while l<r:
        while arr[r] > pivot :
            r-=1
        while arr[l] < pivot :
            l+=1
        swap(arr,l,r)
    if original_l < l-1:
        quick_sort(arr,l-1,original_l,l-1)
    if original_r > l+1:
        quick_sort(arr,original_r,l+1,original_r)
