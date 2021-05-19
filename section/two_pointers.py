"""
計算量
O(N)
区間和がX以上になる区間の個数
"""
A = list(map(int, input().split()))
right, now_sum, res = 0, 0, 0
X = k
for left in range(N):
    while right < N and now_sum + A[right] <= X:
        now_sum += A[right]
        right += 1
    res += (right - left)
    if right == left:
        right += 1
    else:
        now_sum -= A[left]

"""
座標圧縮×尺取法
今までの区間にA[i]が含まれているかどうかはlistの値が0か1以上かで判断
cntで現在の区間の種類数を管理
"""
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

comp, LR = set(), []
for i in range(N):
    LR.append(A[i])
    comp.add(A[i])
comp = sorted(list(comp))
d = defaultdict(int)
for i, c in enumerate(comp):
    d[c] = i

right, res, cnt = 0, 0, 0
num = [0 for _ in range(len(comp))]
for left in range(N):
    while right < N:
        if not num[d[A[right]]] and cnt+1 > K:
            break
        if num[d[A[right]]] == 0:
            cnt += 1
        num[d[A[right]]] += 1
        right += 1
    res = max(res, right - left)
    if right == left:
        right += 1
    else:
        num[d[A[left]]] -= 1
        if num[d[A[left]]] == 0:
            cnt -= 1
print(res)