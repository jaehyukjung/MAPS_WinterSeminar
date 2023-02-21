from module import *
import numpy as np
import random


def mut_solver(instance: Prob_Instance, seed, chromo: Chromosome):
    print('Solver Start')
    solution = {}
    solution["Problem"] = instance.deepcopy()
    total_CompletionTime = 0
    sch_list = []

    job_list = instance.job_list
    job: Job
    for job in job_list:
        job.initialize()

    mach_list = instance.machine_list
    mach: Machine
    mach_set = []
    for mach in mach_list:
        mach.initialize()

    setup_matrix = instance.setup_metrix

    for mach in mach_list:
        mach.set_time_matrix = setup_matrix
        mach_set.append(mach.setup_status)

    chromo_id_list = chromo.getId_list()
    chromo_id_list, n = change_chromo(chromo_id_list, job_list, mach_list, seed)
    ch_id = chromo_id_list[n][0]

    # solver
    instance, mach_list, job_list, sch_list = match(instance, job_list, mach_list, chromo_id_list, n, ch_id, sch_list)

    for job in job_list:
        total_CompletionTime += job.end_time

    instance.chromo.objective = total_CompletionTime
    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)

    return solution, instance.chromo, mach_list, sch_list


def match(instance, job_list, mach_list, chromo_id_list, n, ch_id,sch_list):
    gene_id = 1

    while any(job.done is False for job in job_list):
        not_completed_jobs = list(filter(lambda x: x.done is False, job_list))

        for job in not_completed_jobs:
            mach = mach_match(job, mach_list, chromo_id_list)
            cur = job
            setup_time = mach.get_setup_time(previousJob=mach.setup_status, currentJob=cur)
            if mach.work_speed_list[job.id - 1] != 0:
                mach.work(job)
                gene = Gene(gene_id, job, mach)
                instance.chromo.setChromo(gene.getGene())
                gene_id += 1
                sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setup_status, setup_time])
            else:
                if job.id == ch_id:
                    chromo_id_list[n][1] = random.randint(1, len(mach_list))

    return instance, mach_list, job_list, sch_list


def mach_match(job, mach_list, chromo_id_list):
    mach_id = list(filter(lambda x: x[0] == job.id, chromo_id_list))
    mach_id = mach_id[0][1]
    mach = list(filter(lambda x: x.id == mach_id, mach_list))
    return mach[0]


def change_chromo(chromo_id_list, job_list, mach_list, seed):
    random.seed(seed)
    n, m = random.randrange(0, len(job_list)), random.randint(1, len(mach_list))
    chromo_id_list[n][1] = m
    return chromo_id_list, n
