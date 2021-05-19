# 焼き鈍し法
import random, time, math
import matplotlib.pyplot as plt
from copy import deepcopy

class SimulatedAnnealing:
    """
    提出時はmatplotlibは消す
    最大化問題
    sa = SimulatedAnnealing(init_states, limit_time, debug)
    sa.simulate()
    sa.best_states に最も良いスコアになる状態が保存されている．
    ・ハイパーパラメータ
    self.start_tmp, self.end_tmp → 解の大きさによって決定(どのくらいの幅で温度が変化するか)
    ・問題ごとの変更
    self.calc_score() → 評価関数を入れる
    self.modify() → 問題ごとの次の遷移状態を書く(確率的な遷移)
    """
    def __init__(self, init_states, limit_time, debug=True):
        """
        :param init_states: 初期状態
        :param limit_time: 上限時間
        :param debug: プロット系のデバックをするか
        """
        self.now_states = init_states       # 現在の状態
        self.best_states = init_states      # ベストな状態
        self.start_time = time.time()       # 始めの時間
        self.limit_time = limit_time        # 計算時間の最大値
        self.start_tmp = 50                 # 最初の温度(ハイパラ)
        self.end_tmp = 0.1                  # 最後の温度(ハイパラ), 0より大きい値
        self.now_score = -float("inf")      # 現在のスコア
        # float("inf")
        self.best_score = -float("inf")     # 最大のスコア
        # folat("inf")
        self.debug = debug                  # デバック用 probsで温度が適切かの確認
        self.scores = []                    # 歴代のスコア
        self.probs = []                     # 歴代の遷移確率

    def modify(self):
        # paramsの遷移
        new_states = deepcopy(self.now_states)
        return new_states

    def calc_score(self, states):
        # スコアの計算
        score = 0
        return score

    def has_exceeded_time(self):
        # 経過時間が範囲内かどうか
        if self.limit_time <= time.time() - self.start_time:
            return False
        return True

    def probability(self, now_score, new_score):
        # 温度に対する確率遷移
        if self.now_score < new_score: return 1
        # self.now_score > new_score
        temp = self.start_tmp + (self.end_tmp - self.start_tmp)\
               * (time.time() - self.start_time) / self.limit_time
        prob = math.exp((new_score-now_score)/temp) # math.exp(-(new_score-now_score)/temp)
        return prob

    def simulate(self):
        # シミュレーション
        while self.has_exceeded_time():
            new_states = self.modify()
            new_score = self.calc_score(new_states)
            prob = self.probability(self.now_score, new_score)
            if prob >= random.random():
                self.now_score = new_score
                self.now_states = new_states
            if new_score > self.best_score:
            # new_score < self.best_score
                self.best_score = new_score
                self.best_states = new_states
            if self.debug:
                self.scores.append(self.now_score)
                self.probs.append(prob)

    def plot_scores(self):
        # スコアの確認
        plt.plot([i for i in range(len(self.scores))], self.scores)
        plt.show()

    def plot_probs(self):
        # 温度の確認
        plt.plot([i for i in range(len(self.scores))], self.probs)
        plt.show()