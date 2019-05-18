import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Bar
from pyecharts import Page
from pyecharts import Pie
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

city = pd.read_csv('date_deal.csv')

page = Page()
def bar_1():
    top10_city = city.sort_values(by=['总分'],ascending=False).head(10)
    bar_1=Bar('2016年智慧城市排名前十的城市')
    bar_1.add('智慧城市总分',top10_city['城市'],top10_city['总分'],is_more_utils = True)
    page.add(bar_1)
def bar_2():
    city_all = city.sort_values(by=['总分'],ascending=False)
    bar_2=Bar('2016年智慧城市排名')
    bar_2.add('城市',city_all['城市'],city_all['总分'])
    page.add(bar_2)
def bar_3():
    global x_list
    global y_list
    list=[0]*7
    X_list=['20-30','30-40','40-50','50-60','60-70','70-80','80-90']
    for i in city['总分']:
        if 20<=i<30:
            list[0]=list[0]+1
        elif 30<=i<40:
            list[1] = list[1] + 1
        elif 40<=i<50:
            list[2] = list[2] + 1
        elif 50<=i<60:
            list[3] = list[3] + 1
        elif 60<=i<70:
            list[4] = list[4] + 1
        elif 70<=i<80:
            list[5] = list[5] + 1
        elif 80<=i<90:
            list[6] = list[6] + 1
    x_list=X_list
    y_list=list
    bar_3=Bar('2016年智慧城市区间分布')
    bar_3.add('城市',x_list,y_list)
    page.add(bar_3)
def pie_1():

    pie_1=Pie('')
    pie_1.add('',x_list,y_list,is_label_show=True)
    page.add(pie_1)

def main():
    bar_1()
    bar_2()
    bar_3()
    pie_1()
    page.render()

if __name__=='__main__':
    main()


