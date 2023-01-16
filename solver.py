from module import *
import numpy as np
import pandas as pd

def rule_solver(instance: Prob_Instance):
    print('Solver Start')
    solution = {}
    solution["Problem"] = instance.deepcopy()

    setup_matrix: list

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    setup_matrix = np.random.randint(1, 4, size = (len(job_list),len(job_list)))
    setup_matrix = np.triu(setup_matrix)
    setup_matrix += setup_matrix.T - np.diag(setup_matrix.diagonal())
    setup_matrix = [[0 if i == j else setup_matrix[i][j] for j in range(len(job_list))]for i in range(len(job_list))]

    mach_list = instance.machine_list
    mach: Machine
    for mach in mach_list:
        mach.initialize()

    mj_matrix = np.random.randint(0, 2, size=(len(job_list), len(mach_list)))
    workSpeed_matrix = np.random.randint(1, 4, size=(len(job_list), len(mach_list))) # 기계의 각 작업에 대한 작업 속도

    sch_list = []
    sch_list.append(mach.start_time, mach.avail_time, mach.id, job.id, mach.setup)

    total_CompletionTime = 0

    for mach in mach_list:
        total_CompletionTime += mach.avail_time

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    solution['Objective'].append(mach.measures['makespan'])




