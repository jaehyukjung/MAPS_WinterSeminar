import random
import pandas as pd
import matplotlib.pyplot as plt
from module import *
import numpy as np

def rule_solver(instance: Prob_Instance):
    print('Solver Start')
    print('[start time, end time, machine ID, job ID, setup status]')
    solution = {}
    solution["Problem"] = instance.deepcopy()
    sch_list = []
    total_CompletionTime = 0

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    setup_matrix = settingMatrtix()
    mach_list = instance.machine_list
    mach: Machine
    for mach in mach_list:
        mach.initialize()
        mach.settingTimeMatrix = setup_matrix


    while any(job.done is False for job in job_list):
        not_completed_jobs = list(filter(lambda x: x.done is False, job_list))
        is_possble_job = list(filter(lambda x:len(x.pre_list) == 0, not_completed_jobs))

        for job in is_possble_job:
            mach = random.choice(mach_list)
            cur = job
            mach.work(job)
            sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setupstatus]) # 스케줄 리스트

        for job in not_completed_jobs:
            for completed_job in is_possble_job:
                if completed_job.id in job.pre_list:
                    job.pre_list.remove(completed_job.id)

    for mach in mach_list:
        total_CompletionTime += mach.avail_time

    mch1 = list(filter(lambda x: x[2]==1, sch_list))
    mch2 = list(filter(lambda x: x[2]==2, sch_list))

    date_columns = ['start_time', 'end_time', 'machine_ID', 'job_ID', 'setup_status']
    df1 = pd.DataFrame(mch1, columns=date_columns)
    df2 = pd.DataFrame(mch2, columns=date_columns)

    # date_columns = ["Start", "Finish"]
    #
    # for col in date_columns:
    #     df1[col] = pd.to_datetime(df1[col], dayfirst=True)
    df1["Diff"] = df1.end_time - df1.start_time
    df2["Diff"] = df2.end_time - df2.start_time
    #
    # print(df1)
    # print(df2)

    fig, ax = plt.subplots(figsize=(10, 1))
    plt.barh(y=df1['machine_ID'], width=df1['Diff'], left=df1['start_time'])
    plt.barh(y=df2['machine_ID'], width=df2['Diff'], left=df2['start_time'])
    plt.show()
    fig.savefig('gannt-chart.png', facecolor='white', transparent=False, dpi=600)

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    #solution['Objective'].append(mach.measures['makespan'])

    return solution
