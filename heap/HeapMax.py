def MaxHeapify(A, i):
    left = 2*i
    right = 2*i + 1
    if left <= len(A) - 1 and A[left] > A[i]:
        maior = left
    else:
        maior = i 
    if right <= len(A) - 1 and A[right] > A[maior]:
        maior = right
    if maior != i:
        A[i], A[maior] = A[maior], A[i] 
        MaxHeapify(A, maior)

def BuildHeap(A):
    HeapSize = len(A)
    for i in range(HeapSize//2, -1, -1):
        MaxHeapify(A, i)


# --- Main --- 
A = [8, 18, 14, 17, 12, 13, 11, 15, 16]
print(A)
BuildHeap(A)
print(A)