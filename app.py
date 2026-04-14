ADA Lab Programs (Clean & Exam Ready)


1. Linear Search
def search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))

res = search(a, x)

if res != -1:
    print("Element found at index:", res)
else:
    print("Element not found")


2. Binary Search
def bs(a, x):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = (l + h) // 2
        if a[m] == x:
            return m
        elif x < a[m]:
            h = m - 1
        else:
            l = m + 1
    return -1

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter sorted elements: ").split()))
x = int(input("Enter element to search: "))

res = bs(a, x)

if res != -1:
    print("Element found at index:", res)
else:
    print("Element not found")


3. Tower of Hanoi
def hanoi(n, s, a, d):
    if n == 1:
        print("Move disk 1 from", s, "to", d)
        return
    hanoi(n-1, s, d, a)
    print("Move disk", n, "from", s, "to", d)
    hanoi(n-1, a, s, d)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')


4. Selection Sort
n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("Sorted array:", a)


5. Quick Sort
def qs(a):
    if len(a) <= 1:
        return a
    p = a[0]
    left = [x for x in a[1:] if x <= p]
    right = [x for x in a[1:] if x > p]
    return qs(left) + [p] + qs(right)

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

print("Sorted array:", qs(a))


6. Merge Sort
def ms(a):
    if len(a) > 1:
        m = len(a)//2
        l = a[:m]
        r = a[m:]

        ms(l)
        ms(r)

        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i] < r[j]:
                a[k]=l[i]; i+=1
            else:
                a[k]=r[j]; j+=1
            k+=1

        while i<len(l):
            a[k]=l[i]; i+=1; k+=1

        while j<len(r):
            a[k]=r[j]; j+=1; k+=1

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

ms(a)
print("Sorted array:", a)


7. Prim’s Algorithm
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")

g = [list(map(int, input().split())) for _ in range(n)]

selected = [0]*n
selected[0] = 1

edges = 0
cost = 0

print("Edges in MST:")

while edges < n-1:
    min_val = 9999
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and g[i][j]:
                    if g[i][j] < min_val:
                        min_val = g[i][j]
                        x, y = i, j

    print(x, "-", y, "=", g[x][y])
    cost += g[x][y]
    selected[y] = 1
    edges += 1

print("Total cost:", cost)


8. Floyd Warshall
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")

g = [list(map(int, input().split())) for _ in range(n)]

INF = 9999

for i in range(n):
    for j in range(n):
        if i != j and g[i][j] == 0:
            g[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

print("Shortest path matrix:")
for row in g:
    print(row)


9. Tree Traversals
class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def preorder(r):
    if r:
        print(r.v, end=" ")
        preorder(r.l)
        preorder(r.r)

def inorder(r):
    if r:
        inorder(r.l)
        print(r.v, end=" ")
        inorder(r.r)

def postorder(r):
    if r:
        postorder(r.l)
        postorder(r.r)
        print(r.v, end=" ")

root = Node(1)
root.l = Node(2)
root.r = Node(3)

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)


10. Graph Coloring
def safe(v, g, c, col):
    for i in range(len(g)):
        if g[v][i] == 1 and col[i] == c:
            return False
    return True

def solve(g, m, col, v):
    if v == len(g):
        return True

    for c in range(1, m+1):
        if safe(v, g, c, col):
            col[v] = c
            if solve(g, m, col, v+1):
                return True
            col[v] = 0
    return False

n = int(input("Enter number of vertices: "))
g = [list(map(int, input().split())) for _ in range(n)]
m = int(input("Enter number of colors: "))

col = [0]*n

if solve(g, m, col, 0):
    print("Color assignment:", col)
else:
    print("No solution")


11. Job Sequencing
n = int(input("Enter number of jobs: "))
jobs = []

print("Enter job_id deadline profit:")

for _ in range(n):
    i, d, p = input().split()
    jobs.append((i, int(d), int(p)))

jobs.sort(key=lambda x: x[2], reverse=True)

max_d = max(j[1] for j in jobs)
slot = [-1]*(max_d+1)
profit = 0

for j in jobs:
    for t in range(j[1], 0, -1):
        if slot[t] == -1:
            slot[t] = j[0]
            profit += j[2]
            break

print("Job sequence:", slot)
print("Total profit:", profit)


12. 0/1 Knapsack
n = int(input("Enter number of items: "))
val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter capacity: "))

dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, W+1):
        if wt[i-1] <= w:
            dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum profit:", dp[n][W])
