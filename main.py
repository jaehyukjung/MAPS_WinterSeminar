import copy
from solver import *
from mutation_solver import *
from crossover_solver import *
from gantt_chart import *

def random_LoadProb(id:int) -> Prob_Instance:
    random.seed(100)
    random_job = 15
    random_machine = 5

    ThisProb = Prob_Instance()
    copiedProb = copy.deepcopy(ThisProb)
    ThisProb.chromo = Chromosome(id)
    for i in range(random_job):
        ThisProb.job_list.append(Job(i + 1, random.randint(2, 8), random.randint(6, 14), random.randint(1, 3),
                                            random.randint(0, 2), random.choice(STATUSLIST)))
    for i in range(random_machine):
        ThisProb.machine_list.append(Machine(i + 1, random.choice(STATUSLIST)))

    ThisProb.setup_metrix = set_setup_matrtix()
    ThisProb.machine_list = check_avail(ThisProb.machine_list)
    set_work_speed_matrix(ThisProb.job_list, ThisProb.machine_list)

    return ThisProb

if __name__ == "__main__":
    population = []
    for i in range(1, 501):  # random 생성 후 상위 100개
        Sample = random_LoadProb(i)
        mach_setup = [[i.setup_status] for i in Sample.machine_list]
        Solution, chromo, mach_list, sch_list = rule_solver(Sample, i)
        population.append((chromo, Solution, sch_list))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))
    population = sorted(population, key=lambda x: x[0].objective)[:100]

    for i in range(10): # generation = 10
        population2 = []
        for i in range(501, 601): # mutate population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo,mach_list, sch_list = mut_solver(Sample, i, population[i - 501][0])
            population2.append((chromo, Solution, sch_list))
            print('Sum of Comepletion Time is ' + str(Solution['Objective']))

        population3 = []
        for i in range(601, 700): # crossover population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo, mach_list, sch_list = cross_solver(Sample, i, population[i - 601][0], population[i - 600][0])
            population3.append((chromo, Solution, sch_list))
            print('Sum of Comepletion Time is ' + str(Solution['Objective']))

        population4 = []
        for i in range(700, 800): # random population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo, mach_list, sch_list = rule_solver(Sample, i)
            population4.append((chromo, Solution,sch_list))
            print('Sum of Comepletion Time is ' + str(Solution['Objective']))

        population5 = population + population2 + population3 + population4
        population = sorted(population5, key=lambda x: x[0].objective)[:100]
        ganttChart(population[0][2], population[0][1], mach_setup) # 제일 좋은 결과값 간트 차트
