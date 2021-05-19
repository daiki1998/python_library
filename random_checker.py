"""
注意点
1. 適切に初期化しているか
2. 小さいケースを試しているか
3. 遅い解法があっているか
"""
import random
def random_generate():
    # 入力値のランダム生成
    N = random.randint(a, b) # a<=n<=b
    A = list(random.randint(a, b) for _ in range(N))
    B = list(list(random.randint(a, b) for _ in range(N)) for _ in range(N))
    return N, A, B

def solve(N, A, B):
    # 自分のプログラム
    pass

def solve_AC(N, A, B):
    # 遅いけど確実にあっているプログラム
    pass

def main():
    test_num = 100
    for t in range(test_num):
        N, A, B = random_generate()
        ans1 = solve(N, A, B)
        ans2 = solve_AC(N, A, B)
        if ans1 != ans2:
            print("WA on Test #{}".format(t+1))
            print("AC output: {}".format(ans1))
            print("WA output: {}".format(ans2))
            print("N: {}".format(N))
            print("A: {}".format(A))
            print("B: {}".format(B))
            break
    print("AC")
if __name__ == "__main__":
    main()
