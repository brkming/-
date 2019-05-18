import csv
import matplotlib.pyplot as plt
from take_MySQL import test
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#防止出现乱码
def deal():
    city=test()
    city_list=city.mySQLCommand.queryMysql()
    with open('date_deal.csv','w',encoding='utf-8',newline='')as f:
        writer = csv.writer(f)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                # 每处理十条记录输出
                print('已处理{}条记录，共{}条记录'.format(i + 1, len(city_list)))
            writer.writerow(city)

def main():
    deal()
if __name__=='__main__':
    main()

