def TowerOfHanoi(n, P1, P2, P3,originalN):
    """ Move n discs from pole P1 to pole P3. """
    if n == 0:
        # No more discs to move in this step
        return

    global count
    count += 1

    # move n-1 discs from P1 to P2
    TowerOfHanoi(n-1, P1, P3, P2,originalN)

    if P1:
        # move disc from P1 to P3
        P3.append(P1.pop())
        print(A, B, C)

    # move n-1 discs from P2 to P3
    TowerOfHanoi(n-1, P2, P1, P3,originalN)

# Initialize the poles: all n discs are on pole A.
n = 3
A = list(range(n,0,-1))
B, C = [], []

print(A, B, C)
count = 0
TowerOfHanoi(n, A, B, C,n)
print(count)