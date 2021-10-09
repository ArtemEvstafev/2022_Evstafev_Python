import matplotlib.pyplot as plt

f = open(f"students.csv", 'r')
data = [i.rstrip() for i in f.readlines()]
f.close()
preps = ['prep1', 'prep2', 'prep3', 'prep4', 'prep5', 'prep6', 'prep7']
groups = ['751', '752', '753', '754', '755', '756']
preps_marks = {i: [0] * 10 for i in preps}
groups_marks = {i: [0] * 10 for i in groups}

for i in data:
    person = i.split(sep=';')
    preps_marks[person[0]][int(person[2]) - 1] += 1
    groups_marks[person[1]][int(person[2]) - 1] += 1

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
width = 0.45
fig.set_figheight(9)
fig.set_figwidth(18)

marks_preps = {}
marks_groups = {}

for i in range(0, 10):
    marks_preps[10 - i] = [sum(j[0:(10 - i):1]) for j in preps_marks.values()]
for i in range(0, 10):
    marks_groups[10 - i] = [sum(j[0:(10 - i):1]) for j in groups_marks.values()]
for i in range(10, 0, -1):
    ax1.bar(preps, marks_preps[i], width, label=f"{i}")
for i in range(10, 0, -1):
    ax2.bar(groups, marks_groups[i], width, label=f"{i}")

ax1.set_title('Marks per Prep')
ax2.set_title('Marks per Group')
for ax in (ax1, ax2):
    ax.legend(loc=1)
    ax.set_yticks(range(0, 20))
plt.savefig('Result.png')
