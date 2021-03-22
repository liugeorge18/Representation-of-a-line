import numpy as np
import matplotlib.pyplot as plt

a=10
b=-10

def f1 (x):
    f = a*x+b
    return f

s= -5
r= 5
h=.001

x = np.arange(s,r,h)
y1 = [f1(s)for s in x]

x1=[2.6714,2,3]
y2=[26,4,4]

fig=plt.figure(figsize=(10,5))

#Create 3D axes
ax = fig.add_subplot(111)
ax.plot (x,y1, color="green")
plt.grid()
ax.scatter(x1,y2,color="darkblue",marker="o",s=100)
ax.set_xlabel("Eje x",fontsize=14)
ax.set_ylabel("Eje y",fontsize=14)