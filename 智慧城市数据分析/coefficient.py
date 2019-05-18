import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
from take_MySQL import test

class coe():
    def data(self):
        self.city = test()
        self.city_list = self.city.mySQLCommand.queryMysql()[1:]

        self.X1 = []
        self.X2 = []
        for v in self.city_list:
            self.X1.append(float(v[1]))
            self.X2.append(float(v[9]))

        # 初始化原始数字点
        self.x1 = np.array(self.X1)
        self.x2 = np.array(self.X2)
        self.X = np.array([self.x1, self.x2])
        self.X = np.array(list(zip(self.x1, self.x2))).reshape(len(self.x1), 2)
        print(self.X1)
        print(self.X2)

    def coef(self):
        self.data()
        self.colors = ['b', 'g', 'r', 'c', 'y']  # 颜色
        self.markers = ['o', 's', 'D', 'v', '*']  # 符号
        self.clusters = [2, 3, 4, 5]  # 簇的个数
        self.how_picture = 0
        self.sc_scores = []

        for t in self.clusters:
            self.how_picture = self.how_picture + 1
            plt.subplot(2, 2, self.how_picture)
            self.kmeans_model = KMeans(n_clusters=t).fit(self.X)  # 训练模型

            for i, l in enumerate(self.kmeans_model.labels_):
                plt.plot(self.x1[i], self.x2[i], color=self.colors[l], marker=self.markers[l], ls='None')

            plt.xlim([0, 20])
            plt.ylim([0, 100])

            self.sc_score = silhouette_score(self.X,self.kmeans_model.labels_, metric='euclidean')
            self.sc_scores.append(self.sc_score)

            plt.title('簇类数=%s, 轮廓系数=%0.03f' % (t,self.sc_score))
        plt.show()
        plt.figure(figsize=(10,5))

        plt.plot(self.clusters,self.sc_scores, '*-')
        plt.title('智慧城市轮廓系数')
        plt.xlabel('簇类数')
        plt.ylabel('轮廓系数')
        plt.show()

def main():
    coe().coef()

if __name__=='__main__':
    main()




