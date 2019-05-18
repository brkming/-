import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from take_MySQL import test
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#防止出现乱码
class K_means():
    def picture_1(self):
        self.city=test()
        self.city_list=self.city.mySQLCommand.queryMysql()[1:]

        self.X1=[]
        self.X2=[]
        for v in self.city_list:
            self.X1.append(float(v[2]))
            self.X2.append(float(v[10]))

        # 初始化原始数字点
        self.x1 = np.array(self.X1)
        self.x2 = np.array(self.X2)
        self.X = np.array([self.x1,self.x2])
        self.X = np.array(list(zip(self.x1, self.x2))).reshape(len(self.x1), 2)

        # 初始分布图
        plt.xlim([0, 20])
        plt.ylim([0, 100])
        plt.title('智慧城市评分总览')
        plt.scatter(self.x1, self.x2)

    def picture_24(self):
        self.picture_1()
        print(self.X1)
        print(self.X2)
        self.colors = ['b', 'g', 'r', 'c','y']  # 颜色
        self.markers = ['o', 's', 'D', 'v','*']  # 符号
        self.clusters = [2,3,4,5]  # 簇的个数
        self.how_picture=0


        for t in self.clusters:
            self.how_picture=self.how_picture+1
            plt.subplot(2, 2,self.how_picture)
            self.kmeans_model = KMeans(n_clusters=t).fit(self.X)  # 训练模型

            for i, l in enumerate(self.kmeans_model.labels_):
                plt.plot(self.x1[i],self.x2[i],color=self.colors[l],marker=self.markers[l], ls='None')

            plt.xlim([0, 20])
            plt.ylim([0, 100])
            plt.title('簇类数={}'.format(t))


def main():
    K_means().picture_1()
    plt.show()
    K_means().picture_24()
    plt.show()

if __name__=='__main__':
    main()
