from math import inf
from random import*
from time import*
import math
import numpy as np 
import matplotlib.pyplot as plt
from math import radians

#Доп Функции 
def GenerationGaps(A): #2^k-1
    N=len(A)
    all_gaps=[]
    i=1
    while(((2**i)-1) < N):
       all_gaps.append((2**i)-1)
       i=i+1
    all_gaps.reverse()
    return all_gaps
#Сортировки без рекурсии 
def ChoisSort(A_copy):
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
def ShellSort(A_copy):
    A=A_copy
    start_time =time()
    all_gaps=GenerationGaps(A)
    for gap in all_gaps:
        for i in range(gap,len(A)):
            j=i
            while(A[j]<A[j-gap] and (j)>=gap):
                A[j],A[j-gap]=A[j-gap],A[j]
                j=j-gap
    end_time=time()- start_time
    print("ShellSort time: ",round(end_time,2),"N=",len(A),end='\n')
    return A
#Сортировки с рекурсией
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
    #elif(arr_len==3):
    #    temp_arr.append(min(A[0],A[1],A[2]))
    #    temp_arr.append(sum(int(A[0]),int(A[1]),int(A[2]))-max(A[0],A[1],A[2])-min(A[0],A[1],A[2]))
    #    print(A[0],A[1],A[2])
    #    temp_arr.append(max(A[0],A[1],A[2]))
    #    return temp_arr
    else:
        mid_num=A[0]
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


#def main():
#    x = np.arange(0, radians(1800), radians(12))
#    plt.plot(x, np.cos(x), 'b')
#    plt.show()




#seed(25)


#A=[]

#for i in range(1000, 100000, 1000):
#    A.clear()
#    n=i
#    A=[randint(0,n//2) for _ in range(n)]
#    B=A.copy()
#    C=A.copy()
#    print("N:",n)
#    A=ShellSort(A)
#    B=MergeSort_with_time(B)
#    C=QickSort_with_time(C)


#n=1000000
#A=[randint(1,n//2) for _ in range(n)]
#B=A.copy()
#C=A.copy()
#D=A.copy()
#E=A.copy()
#F=A.copy()
#test=A.copy()

#B=ChoisSort(B)
#C=InsertionSort(C)
#D=BubbleSort(D)
#E=ShellSort(E)
#F=MergeSort_with_time(F)
#A=QickSort_with_time(A)
#test.sort()
#print(A==test==E==F)
#print(B==C==D==E==F==test==A)
