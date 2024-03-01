import re
from threading import Thread, Lock, Semaphore
import queue
import time
import pywifi
from pywifi import const
from asyncio.tasks import sleep
import itertools as its
from printMap import * 
from loc import * 
import math

#两个对象如何才能相等要比我们想象的复杂很多，但核心的方法是重写__eq__方法，这个方法返回True，则表示两个对象相等，否则，就不相等。相反的，如果两个对象不相等，则重写__ne__方法。
#默认情况下，如果你没有实现这个方法，则使用父类(object)的方法。父类的方法比较是的两个对象的ID(可以通过id方法获取对象ID)，也就是说，如果对象的ID相等，则两个对象也就相等。因此，我们可以得知，默认情况下，对象只和自己相等。例如：

class AP:
    def __init__(self, ssid, mac, signal):
        self.ssid = ssid
        self.mac = mac
        self.signal = signal

class Po:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# mac : location
APdict = {'b8:45:f4:14:d3:30:': Po(25,10), 'b8:45:f4:14:d3:40:': Po(25,10), 'b8:45:f4:14:d3:50:': Po(25,10),
        'b8:45:f4:14:00:50:': Po(35,10), 'b8:45:f4:14:00:60:': Po(35,10), 
        'b8:45:f4:14:d5:a0:': Po(10,20), 'b8:45:f4:14:d5:b0:': Po(10,20), 'b8:45:f4:14:d5:c0:': Po(10,20), 
        'b8:45:f4:14:c7:30:': Po(20,20), 'b8:45:f4:14:c7:40:': Po(20,20), 'b8:45:f4:14:c7:50:': Po(20,20),
        'b8:45:f4:14:c8:50:': Po(30,20), 'b8:45:f4:14:c8:60:': Po(30,20), 'b8:45:f4:14:c8:70:': Po(30,20),
        'b8:45:f4:14:d4:e0:': Po(40,20), 'b8:45:f4:14:d4:f0:': Po(40,20), 'b8:45:f4:14:d5:00:': Po(40,20), 
        'b8:45:f4:14:04:c0:': Po(10,30), 'b8:45:f4:14:04:d0:': Po(10,30), 'b8:45:f4:14:04:e0:': Po(10,30), 
        'b8:45:f4:14:b8:60:': Po(20,30), 'b8:45:f4:14:b8:70:': Po(20,30), 'b8:45:f4:14:b8:80:': Po(20,30),
        'b8:45:f4:14:c8:20:': Po(30,30), 'b8:45:f4:14:c8:30:': Po(30,30), 'b8:45:f4:14:c8:40:': Po(30,30),
        'b8:45:f4:14:6a:60:': Po(40,30), 'b8:45:f4:14:6a:70:': Po(40,30), 'b8:45:f4:14:6a:80:': Po(40,30), 
        'b8:45:f4:14:d5:d0:': Po(20,40), 'b8:45:f4:14:d5:e0:': Po(20,40), 'b8:45:f4:14:d5:f0:': Po(20,40), 
        'b8:45:f4:14:c9:a0:': Po(30,40), 'b8:45:f4:14:c9:b0:': Po(30,40), 'b8:45:f4:14:c9:c0:': Po(30,40),
        'b8:45:f4:14:d3:d0:': Po(20,50), 'b8:45:f4:14:d3:e0:': Po(20,50), 
        'b8:45:f4:14:d4:60:': Po(30,50), 'b8:45:f4:14:d4:70:': Po(30,50), 'b8:45:f4:14:d4:80:': Po(30,50),
        'b8:45:f4:14:d7:50:': Po(10,45), 'b8:45:f4:14:d7:60:': Po(10,45), 'b8:45:f4:14:d7:70:': Po(10,45)}

MACset = set()
APlist = list()  # 去重的AP列表
wifi = pywifi.PyWiFi()  # 抓取网卡接口

# for ifaces in wifi.interfaces():
#     ifaces.disconnect()  #断开所有连接

def getWifiList():
    MACset.clear() # 初始化
    APlist.clear()
    ifaces = wifi.interfaces()[0]  # 抓取第一个无限网卡
    ifaces.scan()
    time.sleep(5)
    results = ifaces.scan_results()  #扫描所有wifi
    for result in results:
        # MAC地址需要在已知的字典中
        if result.ssid == 'SEU-WLAN' and result.bssid in APdict:
            if result.bssid not in MACset:
                MACset.add(result.bssid)
                obj = AP(result.ssid, result.bssid, result.signal)
                APlist.append(obj)    

def printWifiList():
    for obj in APlist:
        print("SSID: " + obj.ssid + " MAC: " + obj.mac + " 信号强度: " + str(obj.signal))

def findMaxWifi(): 
    APlist_sort = sorted(APlist, key=lambda x:x.signal, reverse=True)
    return [APlist_sort[0],APlist_sort[1],APlist_sort[2]]

# 根据信号强度推测距离 dBm
def dis(p):
    d = [0,0,0]
    t = -40  # 基准
    for i in range(3):
        # 换算成dB
        tmp = t - p[i]
        R = (tmp - 65) / 20
        d[i] = (10 ** R) * 1000
    return d

# d = dis([-46,-53,-54])
# print(d[0],d[1],d[2])

def printAP(p):
    print("SSID: " + p.ssid + " MAC: " + p.mac + " 信号强度: " + str(p.signal))

def MacToLoc(m):
    if m in APdict:
        return APdict[m]
    else:
        return Po(0,0)

while (1):
    print("\n>>>>>>>>>>>> operation <<<<<<<<<<<<")
    print(">> 1: continue")
    print(">> 2: quit")
    opt = input(">> option = ")
    if opt == '2':
        break
    else:
        OriginalMap() # 输出原始地图
        print("\n")
        for cnt in range(5):
            getWifiList()
            [maxWifi1,maxWifi2,maxWifi3] = findMaxWifi()

            print("============ " + str(cnt+1) + " ============")
            printAP(maxWifi1)
            printAP(maxWifi2)
            printAP(maxWifi3)

            # 根据mac地址获取AP的位置
            P1 = MacToLoc(maxWifi1.mac)
            P2 = MacToLoc(maxWifi2.mac)
            P3 = MacToLoc(maxWifi3.mac)

            D = Po(0,0)
            # P1 == P2
            if P1.x == P2.x and P1.y == P2.y:
                D.x = (P1.x + P3.x) /2
                D.y = (P1.y + P3.y) /2
            # P1 == P3 or P2 == P3
            elif (P1.x == P3.x and P1.y == P3.y) or (P2.x == P3.x and P2.y == P3.y):
                D.x = (P1.x + P2.x) /2
                D.y = (P1.y + P2.y) /2
            else: 
                D = location([P1,P2,P3],dis([maxWifi1.signal,maxWifi2.signal,maxWifi3.signal]))
            
            # 三点定位出错就用最近邻算法
            if D.x == 0 and D.y == 0:
                D = P1
            
            NewMap(D) # 输出新地图