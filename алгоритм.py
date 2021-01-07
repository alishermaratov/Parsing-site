def insert_sort(A):
    N=len(A)
    for top in range(1, N):
        k=top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k-=1
    return A


def choise_sort(A):
    N=len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k]<A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


    def choise_sort(A):
        N=len(A)
        for pos in range(0, N-1):
            for k in range(pos+1, N):
                if A[k]<A[pos]:
                    A[k], A[pos] = A[k], A[pos]



    def buble_sort(A):
        N=Len(A)
        for i in range(1, N):
            for k in range(0, N-i):
                if A[k]>A[k+1]:
                    A[k], A[k+1]=A[k+1], A[k]
        return A


"""дерево"""
def binary_search(A:list, key:int, start:int, stop:int):
    if start > stop:
        return False
    middle = (start+stop)//2
    if key == A[middle]:
        return middle
    elif key < A[middle]:
         return binary_search(A, key, start, middle-1)
    else:
        return binary_search(A, key, middle+1, stop)

A = [1,12,45,65,86,91,92,100,111]
start = 0
stop = len(A)
key = 45
a = 55

# s = binary_search(A, a, start, stop)
#
#
# print(s)




#
"""steck
модуль описавающий структуру данных -стек
push(1)#вход в очередь
push(2)
push(3)
is_empty()
False
pop()#выход оттуда
3
pop()
2
pop()
1
is_empty()
True
"""
_stack=[]

def push(x):
    _stack.append(x)

def pop():
    x=_stack.pop()
    return x

def clear ():
    _stack.clear()

def is_empty():
    return True #len(_stack)==0

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
