from math import inf
from random import*
from time import*
import math
import numpy as np 
import matplotlib.pyplot as plt
from math import radians
import sys





sys.setrecursionlimit(10000)


def Heapify(A,n, i):
    left=2*i+1
    right=2*i+2
    max_num=i
    if(left<n and A[max_num]<A[left]):
        max_num= left
    if(right<n and A[max_num]<A[right]):
        max_num= right
    if(max_num != i):
        A[max_num],A[i]=A[i],A[max_num]
        Heapify(A,n,max_num)



def HeapSort(A_copy):
    A=A_copy
    n=len(A)
    for i in range(n//2-1,-1,-1):
        Heapify(A,n,i)

    for j in range(n-1, 0, -1):
        A[j], A[0] = A[0], A[j] 
        Heapify(A, j, 0)
    return A
      
def HeapSort_witch_time(A_copy):
    start_time =time()
    B=HeapSort(A)
    end_time=time()- start_time
    print("HeapSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return B

def GenerationGapsHibbard(A): 
    N=len(A)
    all_gaps=[]
    i=1
    while(((2**i)-1) < N):
       all_gaps.append((2**i)-1)
       i=i+1
    all_gaps.reverse()
    return all_gaps
def GenerationGapsShella(A):
    N=len(A)
    all_gaps=[]
    i=1
    while(math.ceil(N/(2**i)) > 1):
       all_gaps.append(math.ceil(N/(2**i)))
       i=i+1
    all_gaps.append(1)
    return all_gaps
def GenerationGapsPratta(A):
    N=len(A)
    all_gaps=[]
    for i in range(0,math.ceil(math.log(N,3))):
        for j in range(0,math.ceil(math.log(N,2))):
            if((3**i)*(2**j)>N/2):
                break
            else:
                all_gaps.append((3**i)*(2**j))

    all_gaps.sort(reverse=True)

    return all_gaps


def SelectionSort(A_copy):
    A=A_copy
    start_time =time()
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                A[j],A[i]=A[i],A[j]


    end_time=time()- start_time
    print("ChoisSort time: ",end_time,end='\n')
    return A
def InsertionSort(A_copy):
    A=A_copy
    start_time =time()
    for i in range(1,len(A)):
        j=i
        while((j != 0)and(A[j-1]>A[j])):
            A[j-1],A[j]=A[j],A[j-1]
            j=j-1
    end_time=time()- start_time
    print("InsertionSort time: ",end_time,end='\n')
    return A
def ShellSort(A_copy,all_gaps):
    A=A_copy
    start_time =time()
    for gap in all_gaps:
        for i in range(gap,len(A)):
            j=i
            while(A[j]<A[j-gap] and (j)>=gap):
                A[j],A[j-gap]=A[j-gap],A[j]
                j=j-gap
    end_time=time()- start_time
    print("ShellSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return A
def BubbleSort(A_copy):
    A=A_copy
    start_time =time()
    flag=True 
    while(flag!=False):
        flag=False
        j=0
        for i in range(1,len(A)-j):
            if A[i-1]>A[i]:
                A[i-1],A[i]=A[i],A[i-1]
                flag=True
        j=j+1
    end_time=time()- start_time
    print("BubbleSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return A
def MergeSort(A):
    temp_arr=[]
    arr_len=len(A) 
    if(arr_len==1):
        temp_arr.append(A[0])
        return temp_arr
    else:
        arr_left=MergeSort(A[:int(arr_len/2)])
        arr_right=MergeSort(A[int(arr_len/2):])
        arr_len_left=len(arr_left)
        arr_len_right=len(arr_right)
        arr_left_temp=0
        arr_right_temp=0
        while((arr_len_left != arr_left_temp)and(arr_len_right != arr_right_temp)):
            if(arr_left[arr_left_temp]<arr_right[arr_right_temp]):
                temp_arr.append(arr_left[arr_left_temp])
                arr_left_temp=arr_left_temp+1
            else:
                temp_arr.append(arr_right[arr_right_temp])
                arr_right_temp=arr_right_temp+1
        if(arr_len_left != arr_left_temp):
            for i in range(arr_left_temp, arr_len_left):
                temp_arr.append(arr_left[i])
        elif(arr_len_right != arr_right_temp):
             for i in range(arr_right_temp, arr_len_right):
                temp_arr.append(arr_right[i])
        return temp_arr
def MergeSort_with_time(A):
    start_time =time()
    B=MergeSort(A)
    end_time=time()- start_time
    print("MergeSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return B
def QickSort(A_copy):
    A=A_copy
    temp_arr=[]
    arr_len=len(A) 
    if(arr_len==0):
        return temp_arr
    elif(arr_len==1):
        temp_arr.append(A[0])
        return temp_arr
    elif(arr_len==2):
        temp_arr.append(min(A[0],A[1]))
        temp_arr.append(max(A[0],A[1]))
        return temp_arr

    else:
        mid_num=A[math.ceil(len(A)/2)]

        left_num=[]
        right_num=[] 
        for i in range(1,len(A)):
            if(A[i]<=mid_num):
                left_num.append(A[i]) 
            else:
                right_num.append(A[i])

        left_num=QickSort(left_num)
        left_num.append(mid_num)
        right_num=QickSort(right_num)

        return (left_num+right_num)
def QickSort_with_time(A):
    start_time =time()
    B=QickSort(A)
    end_time=time()- start_time
    print("QickSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return B

def SortedArr(kol):
    A=[i for i in range(1,kol+1)]
    return A

def AlmostSortedArr(kol,_seed):
    A=[i for i in range(1,kol-math.ceil((kol*0.1))+1)]
    seed(_seed)
    for j in range(0,math.ceil(kol*0.1)):
        A.append(randint(0,kol//2))
    return A


def ReversedArr(kol):
    A=[i for i in range(kol,0,-1)]
    return A
def RandomArr(kol,_seed):
    seed(_seed)
    A=[randint(0,kol//2) for _ in range(kol)]
    return A




A=RandomArr(100000,25)
A=QickSort_with_time(A)
print(A)