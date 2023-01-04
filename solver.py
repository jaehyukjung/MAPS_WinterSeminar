from module import *
import numpy as np

def rule_solver(instance: Prob_Instance):
    print('Solver Start')
    solution = {}
    solution["Problem"] = instance.deepcopy()

    setup_metrix: list

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    setup_metrix = np.random.randint(0, 4, size = (len(job_list),len(job_list)))
    setup_metrix = np.triu(setup_metrix)
    setup_metrix += setup_metrix.T - np.diag(setup_metrix.diagonal())
    setup_metrix = [[0 if i == j else setup_metrix[i][j] for j in range(10)]for i in range(10)]

    mach_list = instance.machine_list
    mach: Machine
    for mach in mach_list:
        mach.initialize()



