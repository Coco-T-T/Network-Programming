import numpy as np
from numpy import random
import matplotlib.pyplot as plt

class Po:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def location(p, dis):
    D = Po(0,0)
    for i in range(3):
        if (p[i].x == 0 and p[i].y == 0):
            continue
        for j in range(i+1,3):
            if (p[j].x == 0 and p[j].y == 0):
                continue
            p2p = (float)((p[i].x - p[j].x)*(p[i].x - p[j].x) + (p[i].y - p[j].y)*(p[i].y - p[j].y)) ** 0.5
            if p2p == 0:
                return Po(0,0)
            if (dis[i] + dis[j] <= p2p):
                D.x += p[i].x + (p[j].x - p[i].x)*dis[i] / (dis[i] + dis[j])
                D.y += p[i].y + (p[j].y - p[i].y)*dis[i] / (dis[i] + dis[j])
            else:
                dr = p2p / 2 + (dis[i] * dis[i] - dis[j] * dis[j]) / (2 * p2p) 
                D.x += p[i].x + (p[j].x - p[i].x)*dr / p2p
                D.y += p[i].y + (p[j].y - p[i].y)*dr / p2p
    D.x /= 3
    D.y /= 3
    return D       
            