import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from module import *
import numpy as np
import random

def rule_solver(instance: Prob_Instance, seed):
    random.seed(seed)
    print('Solver Start')
    solution = {}
    solution["Problem"] = instance.deepcopy()
    sch_list = []
    total_CompletionTime = 0

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    setup_matrix = set_setup_matrtix()
    mach_list = instance.machine_list
    mach: Machine
    mach_set = []
    for mach in mach_list:
        mach.initialize()

    avail_check_list = np.array([[1 if mach.availabityMatrix[i] == True else 0 for i in range(statusNum)] for mach in mach_list])
    avail_check_list2 = avail_check_list.sum(axis=0)
    for i in range(len(avail_check_list2)):
        if avail_check_list2[i] == 0:
            mach = random.choice(mach_list)
            mach.availabityMatrix[i] = True
    for mach in mach_list:
        mach.settingTimeMatrix = setup_matrix
        mach_set.append(mach.setupstatus)

    work_speed = set_work_speed_matrix(job_list, mach_list)

    while any(job.done is False for job in job_list):
        not_completed_jobs = list(filter(lambda x: x.done is False, job_list))
        is_possble_job = list(filter(lambda x:len(x.pre_list) == 0, not_completed_jobs))

        for job in is_possble_job:
            mach = random.choice(mach_list)
            cur = job
            setup_time = mach.GETSETTime(previousJob=mach.setupstatus, currentJob=cur)
            if mach.workSpeedList[job.id -1] != 0:
                mach.work(job)
                gene = Gene(job,mach)
                instance.chromo.setChromo(gene.getGene())
                sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setupstatus, setup_time]) # 스케줄 리스트

        for job in not_completed_jobs:
            for completed_job in is_possble_job:
                if completed_job.id in job.pre_list:
                    job.pre_list.remove(completed_job.id)

    for mach in mach_list:
        total_CompletionTime += mach.avail_time

    instance.chromo.objective = total_CompletionTime

    # mch1 = list(filter(lambda x: x[2]==1, sch_list))
    # mch2 = list(filter(lambda x: x[2]==2, sch_list))
    # mch3 = list(filter(lambda x: x[2]==3, sch_list))
    #
    # set_lst1 = [mach_set[0]]
    # set_lst2 = [mach_set[1]]
    # set_lst3 = [mach_set[2]]
    #
    # for i in range(len(mch1)):
    #     set_lst1.append(mch1[i][4])
    #
    # for i in range(len(mch2)):
    #     set_lst2.append(mch2[i][4])
    #
    # for i in range(len(mch3)):
    #     set_lst3.append(mch3[i][4])
    #
    # word1 = []
    # word2 = []
    # word3 = []
    #
    # for i in range(len(set_lst1)-1):
    #     word1.append("(" + str(set_lst1[i]) + "->" + str(set_lst1[i+1]) + ")")
    #
    # for i in range(len(set_lst2)-1):
    #     word2.append("(" + str(set_lst2[i]) + "->" + str(set_lst2[i + 1]) + ")")
    #
    # for i in range(len(set_lst3)-1):
    #     word3.append("(" + str(set_lst3[i]) + "->" + str(set_lst3[i + 1]) + ")")
    #
    # sch_columns = ['start_time', 'end_time', 'machine_ID', 'job_ID', 'setup_status','setup_time']
    # df1 = pd.DataFrame(mch1, columns=sch_columns)
    # df2 = pd.DataFrame(mch2, columns=sch_columns)
    # df3 = pd.DataFrame(mch3, columns=sch_columns)
    #
    # mcolors.CSS4_COLORS = list(mcolors.CSS4_COLORS.values())
    #
    # df1["work_time"] = df1.end_time - df1.start_time
    # df2["work_time"] = df2.end_time - df2.start_time
    # df3["work_time"] = df3.end_time - df3.start_time
    #
    # print(df1)
    # print(df2)
    # print(df3)
    #
    # # 간트차트 생성
    # fig, ax = plt.subplots(figsize=(11, 2))
    # ax.set_yticks([1,2,3])
    # ax.set_yticklabels(['Machine1', 'Machine2','Machine3'])
    #
    # pl1 = plt.barh(y=df1['machine_ID'], width=df1['work_time'], left=df1['start_time'], color=mcolors.CSS4_COLORS)
    # mcolors.CSS4_COLORS.pop(7)
    # for i in range(len(df1)):
    #     mcolors.CSS4_COLORS.pop(0)
    # pl2 = plt.barh(y=df1['machine_ID'], width=df1['setup_time'], left=df1['start_time'] - df1['setup_time'], color = 'yellow')
    # pl3 = plt.barh(y=df2['machine_ID'], width=df2['work_time'], left=df2['start_time'], color = mcolors.CSS4_COLORS)
    # pl4 = plt.barh(y=df2['machine_ID'], width=df2['setup_time'], left=df2['start_time'] - df2['setup_time'], color = 'yellow')
    # pl5 = plt.barh(y=df3['machine_ID'], width=df3['work_time'], left=df3['start_time'], color = mcolors.CSS4_COLORS)
    # pl6 = plt.barh(y=df3['machine_ID'], width=df3['setup_time'], left=df3['start_time'] - df3['setup_time'], color = 'yellow')
    #
    # job_name1 = df1['job_ID'].to_list()
    # job_name2 = df2['job_ID'].to_list()
    # job_name3 = df3['job_ID'].to_list()
    #
    #
    # setup1 = []
    # setup2 = []
    # setup3 = []
    #
    #
    # for i in range(len(df1)):
    #     setup1.append("setup\n" + word1[i])
    #     job_name1[i] = ('Job'+str(job_name1[i]))
    #
    # for i in range(len(df2)):
    #     setup2.append("setup\n" + word2[i])
    #     job_name2[i] = ('Job' + str(job_name2[i]))
    #
    # for i in range(len(df3)):
    #     setup3.append("setup\n" + word3[i])
    #     job_name3[i] = ('Job' + str(job_name3[i]))
    #
    # ax.bar_label(pl1, job_name1, label_type='center')
    # ax.bar_label(pl2, setup1, label_type='center')
    # ax.bar_label(pl3, job_name2, label_type='center')
    # ax.bar_label(pl4,setup2, label_type='center')
    # ax.bar_label(pl5, job_name3, label_type='center')
    # ax.bar_label(pl6,setup3, label_type='center')
    #
    # plt.title('Sum of Completion Time: ' + str(total_CompletionTime))
    #
    # plt.show()

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    #solution['Objective'].append(mach.measures['makespan'])

    return solution, instance.chromo