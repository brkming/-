import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from take_MySQL import test
import pandas as pd

class data_ana():
    def data(self):
        self.city = test()
        self.city_list = self.city.mySQLCommand.queryMysql()[1:]

        self.X1=[]
        self.X2=[]
        for v in self.city_list:
            self.X1.append(float(v[1]))
            self.X2.append(float(v[9]))

        # 初始化原始数字点
        self.basis= np.array(self.X1)
        self.total= np.array(self.X2)
        self.X = np.array([self.basis, self.total])
        self.X = np.array(list(zip(self.basis, self.total))).reshape(len(self.basis), 2)

    def category(self):
        self.data()
        self.clusters = [2, 3, 4, 5]  # 簇的个数
        for t in self.clusters:
            self.kmeans_model = KMeans(n_clusters=t).fit(self.X)
            self.nums=list(self.kmeans_model.labels_)
            print('当智慧城市分为{}类时：'.format(t))
            for i in range(t):
                self.num=self.nums.count(i)
                print('\t\t\t\t第{}类的城市有{}个'.format(i+1,self.num))
            print('-----------------------------------')
    def city_all(self):
        city = pd.read_csv('date_deal.csv')

        top10_city = city.sort_values(by=['总分'],ascending=False).head(10)
        print('2016年智慧城市排名前十的是：\n{}'.format(top10_city))
    def find_city(self):
        cities = pd.read_csv('date_deal.csv')
        city=input('请输入你要查询的城市：')
        for i,city1 in enumerate(cities['城市']):
            if city==city1:
                print(cities[i:i+1])


def main():
    f = True
    while f:
        print('\n\n2016年智慧城市数据分析')
        print('请选择以下功能:')
        print('\t\t1—智慧城市分类：')
        print('\t\t2-智慧城市前十名：')
        print('\t\t3-请选择你要查询的城市：')
        print('\t\t4-退出：')
        i = int(input())
        if i == 1:
            data_ana().category()
        elif i == 2:
            data_ana().city_all()
        elif i == 3:
            data_ana().find_city()
        elif i == 4:
            f = False
        input()
if __name__=='__main__':
    main()
