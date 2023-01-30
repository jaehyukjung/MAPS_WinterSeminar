import copy
import random
import numpy as np

statusList = [0,1,2]
statusNum = len(statusList)


class Prob_Instance:
    def __init__(self):
        self.objective = 'Makespan'
        self.job_list = [] # 작업 list
        self.machine_list = [] # 기계 list
        self.chromo: Chromosome

    def __repr__(self):
        return str(
            'Objective - ' + self.objective + ', Job - ' + str(self.job_list.__len__()) + ', Machine - ' + str(
                self.machine_list.__len__()) + '\n')

    def deepcopy(self):
        return copy.deepcopy(self)


class Job: # 입력 데이터: job (요청)
    def __init__(self, ID: int, Process_time, Due_date, Weight, Release_time,Setup_Status:int, Pre_list:list):
        self.id = ID
        self.process_time = Process_time
        self.due_date = Due_date
        self.release_date = Release_time
        self.setup = Setup_Status
        self.weight = Weight # 가중치
        self.pre_list = Pre_list # 선행작업

    def initialize(self):
        self.done = False
        self.priority = -1 # 우선순위
        self.start_time = -1 # 시작 시간
        self.tardiness = -1

class Machine: # 작업 기계
    def __init__(self, ID: int, setUpStatus: int):
        self.start_time = None
        self.workSpeedList = None
        self.availabityMatrix = None
        self.settingTimeMatrix = None
        self.id = ID
        self.setupstatus = setUpStatus
        self.avail_time = 0 # 시작 가능 시간
        self.work_speed = 0

    def initialize(self):
        self.measures = {}
        self.served_job = []
        self.can_work = True
        self.measures['makespan'] = 0
        self.measures['total_tardiness'] = 0
        self.setAvialabilityMatrix()
        # self.setWorkSpeedList()
        # self.work_speed = self.workSpeedList[0]

    def work(self, target: Job):
        target.done = True
        self.work_speed = self.workSpeedList[target.id-1]
        self.work_time = target.process_time / self.work_speed  # 작업시간

        if self.setupstatus != target.setup: # 기계의 setup과 Job의 setup 차이 계산
           self.avail_time += self.settingTimeMatrix[self.setupstatus][target.setup]
           self.setupstatus = target.setup

        self.start_time = self.avail_time # set -> setup 후
        target.start_time = self.start_time
        self.avail_time += self.work_time  # 완료시간
        target.tardiness = max(0, self.avail_time - target.due_date)
        self.measures['total_tardiness'] += target.tardiness
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def setAvialabilityMatrix(self): # Job에 대한 기계의 작업 가능 여부(Mj)
        self.availabityMatrix = [random.choice([True, False]) for i in range(statusNum)]
        if True not in self.availabityMatrix:
            self.availabityMatrix[random.randint(0,2)] = True

    # def setWorkSpeedList(self): # 각 기계의 Job에 대한 작업 속도
    #     workSpeedList = [np.random.randint(1,4) for i in range(statusNum)]
    #     self.workSpeedList = workSpeedList

    def GETSETTime(self, previousJob, currentJob: Job): # 기계가 작업할때 setupTime 계산
        return self.settingTimeMatrix[previousJob][currentJob.setup]

    def doable(self, target: Job) -> bool: # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))

def set_setup_matrtix(): # 각 작업별 setupTimeMatrix
    setup_matrix = np.random.randint(1, 4, size=(statusNum, statusNum))
    setup_matrix = np.triu(setup_matrix)
    setup_matrix += setup_matrix.T - np.diag(setup_matrix.diagonal())
    setup_matrix = [[0 if i == j else setup_matrix[i][j] for j in range(statusNum)] for i in
                    range(statusNum)]
    return setup_matrix

def set_work_speed_matrix(job_list, mach_list):
    work_speed_list = [[np.random.randint(1,4) if mach_list[j].availabityMatrix[job_list[i].setup] == True else 0 for i in range(len(job_list))] for j in range(len(mach_list))]
    for i in range(len(mach_list)):
        mach_list[i].workSpeedList = work_speed_list[i]

    return work_speed_list

class Gene:
    def __init__(self,job, mach):
        self.job = job
        self.mach = mach

    def getGene(self):
        return [self.job, self.mach]

class Chromosome:
    def __init__(self, id):
        self.id = id
        self.chromo = []

    def setChromo(self, gene):
        self.chromo.append(gene)

    def getChromo(self):
        return self.chromo