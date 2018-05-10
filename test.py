# from redpacket_policy import RedpacketPolicy
from normal_distrib_strategy import NormalDistribStrategy
from beta_distrib_strategy import BetaDistribStrategy
import time
import matplotlib.pyplot as plt

def test_normal():
    start = time.time()
    policy = NormalDistribStrategy()
    x = policy.gen(100000, 6000)
    end = time.time()
    print(x, sum(x), sum(x)/len(x))
    print('cost: ', end-start)
    # plt.hist(x, len(x))
    # plt.show()

def test_beta():
    start = time.time()
    policy = BetaDistribStrategy()
    x = policy.gen(100000, 1000)
    end = time.time()
    print(x, sum(x), sum(x)/len(x), max(x), min(x))
    print('cost: ', end-start)
    plt.hist(x, len(x))
    plt.show()


if __name__ == '__main__':
    test_beta()

