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

    def __repr__(self):
        return str(
            'Objective - ' + self.objective + ', Job - ' + str(self.job_list.__len__()) + ', Machine - ' + str(
                self.machine_list.__len__()) + '\n')

    def deepcopy(self):
        return copy.deepcopy(self)

class Job: # 입력 데이터: job (요청)
<<<<<<< HEAD
    def __init__(self, ID: int, Process_time, Due_date, Weight, Release_time,Setup_Status:int, Pre_list:list):
=======
    def __init__(self, ID: int, Process_time, Due_date, Weight, Release_time, Setup_Status:str):
>>>>>>> b25e921acd8c3ee661456ffb2a09ad27e4b4bad3
        self.id = ID
        self.process_time = Process_time
        self.due_date = Due_date
        self.release_date = Release_time
        self.setup = Setup_Status
<<<<<<< HEAD
=======
        # self.pre_job = Pre_Job # 이전에 필요한 작업 리스트 => 머신의 셋업? 에 따라 바뀌는 것도 고려해서 추가해야 할 덧
>>>>>>> b25e921acd8c3ee661456ffb2a09ad27e4b4bad3
        self.weight = Weight # 가중치
        self.pre_list = Pre_list # 선행작업

    def initialize(self):
        self.done = False
        self.priority = -1 # 우선순위
        self.start_time = -1 # 시작 시간
        self.tardiness = -1

    def __repr__(self):
        return str('Job # ' + str(self.id))

class Machine: # 작업 기계
<<<<<<< HEAD
    def __init__(self, ID: int, setUpStatus: int):
        self.start_time = None
        self.workSpeedList = None
        self.availabityMatrix = None
        self.settingTimeMatrix = None
        self.id = ID
        self.setupstatus = setUpStatus
=======
    def __init__(self, ID: int, Work_speed, SetUp: str):
        self.id = ID
        self.work_speed = Work_speed
        self.setup = SetUp
>>>>>>> b25e921acd8c3ee661456ffb2a09ad27e4b4bad3
        self.avail_time = 0 # 시작 가능 시간

    def initialize(self):
        self.measures = {}
        self.served_job = []
        self.can_work = True
        self.measures['makespan'] = 0
        self.measures['total_tardiness'] = 0
        self.setAvialabilityMatrix()
        self.setWorkSpeedList()
        self.work_speed = self.workSpeedList[0]

    def work(self, target: Job):
        target.done = True
<<<<<<< HEAD
        self.work_speed = self.workSpeedList[target.setup]
        self.work_time = target.process_time / self.work_speed  # 작업시간

        if self.setupstatus != target.setup: # 기계의 setup과 Job의 setup 차이 계산
           self.avail_time += self.settingTimeMatrix[self.setupstatus][target.setup]
           self.setupstatus = target.setup

        self.start_time = self.avail_time # set -> setup 후
        target.start_time = self.start_time
=======
        self.work_time = target.process_time / self.work_speed

        if self.setup != target.setup:
            self.setup = target.setup
            self.avail_time += self.setup_time

        self.start_time = self.avail_time # set -> setup 후
>>>>>>> b25e921acd8c3ee661456ffb2a09ad27e4b4bad3
        self.avail_time += self.work_time  # 완료시간
        target.tardiness = max(0, self.avail_time - target.due_date)
        self.measures['total_tardiness'] += target.tardiness
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def setAvialabilityMatrix(self): # Job에 대한 기계의 작업 가능 여부(Mj)
        self.availabityMatrix = [random.choice([True, False]) for i in range(statusNum)]

    def setWorkSpeedList(self): # 각 기계의 Job에 대한 작업 속도
        workSpeedList = [np.random.randint(1,4) for i in range(statusNum)]
        self.workSpeedList = workSpeedList

    def GETSETTime(self, previousJob, currentJob: Job): # 기계가 작업할때 setupTime 계산
        return self.settingTimeMatrix[previousJob][currentJob.setup]

    def doable(self, target: Job) -> bool: # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))

def settingMatrtix(): # 각 작업별 setupTimeMatrix
    setup_matrix = np.random.randint(1, 4, size=(statusNum, statusNum))
    setup_matrix = np.triu(setup_matrix)
    setup_matrix += setup_matrix.T - np.diag(setup_matrix.diagonal())
    setup_matrix = [[0 if i == j else setup_matrix[i][j] for j in range(statusNum)] for i in
                    range(statusNum)]
    return setup_matrix

# class Machine: # 작업 기계
#     def __init__(self, ID: int, Work_speed = 1):
#         self.id = ID
#         self.work_speed = Work_speed
#         self.avail_time = 0 # 시작 가능 시간
#
#     def initialize(self):
#         self.measures = {}
#         self.served_job = []
#         self.can_work = True
#         self.measures['makespan'] = 0
#         self.measures['total_tardiness'] = 0
#
#     def work(self, target: Job):
#         if not self.doable(target): raise Exception('Infeasible Working!')
#         target.done = True
#         self.work_time = target.process_time / self.work_speed
#         target.start_time = self.avail_time # set -> setup 후
#         self.avail_time += self.work_time  # 완료시간
#         target.tardiness = max(0, self.avail_time - target.due_date)
#         self.measures['total_tardiness'] += target.tardiness
#         self.measures['makespan'] = self.avail_time
#         self.served_job.append(target.id)
#
#     def setAvialabilityMatrix(self): # Job에 대한 기계의 작업 가능 여부(Mj)
#         self.availabityMatrix = [True for i in range(statusNum)]
#
#     def setWorkSpeedList(self): # 각 기계의 Job에 대한 작업 속도
#         workSpeedList = [np.random.randint(1,4) for i in range(statusNum)]
#         self.workSpeedList = workSpeedList
#
#     def doable(self, target: Job) -> bool: # -> return 값 힌트
#         if target.done:
#             return False
#         else:
#             return True
#
#     def __repr__(self):
#         return str('Machine # ' + str(self.id))
#
# class Setup_Machine(Machine): # 작업 기계
#     def __init__(self, ID: int, SETUP: str):
#         Machine.__init__(self,ID)
#         self.setup = SETUP
#
#     def initialize(self):
#         Machine.initialize(self)
#         self.setup_time = 3
#
#     def work(self, target: Job):
#         if not self.doable(target): raise Exception('Infeasible Working!')
#         target.done = True
#         self.work_time = target.process_time / self.work_speed
#
#         if self.setup != target.setup:
#             self.setup = target.setup
#             self.avail_time += self.setup_time
#
#         target.start_time = self.avail_time # set -> setup 후
#         self.avail_time += self.work_time  # 완료시간
#         target.tardiness = max(0, self.avail_time - target.due_date)
#         self.measures['total_tardiness'] += target.tardiness
#         self.measures['makespan'] = self.avail_time
#         self.served_job.append(target.id)
#
#     def setAvialabilityMatrix(self): # Job에 대한 기계의 작업 가능 여부(Mj)
#         self.availabityMatrix = [random.choice([True,False]) for i in range(statusNum)]
#
#     def GETSETTime(self, previousJob, currentJob: Job): # 기계가 작업할때 setupTime 계산
#         return self.settingTimeMatrix[previousJob][currentJob.setup]
#
#     def doable(self, target: Job) -> bool: # -> return 값 힌트
#         if target.done:
#             return False
#         else:
#             return True
#
#     def __repr__(self):
#         return str('Machine # ' + str(self.id))
