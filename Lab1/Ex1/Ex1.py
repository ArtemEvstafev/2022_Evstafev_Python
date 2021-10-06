import matplotlib.pyplot as plt
for i in range(1, 2):
    f = open(f"dead_moroz/00{i}.dat", 'r')
    a = [i.rstrip() for i in f.readlines()]
    a[int(a[0])+1::] = []
    del a[0]
    x = []
    y = []
    for j in a:
        x.append(float(j.split()[0]))
        y.append(float(j.split()[1]))
    plt.plot(x, y, 'ro')
    plt.title("Plot № %d"% i)
    plt.savefig("Plot № %d.png"% i, )
    f.close()