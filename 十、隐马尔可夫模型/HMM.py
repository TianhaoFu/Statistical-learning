import numpy as np

class HMM(object):
    def __init__(self, N, M, pi=None, A=None, B=None):
        self.N = N
        self.M = M
        self.pi = pi
        self.A = A
        self.B = B

    def get_data_with_distribute(self, dist): # 根据给定的概率分布随机返回数据（索引）
        r = np.random.rand()
        for i, p in enumerate(dist):
            if r < p: return i
            r -= p

    def generate(self, T: int):
        '''
        根据给定的参数生成观测序列
        T: 指定要生成数据的数量
        '''
        z = self.get_data_with_distribute(self.pi)    # 根据初始概率分布生成第一个状态
        x = self.get_data_with_distribute(self.B[z])  # 生成第一个观测数据
        result = [x]
        for _ in range(T-1):        # 依次生成余下的状态和观测数据
            z = self.get_data_with_distribute(self.A[z])
            x = self.get_data_with_distribute(self.B[z])
            result.append(x)
        return result

if __name__ == "__main__":
    pi = np.array([.25, .25, .25, .25])
    A = np.array([
        [0,  1,  0, 0],
        [.4, 0, .6, 0],
        [0, .4, 0, .6],
        [0, 0, .5, .5]])
    B = np.array([
        [.5, .5],
        [.3, .7],
        [.6, .4],
        [.8, .2]])
    hmm = HMM(4, 2, pi, A, B)
    print(hmm.generate(10))  # 生成10个数据
 
# 生成结果如下
[0, 0, 1, 1, 1, 1, 0, 1, 0, 0]   # 0代表红球，1代表白球