from module import *
import numpy as np
import random


def rule_solver(instance: Prob_Instance, seed):
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

    # solver
    instance, mach_list, job_list = match(instance, job_list, mach_list, seed)

    for mach in mach_list:
        total_CompletionTime += mach.avail_time

    instance.chromo.objective = total_CompletionTime
    solution['Objective'] = []
    solution['Objective'].append(total_CompletionTime)

    return solution, instance.chromo


def match(instance, job_list, mach_list, seed):
    random.seed(seed)

    gene_id = 1
    while any(job.done is False for job in job_list):
        not_completed_jobs = list(filter(lambda x: x.done is False, job_list))

        for job in not_completed_jobs:
            mach = random.choice(mach_list)
            cur = job
            setup_time = mach.get_setup_time(previousJob=mach.setup_status, currentJob=cur)
            if mach.work_speed_list[job.id - 1] != 0:
                mach.work(job)
                gene = Gene(gene_id, job, mach)
                instance.chromo.setChromo(gene.getGene())
                gene_id += 1
                # sch_list.append([mach.start_time, mach.avail_time, mach.id, cur.id, mach.setup_status, setup_time]) # 스케줄 리스트

    return instance, mach_list, job_list


def check_avail(mach_list: list):  # 사용 가능한 머신 리스트인지 판단 -> 모든 셋업에 True가 포함 돼 있는지 확인 없다면 변경
    avail_check_list = np.array(
        [[1 if mach.avail_matrix[i] else 0 for i in range(STATUSNUM)] for mach in mach_list])
    avail_check_list2 = avail_check_list.sum(axis=0)

    if 0 in avail_check_list2:
        for i in range(STATUSNUM):
            if avail_check_list2[i] == 0:
                avail_check_list3 = avail_check_list.sum(axis=1)
                mach_id = np.where(avail_check_list3.any() <= (min(avail_check_list3)))
                mach = list(filter(lambda x: (x.id == (mach_id[0] + 1)), mach_list))
                mach[0].avail_matrix[i] = True

    return mach_list
