import heapq, time
import matplotlib.pyplot as plt

class BeamSearch():
    """
    提出時はmatplotlibは消す
    最大化問題
    bs = BeamSearch(len_sol, len_beam, debug)
    bs.simulate()
    bs.score_states[0][1] に最も良いスコアになる状態が保存されている．
    ・ハイパーパラメータ
    self.len_beam → ビーム幅,大きい方が幅広い探索,時間との相談
    ・問題ごとの変更
    self.calc_score() → 評価関数を入れる
    self.can_move → 次にとりうる状態を入れる(現在の状態との差分管理)
    """
    def __init__(self, len_sol, len_beam, debug=True):
        self.score_states = [[0, 0]]    # スコア, 状態
        self.len_sol = len_sol          # 答えの配列の長さ
        self.len_beam = len_beam        # ビーム幅(チューニング必要)
        self.can_move = []              # 次の状態にとりうるもの
        self.debug = debug              # スコアのプロットをするか
        self.scores = []                # 各回のスコア
        self.time = time.time()         # かかる時間を保持

    def calc_score(self, state):
        # スコアの計算
        score = 0
        return score

    def simulate(self):
        # 試行
        for _ in range(self.len_sol):
            next_states = []
            for _, state in self.score_states:
                for move in self.can_move:
                    next_state = move+state     # 次の状態に変換
                    next_states.append([-self.calc_score(next_state), next_state])
                    # 最小化 self.calc_score(next_state)
            heapq.heapify(next_states)
            self.score_states = []
            for i in range(min(self.len_beam, len(next_states))):
                self.score_states.append(heapq.heappop(next_states))
            if self.debug:
                self.scores.append(self.score_states[0][0]*(-1))
                # 最小化 self.score_states[0][0]
        self.time = time.time() - self.time

    def plot_scores(self):
        # スコアの確認
        plt.plot([i for i in range(len(self.scores))], self.scores)
        plt.show()