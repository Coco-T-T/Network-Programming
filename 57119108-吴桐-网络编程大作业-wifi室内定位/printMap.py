import matplotlib.pyplot as plt
import numpy as np

class Po:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = 15
fig_edge = 60
x=[25, 35, 10, 20, 30, 40, 10, 20, 30, 40, 20, 30, 20, 30, 10]
y=[10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 50, 50, 45]

# mac : location
APdict = {'a': Po(25,10), 'b': Po(35,10), 
        'c': Po(10,20), 'a': Po(20,20), 'b': Po(30,20), 'c': Po(40,20), 
        'a': Po(10,30), 'b': Po(20,30), 'c': Po(30,30), 'c': Po(40,30), 
        'a': Po(20,40), 'b': Po(30,40), 'c': Po(20,50), 'c': Po(30,50),
        'a': Po(10,45)}

def OriginalMap():
    # 1. 创建数据
    # x = np.random.rand(n) * 25
    # y = np.random.rand(n) * 25
    # 2.创建一张figure
    fig = plt.figure(1)
    # 3. 设置颜色 color 值【可选参数，即可填可不填】，方式有几种
    # colors = np.random.rand(n) # 随机产生10个0~1之间的颜色值，或者
    # colors = ['r', 'g', 'y', 'b', 'r', 'c', 'g', 'b', 'k', 'm']  # 可设置随机数取
    colors = ['b'] * n
    # 4. 设置点的面积大小 area 值 【可选参数】
    area = 50
    # 5. 设置点的边界线宽度 【可选参数】
    widths = 5 # 0-9的数字
    # 6. 正式绘制散点图：scatter
    plt.scatter(x, y, s=area, c=colors, linewidths=widths, alpha=0.5, marker='o')
    # 7. 设置轴标签：xlabel、ylabel
    #设置X轴标签
    plt.xlabel('X坐标')
    #设置Y轴标签
    plt.ylabel('Y坐标')
    # 8. 设置图标题：title
    plt.title('梅园食堂一楼')
    # 9. 设置轴的上下限显示值：xlim、ylim
    # 设置横轴的上下限值
    plt.xlim(0, fig_edge)
    # 设置纵轴的上下限值
    plt.ylim(0, fig_edge)
    # 10. 设置轴的刻度值：xticks、yticks
    # 设置横轴精准刻度
    plt.xticks(np.arange(0, fig_edge, step=5))
    # 设置纵轴精准刻度
    plt.yticks(np.arange(0, fig_edge, step=5))
    # 11. 在图中某些点上（位置）显示标签：annotate
    # plt.annotate("(" + str(round(x[2], 2)) + ", " + str(round(y[2], 2)) + ")", xy=(x[2], y[2]), fontsize=10, xycoords='data')# 或者
    for i in range(n):
        plt.annotate("({0},{1})".format(round(x[i],1), round(y[i],1)), xy=(x[i], y[i]), fontsize=10, xycoords='data')
    # xycoords='data' 以data值为基准
    # 设置字体大小为 10
    # 12. 在图中某些位置显示文本：text
    # plt.text(round(x[6],2), round(y[6],2), "good point", fontdict={'size': 10, 'color': 'red'})  # fontdict设置文本字体
    # Add text to the axes.
    # 13. 设置显示中文
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    # 14. 设置legend，【注意，'绘图测试’：一定要是可迭代格式，例如元组或者列表，要不然只会显示第一个字符，也就是legend会显示不全】
    plt.legend(['AP'], loc=2, fontsize=10)
    # plt.legend(['绘图测试'], loc='upper left', markerscale = 0.5, fontsize = 10) #这个也可
    # markerscale：The relative size of legend markers compared with the originally drawn ones.
    # 15. 显示图片 show
    plt.show()

def NewMap(person):
    # 1. 创建数据
    # x = np.random.rand(n) * 25
    # y = np.random.rand(n) * 25
    # 2.创建一张figure
    fig = plt.figure(1)
    # 3. 设置颜色 color 值【可选参数，即可填可不填】，方式有几种
    # colors = np.random.rand(n) # 随机产生10个0~1之间的颜色值，或者
    # colors = ['r', 'g', 'y', 'b', 'r', 'c', 'g', 'b', 'k', 'm']  # 可设置随机数取
    colors = ['b'] * n
    # 4. 设置点的面积大小 area 值 【可选参数】
    area = 50
    # 5. 设置点的边界线宽度 【可选参数】
    widths = 5 # 0-9的数字
    # 6. 正式绘制散点图：scatter
    plt.scatter(x, y, s=area, c=colors, linewidths=widths, alpha=0.5, marker='o')
    plt.scatter(person.x, person.y, s=area, c='r', linewidths=widths, alpha=0.5, marker='o')
    # 7. 设置轴标签：xlabel、ylabel
    #设置X轴标签
    plt.xlabel('X坐标')
    #设置Y轴标签
    plt.ylabel('Y坐标')
    # 8. 设置图标题：title
    plt.title('梅园食堂一楼')
    # 9. 设置轴的上下限显示值：xlim、ylim
    # 设置横轴的上下限值
    plt.xlim(0, fig_edge)
    # 设置纵轴的上下限值
    plt.ylim(0, fig_edge)
    # 10. 设置轴的刻度值：xticks、yticks
    # 设置横轴精准刻度
    plt.xticks(np.arange(0, fig_edge, step=5))
    # 设置纵轴精准刻度
    plt.yticks(np.arange(0, fig_edge, step=5))
    # 11. 在图中某些点上（位置）显示标签：annotate
    # plt.annotate("(" + str(round(x[2], 2)) + ", " + str(round(y[2], 2)) + ")", xy=(x[2], y[2]), fontsize=10, xycoords='data')# 或者
    for i in range(n):
        plt.annotate("({0},{1})".format(round(x[i],1), round(y[i],1)), xy=(x[i], y[i]), fontsize=10, xycoords='data')
    # xycoords='data' 以data值为基准
    # 设置字体大小为 10
    # 12. 在图中某些位置显示文本：text
    plt.text(round(person.x,2), round(person.y,2), "YOU", fontdict={'size': 10, 'color': 'red'})  # fontdict设置文本字体
    # Add text to the axes.
    # 13. 设置显示中文
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    # 14. 设置legend，【注意，'绘图测试’：一定要是可迭代格式，例如元组或者列表，要不然只会显示第一个字符，也就是legend会显示不全】
    plt.legend(['AP'], loc=2, fontsize=10)
    # plt.legend(['绘图测试'], loc='upper left', markerscale = 0.5, fontsize = 10) #这个也可
    # markerscale：The relative size of legend markers compared with the originally drawn ones.
    # 15. 显示图片 show
    plt.show()