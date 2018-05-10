import numpy as np
from scipy.stats import truncnorm
from sample_helper import normalize

class NormalDistribStrategy:
    def __init__(self):
        self.sd = 50
        self.miss = 0.3

    def gen(self, amount, total):
        mean = amount / total
        samples = self.get_truncated_normal(mean=mean, sd=self.sd, low=mean/5, upp=amount).rvs(total)
        while not self.isValidSample(samples, amount):
            samples = self.get_truncated_normal(mean=mean, sd=self.sd, low=mean/5, upp=amount).rvs(total)
        return normalize(samples, amount) # 把样本正规化

    def isValidSample(self, samples, amount):
        #if abs(sum(samples) - amount) / amount > self.miss:
        #    return False
        for item in samples:
            if item < 1:
                return False
        return True

    def get_truncated_normal(self, mean=0, sd=1, low=0, upp=10):
        return truncnorm(a=1, b=(upp-mean)/sd, loc=mean, scale=sd)

