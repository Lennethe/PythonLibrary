# labels と arrays(観測値)からそれぞれの適切に積み上げ棒グラフを出力する
import matplotlib.pyplot as plt
# テスト用
import numpy as np

def calc_width(t,width):
    if width<1:
        return t*(1/width)//1/(1/width)
        return t*width//width

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

    def initial(self,lower, upper):
        self.bottom = {}
        self.dic = {}
        self.sum = {}
        for label,array in zip(self.labels,self.arrays):
            self.dic[label] = {}
            for value in array:
                if lower != None and value < lower: continue
                if upper != None and upper <= value: continue                
                value = calc_width(value,self.value)
                if value not in self.dic[label]: self.dic[label][value] = 0
                if value not in self.bottom: self.bottom[value] = 0
                self.dic[label][value] += 1
                
    def initial_sum(self):
        for label in self.labels:
            x,y,b = self.get_xyb(label)
            for v1,v2 in zip(x,y):
                if v1 not in self.sum: self.sum[v1] = 0
                self.sum[v1] += v2

    def get_xyb(self, label):
        res = {}
        for k in (self.bottom.keys()): res[k] = 0
        for k in (self.dic[label].keys()): res[k] += self.dic[label][k]
        x = list(res.keys())
        return x, [res[k] for k in x],[self.bottom[k] for k in x]
            
    ##########################

    def plot(self, relative=False, lower=None, upper=None):
        self.initial(lower,upper)
        if relative: self.initial_sum()
        for label in self.labels:
            x,y,bottom = self.get_xyb(label)
            if relative: y = [v/self.sum[k] for k,v in zip(x,y)]
            #plt.bar(x,y,width=self.width,bottom=list(self.bottom.values()),align="edge")
            plt.bar(x,y,width=self.width,bottom=bottom,align="edge",label=label)
            for k,v in zip(x,y):
                self.bottom[k] += v


if __name__ == "__main__":
    a3 = ["a","b","c"]
    b3 = [(np.random.normal(a*3,2,1000)) for a in range(3)]
    print("B1")
    B1 = StackedBarPlot(a3,b3,width=2)
    plt.subplot(2,1,1)
    B1.plot(relative=False,lower=1,upper=5)
    plt.subplot(2,1,2)
    B1.plot(relative=True)
    plt.show()