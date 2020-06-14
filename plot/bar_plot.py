# labels と arrays(観測値)からそれぞれの適切に積み上げ棒グラフを出力する
import matplotlib.pyplot as plt
# テスト用
import numpy as np

class StackedBarPlot():
    def __init__(self,labels,arrays,width=1):
        if len(labels) != len(arrays):
            print("二引数の次元は同一でなければいけません")
        self.labels = labels
        self.arrays = arrays
        self.width = width
        self.bottom = {}
        self.dic = {}
        self.sum = {}

    def initial(self):
        self.bottom = {}
        self.dic = {}
        self.sum = {}
        for label,array in zip(self.labels,self.arrays):
            self.dic[label] = {}
            for value in array:
                value = value//self.width*self.width
                if value not in self.dic[label]: self.dic[label][value] = 0
                if value not in self.bottom: self.bottom[value] = 0
                self.dic[label][value] += 1
                
    def initial_sum(self):
        for label in self.labels:
            x,y = self.get_xy(label)
            for v1,v2 in zip(x,y):
                if v1 not in self.sum: self.sum[v1] = 0
                self.sum[v1] += v2

    def get_xy(self, label):
        res = {}
        for k in self.bottom.keys(): res[k] = 0
        for k,v in self.dic[label].items():
            res[k] += v
        return list(res.keys()),list(res.values()) 
            
    ##########################

    def plot(self, relative=False):
        self.initial()
        if relative: self.initial_sum()
        for label in self.labels:
            x,y = self.get_xy(label)
            if relative: y = [v1/s1 for v1,s1 in zip(y,self.sum.values())]
            plt.bar(x,y,width=self.width,bottom=list(self.bottom.values()),align="edge")
            for i in range(len(y)):
                self.bottom[x[i]] += y[i]


if __name__ == "__main__":
    a3 = ["a","b","c"]
    b3 = [(np.random.normal(a*3,2,10000)) for a in range(3)]
    print("B1")
    B1 = StackedBarPlot(a3,b3,width=0.1)
    plt.subplot(2,1,1)
    B1.plot(relative=False)
    plt.subplot(2,1,2)
    B1.plot(relative=True)
    plt.show()