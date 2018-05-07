import numpy as np
from scipy.stats import truncnorm

class RedpacketPolicy:
    def __init__(self):
        self.sd = 80
        self.miss = 0.1

    def gen(self, amount, total):
        mean = amount / total
        samples = self.get_truncated_normal(mean=mean, sd=self.sd, low=mean/5, upp=amount).rvs(total)
        while not self.isValidSample(samples, amount):
            samples = self.get_truncated_normal(mean=mean, sd=self.sd, low=mean/5, upp=amount).rvs(total)
        return self.normalize(samples, amount) # 把样本正规化

    def isValidSample(self, samples, amount):
        if abs(sum(samples) - amount) / amount > self.miss:
            return False
        for item in samples:
            if item <= 1:
                return False
        return True

    def get_truncated_normal(self, mean=0, sd=1, low=0, upp=10):
        return truncnorm(a=(low-mean)/sd, b=(upp-mean)/sd, loc=mean, scale=sd)

    def normalize(self, samples, amount):
        l = list(map(lambda x: int(x), samples)) # 先取整数
        while True:
            if sum(l) - amount > 0:
                for i in range(0, len(l)):
                    if l[i] > 2:
                        l[i] -= 1
                    if sum(l) == amount:
                        return l
            elif sum(l) - amount < 0:
                for i in range(0, len(l)):
                    l[i] += 1
                    if sum(l) == amount:
                            return l
            else:
                return l
