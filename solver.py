import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from module import *
import numpy as np
import random

def rule_solver(instance: Prob_Instance, seed):
    # random.seed(seed)
    # np.random.seed(seed)
    print('Solver Start')
    solution = {}
    solution["Problem"] = instance.deepcopy()
    sch_list = []
    total_CompletionTime = 0

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    setup_matrix = set_setup_matrtix(5)
    mach_list = instance.machine_list
    mach: Machine
    mach_set = []
    for mach in mach_list:
        mach.initialize()

    avail_check_list = np.array([[1 if mach.availabityMatrix[i] == True else 0 for i in range(statusNum)] for mach in mach_list])
    avail_check_list2 = avail_check_list.sum(axis=0)
    for i in range(len(avail_check_list2)):
        if avail_check_list2[i] == 0:
            avail_check_list3 = avail_check_list.sum(axis=1)
            mach_id = (np.where(avail_check_list3.any() <= (min(avail_check_list3))))
            mach = list(filter(lambda x: (x.id == (mach_id[0] + 1)), mach_list))
            # mach = random.choice(mach_list)
            mach[0].availabityMatrix[i] = True
    for mach in mach_list:
        mach.settingTimeMatrix = setup_matrix
        mach_set.append(mach.setupstatus)

    work_speed = set_work_speed_matrix(job_list, mach_list)
    instance, mach_list, job_list= match(instance, job_list,mach_list, seed)

    for mach in mach_list:
        total_CompletionTime += mach.avail_time

    instance.chromo.objective = total_CompletionTime

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    #solution['Objective'].append(mach.measures['makespan'])

    return solution, instance.chromo

def mach_choice(mach_list):
    return random.randrange(0,len(mach_list))

def match(instance, job_list, mach_list, seed):
    random.seed(seed)
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
                # sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setupstatus, setup_time]) # 스케줄 리스트

        for job in not_completed_jobs:
            for completed_job in is_possble_job:
                if completed_job.id in job.pre_list:
                    job.pre_list.remove(completed_job.id)

    return instance, mach_list, job_list