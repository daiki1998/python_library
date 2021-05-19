# 入力系
# 1つの整数を入力として受け取る
N = int(input())
# 2つ以上の整数を入力として受け取る
a, b = map(int, input().split())
# 1行の入力をlistとして受け取る
C = list(map(int, input().split()))

# 複数行に渡る2列の数字を列ごとにlistで受け取る
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
AB = list(list(map(int, input().split()))for _ in range(N))