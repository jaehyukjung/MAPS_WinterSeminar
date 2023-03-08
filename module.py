import copy
import random
import numpy as np

STATUSLIST = [0, 1, 2, 3]
STATUSNUM = len(STATUSLIST)

class Prob_Instance:
    def __init__(self):
        self.objective = 'Makespan'
        self.job_list = []
        self.machine_list = []
        self.chromo: Chromosome
        self.setup_metrix = None
        self.work_speed_matrix = None

    def __repr__(self):
        return str(
            'Objective - ' + self.objective + ', Job - ' + str(self.job_list.__len__()) + ', Machine - ' + str(
                self.machine_list.__len__()) + '\n')

    def deepcopy(self):
        return copy.deepcopy(self)


class Job:  # 입력 데이터: job (요청)
    def __init__(self, ID: int, Process_time: int, Due_date: int, Weight: int, Release_time: int, Setup_Status: int):
        self.id = ID
        self.process_time = Process_time
        self.due_date = Due_date
        self.release_date = Release_time
        self.setup = Setup_Status
        self.weight = Weight  # 가중치
        self.end_time = 0

    def initialize(self):
        self.done = False
        self.priority = -1  # 우선순위
        self.start_time = -1  # 시작 시간
        self.tardiness = -1

    def __repr__(self):
        return str('Job # ' + str(self.id))


class Machine:  # 작업 기계
    def __init__(self, ID: int, setup_status: int):
        self.start_time = None
        self.work_speed_list = None
        self.avail_matrix = None
        self.set_time_matrix = None
        self.id = ID
        self.setup_status = setup_status
        self.avail_time = 0  # 시작 가능 시간
        self.work_speed = 0
        self.set_avail_matrix()

    def initialize(self):
        self.measures = {}
        self.served_job = []
        self.can_work = True
        self.measures['makespan'] = 0
        self.measures['total_tardiness'] = 0

    def work(self, target: Job):
        target.done = True
        self.work_speed = self.work_speed_list[target.id - 1]
        self.work_time = target.process_time / self.work_speed  # 작업시간

        if self.setup_status != target.setup:  # 기계의 setup과 Job의 setup 차이 계산
            self.avail_time += self.set_time_matrix[self.setup_status][target.setup]
            self.setup_status = target.setup

        self.start_time = self.avail_time  # set -> setup 후
        target.start_time = self.start_time
        self.avail_time += self.work_time  # 완료시간
        target.end_time = self.avail_time
        target.tardiness = max(0, self.avail_time - target.due_date)
        self.measures['total_tardiness'] += target.tardiness
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def set_avail_matrix(self):  # Job에 대한 기계의 작업 가능 여부(Mj)
        random.seed(100)
        self.avail_matrix = [random.choice([True, False]) for i in range(STATUSNUM)]
        if True not in self.avail_matrix:
            self.avail_matrix[random.randint(0, 2)] = True

    def get_setup_time(self, previousJob, currentJob: Job):  # 기계가 작업할때 setupTime 계산
        return self.set_time_matrix[previousJob][currentJob.setup]

    def doable(self, target: Job) -> bool:  # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))


def set_setup_matrix():  # 각 작업별 setup_time_matrix
    np.random.seed(100)
    setup_matrix = np.random.uniform(10, 30, size=(STATUSNUM, STATUSNUM))
    setup_matrix = np.triu(setup_matrix)
    setup_matrix += setup_matrix.T - np.diag(setup_matrix.diagonal())
    setup_matrix = [[0 if i == j else setup_matrix[i][j] for j in range(STATUSNUM)] for i in range(STATUSNUM)]
    return setup_matrix


def set_work_speed_matrix(job_list, mach_list):
    work_speed_list = [[np.random.randint(1, 4) if mach_list[j].avail_matrix[job_list[i].setup] == True else 0 for i in
                        range(len(job_list))] for j in range(len(mach_list))]
    for i in range(len(mach_list)):
        mach_list[i].work_speed_list = work_speed_list[i]


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


class Gene:
    def __init__(self, id: int, job, mach):
        self.id = id
        self.job = job
        self.mach = mach

    def getGene(self):
        return [self.job, self.mach]


class Chromosome:
    def __init__(self, id):
        self.id = id
        self.chromo = []
        self.objective = 0

    def setChromo(self, gene):
        self.chromo.append(gene)

    def getChromo(self):
        return self.chromo

    def getId_list(self):
        self.id_list = [[gene[0].id, gene[1].id] for gene in self.chromo]
        return self.id_list

    def __repr__(self):
        return str('chromo' + str(self.id))
