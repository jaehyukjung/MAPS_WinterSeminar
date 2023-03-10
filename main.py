import copy
from solver import *
from mutation_solver import *
from crossover_solver import *
from gantt_chart import *
from spt_solver import *
from min_setup_solver import *

SEED = 100
def random_LoadProb(id: int) -> Prob_Instance:
    random.seed(SEED)
    random_job = 15
    random_machine = 5

    ThisProb = Prob_Instance()
    ThisProb.chromo = Chromosome(id)
    for i in range(random_job):
        ThisProb.job_list.append(Job(i + 1, random.uniform(30, 60), random.randint(6, 14), random.randint(1, 3),
                                     random.randint(0, 2), random.choice(STATUSLIST)))
    for i in range(random_machine):
        ThisProb.machine_list.append(Machine(i + 1, random.choice(STATUSLIST)))

    ThisProb.setup_metrix = set_setup_matrix()
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
        # print('Sum of Comepletion Time is ' + str(Solution['Objective']))
    population = sorted(population, key=lambda x: x[0].objective)[:100]

    for j in range(10):  # generation = 10

        for i in range(100):  # mutate population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo, mach_list, sch_list = mut_solver(Sample, i, population[i][0])
            population.append((chromo, Solution, sch_list))
            # print('Sum of Comepletion Time is ' + str(Solution['Objective']))

        for i in range(100):  # crossover population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo, mach_list, sch_list = cross_solver(Sample, i, population[i][0], population[i + 1][0])
            population.append((chromo, Solution, sch_list))
            # print('Sum of Comepletion Time is ' + str(Solution['Objective']))
            # ganttChart(population[0][2], population[0][1], mach_setup)  # 제일 좋은 결과값 간트 차트

        for i in range(100):  # random population 생성
            Sample = random_LoadProb(i)
            mach_setup = [[i.setup_status] for i in Sample.machine_list]
            Solution, chromo, mach_list, sch_list = rule_solver(Sample, 500 + j * 100 + i)
            population.append((chromo, Solution, sch_list))
            # print('Sum of Comepletion Time is ' + str(Solution['Objective']))

        population = sorted(population, key=lambda x: x[0].objective)[:100]

    population = sorted(population, key=lambda x: x[0].objective)[:100]

    for i in range(10):
        print('Sum of Comepletion Time is ' + str(population[i][1]['Objective']))

    population = []
    for i in range(1):
        Sample = random_LoadProb(i)
        mach_setup = [[i.setup_status] for i in Sample.machine_list]
        Solution, chromo, mach_list, sch_list = spt_solver(Sample, i)
        population.append((chromo, Solution, sch_list))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))
        # ganttChart(population[0][2], population[0][1], mach_setup)  # 제일 좋은 결과값 간트 차트
    population = []
    for i in range(1):
        Sample = random_LoadProb(i)
        mach_setup = [[i.setup_status] for i in Sample.machine_list]
        Solution, chromo, mach_list, sch_list = min_setup_solver(Sample, i)
        population.append((chromo, Solution, sch_list))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))
        # ganttChart(population[0][2], population[0][1], mach_setup)  # 제일 좋은 결과값 간트 차트

