from module import *
import numpy as np
import random


def cross_solver(instance: Prob_Instance, seed, chromo1, chromo2):
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

    # mach_list = check_avail(mach_list) 이전에 있던거 쓰니거니까 무조건 가능함.
    setup_matrix = instance.setup_metrix

    for mach in mach_list:
        mach.set_time_matrix = setup_matrix
        mach_set.append(mach.setup_status)

    chromo_id_list1 = chromo1.getId_list()
    chromo_id_list2 = chromo2.getId_list()
    chromo_id_list = cross_chromo(chromo_id_list1, chromo_id_list2)

    # solver
    instance, mach_list, job_list, sch_list = match(instance, job_list, mach_list, chromo_id_list, sch_list)

    for job in job_list:
        total_CompletionTime += job.end_time

    instance.chromo.objective = total_CompletionTime

    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)
    # solution['Objective'].append(mach.measures['makespan'])

    return solution, instance.chromo, mach_list, sch_list


def match(instance, job_list, mach_list, chromo_id_list, sch_list):
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
                sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setup_status, setup_time]) # 스케줄 리스트

    return instance, mach_list, job_list, sch_list


def mach_match(job, mach_list, chromo_id_list):
    mach_id = list(filter(lambda x: x[0] == job.id, chromo_id_list))
    mach_id = mach_id[0][1]
    mach = list(filter(lambda x: x.id == mach_id, mach_list))
    return mach[0]


def cross_chromo(chromo1, chromo2):
    point = random.randint(1, len(chromo1) - 1)  # point 지정
    chromo = chromo1[:point]
    job_id = list(zip(*chromo))[0]
    temp = list(filter(lambda x: x[0] not in job_id, chromo2))  # chromo에 있는 job id 중 없는 것 추가
    chromo.extend(temp)
    return chromo
