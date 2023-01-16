from module import *
import pandas as pd
import matplotlib.pyplot as plt


def rule_solver(instance: Prob_Instance):
    print('Solver Start')
    print('[start time, end time, machine ID, job ID, setup status]')
    solution = {}
    solution["Problem"] = instance.deepcopy()
    sch_list = []
    job_list = instance.job_list
    mach_list = instance.machine_list
    job: Job
    mach: Machine

    total_CompletionTime = 0

    setup_matrix = settingMatrtix()
    for mach in mach_list:
        mach.initialize()
        mach.settingTimeMatrix = setup_matrix

    for job in job_list:
        job.initialize()

    for mach in mach_list:
        for i in range(len(job_list)):
            cur = job_list[i]
            mach.GETSETTime(previousJob= mach.setupstatus, currentJob= cur)
            mach.work(job_list[i])
            sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setupstatus]) # 스케줄 리스트
            total_CompletionTime += mach.avail_time

    # for sch in sch_list:
    #     print(sch)

    # mch1 = []
    # mch2 = []
    # for sch in sch_list:
    #     if sch[2] == 1:
    #         mch1.append(sch)
    #     else:
    #         mch2.append(sch)

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
    print(df1)
    print(df2)

    fig, ax = plt.subplots(figsize=(10, 1))
    plt.barh(y=df1['machine_ID'], width=df1['Diff'], left=df1['start_time'])
    plt.barh(y=df2['machine_ID'], width=df2['Diff'], left=df2['start_time'])
    plt.show()
    fig.savefig('gannt-chart.png', facecolor='white', transparent=False, dpi=600)

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    #solution['Objective'].append(mach.measures['makespan'])

    return solution

