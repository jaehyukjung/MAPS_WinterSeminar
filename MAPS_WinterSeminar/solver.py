from module import *

def rule_solver(instance: Prob_Instance):
    print('Solver Start')
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

    for sch in sch_list:
        print(sch)

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    #solution['Objective'].append(mach.measures['makespan'])

    return solution




