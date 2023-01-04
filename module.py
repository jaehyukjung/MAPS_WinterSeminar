import copy
import random

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
    def __init__(self, ID: int, Process_time, Due_date, Pre_Job:list, Setup_Status:str, Weight = -1,Release_time = -1 ):
        self.id = ID
        self.process_time = Process_time
        self.due_date = Due_date
        self.release_date = Release_time
        self.setup = Setup_Status
        self.pre_job = Pre_Job # 이전에 필요한 작업 리스트 => 머신의 셋업? 에 따라 바뀌는 것도 고려해서 추가해야 할 덧
        self.weight = Weight # 가중치

    def initialize(self):
        self.done = False
        self.priority = -1 # 우선순위
        self.start_time = -1 # 시작 시간
        self.tardiness = -1

class Machine: # 작업 기계
    def __init__(self, ID: int, Work_speed = 1):
        self.id = ID
        self.work_speed = Work_speed
        self.avail_time = 0 # 시작 가능 시간

    def initialize(self):
        self.measures = {}
        self.served_job = []
        self.can_work = True
        self.measures['makespan'] = 0
        self.measures['total_tardiness'] = 0

    def work(self, target: Job):
        if not self.doable(target): raise Exception('Infeasible Working!')
        target.done = True
        self.work_time = target.process_time / self.work_speed
        target.start_time = self.avail_time # set -> setup 후
        self.avail_time += self.work_time  # 완료시간
        target.tardiness = max(0, self.avail_time - target.due_date)
        self.measures['total_tardiness'] += target.tardiness
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def doable(self, target: Job) -> bool: # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))

class Setup_Machine(Machine): # 작업 기계
    def __init__(self, ID: int, SETUP: str):
        Machine.__init__(self,ID)
        self.setup = SETUP

    def initialize(self):
        Machine.initialize(self)
        self.setup_time = 3

    def work(self, target: Job):
        if not self.doable(target): raise Exception('Infeasible Working!')
        target.done = True
        self.work_time = target.process_time / self.work_speed

        if self.setup != target.setup:
            self.setup = target.setup
            self.avail_time += self.setup_time

        target.start_time = self.avail_time # set -> setup 후
        self.avail_time += self.work_time  # 완료시간
        target.tardiness = max(0, self.avail_time - target.due_date)
        self.measures['total_tardiness'] += target.tardiness
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def doable(self, target: Job) -> bool: # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))