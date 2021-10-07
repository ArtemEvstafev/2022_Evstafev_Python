import matplotlib.pyplot as plt
import math
scale_x = math.cos(math.asin(1080/1980))*15.6
scale_y = math.sin(math.asin(1080/1980))*15.6
def plotting(x, y):
    fig, ax = plt.subplots()
    fig.set_figheight(scale_y)
    fig.set_figwidth(scale_x)
    if(len(x) > 100):
        ax.plot(x, y, 'r.', markersize=0.5)
    else:
        ax.plot(x, y, 'r.', markersize=10)
    ax.set_title("Plot № %d" % i)
    plt.savefig("Plot № %d.jpg" % i, dpi=800)
for i in range(1, 6):
    f = open(f"dead_moroz/00{i}.dat", 'r')
    x = []
    y = []
    a = [i.rstrip() for i in f.readlines()]
    a[int(a[0])+1::] = []
    del a[0]
    for j in a:
        x.append(float(j.split()[0]))
        y.append(float(j.split()[1]))
    a=[]
    plotting(x, y)
    f.close()
