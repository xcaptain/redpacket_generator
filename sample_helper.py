def normalize(samples, amount):
    l = list(map(lambda x: int(x), samples)) # 先取整数
    while True:
        if sum(l) - amount > 0:
            for i in range(0, len(l)):
                if l[i] > 1: # 保证至少分得1分钱
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
