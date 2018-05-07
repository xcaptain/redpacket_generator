from redpacket_policy import RedpacketPolicy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    policy = RedpacketPolicy()
    x = policy.gen(100000, 1000)
    print(x, sum(x), sum(x)/len(x))

    plt.hist(x, len(x))
    plt.show()
