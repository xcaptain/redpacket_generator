import numpy as np
from sample_helper import normalize

class BetaDistribStrategy:
    def __init__(self):
        # c越小，峰值往左偏移，游戏越刺激
        # c越大，峰值往右偏移，游戏越公平
        self.c = 2

    def gen(self, amount, total):
        '''amount分钱，分为total份'''
        sample = []
        currentAmount = amount
        for j in range(total-1):
            delta = self.sample_by_beta(total-j, currentAmount, total)
            sample.append(delta)
            currentAmount -= delta
        sample.append(currentAmount)
        return normalize(sample, amount)

    def sample_by_beta(self, j, current_amount, num_people):
        x = np.random.beta(self.c, self.c*(j-1))
        return current_amount * x
