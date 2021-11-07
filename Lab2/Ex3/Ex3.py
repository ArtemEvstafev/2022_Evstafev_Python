import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data_excel = pd.read_excel('students_info.xlsx')
data_html = pd.read_html('results_ejudge.html')
dFaculty = data_excel.fillna(value=0).loc[:109]
dEjudge = data_html[0].fillna(value=0).loc[:125]

student_in_faculties = Counter(dFaculty.loc[:, 'group_faculty'].to_numpy())
student_in_groups = Counter(dFaculty.loc[:, 'group_out'].to_numpy())
dFaculty.columns = ['User', 'group_faculty', 'group_out']
perfect_data = pd.merge(dEjudge.iloc[:,[1,11]], dFaculty, on='User')
sum_marks_faculties = perfect_data.groupby('group_faculty').sum().loc[:,'Score'].to_numpy(float)
sum_marks_groups = perfect_data.groupby('group_out').sum().loc[:,'Score'].to_numpy(float)
# print(sum_marks_groups,'\n', sum_marks_faculties)

students_in_faculties_sort = [float(i[1]) for i in sorted(list(student_in_faculties.items()), key = lambda e: e[0])]
students_in_groups_sort = [float(i[1]) for i in sorted(list(student_in_groups.items()), key = lambda e: e[0])]
# print(students_in_groups_sort, '\n', students_in_faculties_sort)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))
fig.set_figheight(9)
fig.set_figwidth(18)
colors = np.random.rand(7, 3)

ax1.bar(['1','2','3','4','5','6','8'], sum_marks_faculties/students_in_faculties_sort, color=colors)
ax2.bar(['31','32','33','34','35','36','38'], sum_marks_groups/students_in_groups_sort, color=colors)

ax1.set_title('Средняя оценка по факультетским группам')
ax2.set_title('Средняя оценка по группам информатики')

plt.savefig('AverageMarks.png')
plt.show()

withH = dEjudge[dEjudge['H'] > 10].loc[:, ['User', 'H']]
withG = dEjudge[dEjudge['G'] > 10].loc[:, ['User', 'G']]
best_of_best = pd.merge_ordered(withG, withH, on='User').fillna(value=0)
print("Вот студенты которые смогли пройти более одного теста в задачах G и H, их факультеты и групы указаны\n",
            pd.merge(best_of_best,dFaculty, on='User'))