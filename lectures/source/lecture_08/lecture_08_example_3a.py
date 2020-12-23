A = [5,7,8,9,3]

print(f"Η λίστα μας πριν τη ταξινόμηση είναι:{A}")

for i in range(len(A)):
    for j in range(len(A)-1,i,-1):
        if A[j-1] > A[j]:
            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp

print(f"Η λίστα μας μετά τη ταξινόμηση είναι:{A}")
