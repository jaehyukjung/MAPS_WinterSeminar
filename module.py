import copy
import math
import random

class Prob_Instance:
    def __init__(self):
        self.objective = 'Makespan'
        self.job_list = [] # 작업 list
        self.machine_list = [] # 기계 list

    def __repr__(self):
        return str('Objective - ' + self.objective + ', Job - ' + str(self.job_list.__len__()) + ', Machine - ' + str(self.machine_list.__len__()))

    def deepcopy(self):
        return copy.deepcopy(self)

class Job: # 입력 데이터: job (요청)
    def __init__(self, ID: int, Process_time, Due_date):
        self.id = ID
        self.process_time = Process_time
        self.due_date = [0, Due_date]
        self.tardiness = 0

    def initialize(self):
        self.done = False
        self.priority = -1 # 우선순위
        self.start_time = self.due_date[0] # 시작 시간


class Machine: # 작업 기계
    def __init__(self, ID: int):
        self.id = ID
        self.work_speed = 1
        self.avail_time = 0 # 시작 가능 시간

    def initialize(self):
        self.now_capacity = self.max_capacity
        self.priority = -1
        self.measures = {}
        self.served_job = []
        self.can_work = True
        self.measures['makespan'] = 0
        self.measures['total_tardiness'] = 0

    def work(self, target: Job):
        if not self.doable(target): raise Exception('Infeasible Working!')
        target.done = True
        self.work_time = target.process_time / self.speed
        self.avail_time += self.work_time
        self.measures['total_tardiness'] += max(0, self.avail_time - target.due_date[1])
        self.measures['makespan'] = self.avail_time
        self.served_job.append(target.id)

    def doable(self, target: Job) -> bool: # -> return 값 힌트
        if target.done:
            return False
        else:
            return True

    def __repr__(self):
        return str('Machine # ' + str(self.id))