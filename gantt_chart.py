import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def ganttChart(sch_list, Solution, mach_setup):
    mch = [list(filter(lambda x: x[2]==i, sch_list)) for i in range(1,6)]
    set_lst = mach_setup

    for i in range(len(mch)):
        for j in range(len(mch[i])):
            set_lst[i].append(mch[i][j][4])

    word = []
    for i in set_lst:
        word1 = []
        for j in range(len(i)-1):
            word1.append("") if i[j] == i[j+1] else word1.append("(" + str(i[j]) + "->" + str(i[j+1]) + ")")
        word.append(word1)

    sch_columns = ['start_time', 'end_time', 'machine_ID', 'job_ID', 'setup_status','setup_time']
    df1 = [pd.DataFrame(mch[i], columns=sch_columns) for i in range(5)]
    df =sch_list

    setup = []
    for i in range(len(df)):
        for j in range(len(df[i])):
            setup.append("") if word[i][j] == "" else setup.append("setup\n" + word[i][j])

    for i in df:
        i["work_time"] = i.end_time - i.start_time

    # 간트차트 생성
    fig, ax = plt.subplots(figsize=(11, 2))
    ax.set_yticks([1,2,3,4,5])
    ax.set_yticklabels(['Machine1', 'Machine2','Machine3', 'Machine4', 'Machine5'])
    color = list(mcolors.CSS4_COLORS.values())
    color.pop(7)

    df = pd.concat([df[0],df[1],df[2],df[3],df[4]])

    job_name = df['job_ID'].to_list()
    pl1 = plt.barh(y=df['machine_ID'], width=df['work_time'], left=df['start_time'], color=color)
    pl2 = plt.barh(y=df['machine_ID'], width=df['setup_time'], left=df['start_time'] - df['setup_time'], color = 'yellow')

    for i in range(len(df)):
        job_name[i] = ('Job' + str(job_name[i]))

    ax.bar_label(pl1, job_name, label_type='center')
    ax.bar_label(pl2, setup, label_type='center')
    plt.title('Sum of Completion Time: ' + str(Solution['Objective']))

    return plt.show()