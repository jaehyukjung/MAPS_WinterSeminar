import random
import module
import solver
import numpy as np

def random_LoadProb(id):
    random.seed(100)
    random_job = random.randint(6,8)
    random_machine = random.randint(2,3)

    ThisProb = module.Prob_Instance()
    ThisProb.chromo = module.Chromosome(id)
    for i in range(random_job):
        pre_list = []
        if i >= 2:
            pre_list = [id for id in range(1,i+1)]
            pre_list =  random.sample(pre_list, random.randint(0,2))
        ThisProb.job_list.append(module.Job(i+1, random.randint(2,8), random.randint(6,14), random.randint(1,3),
                                            random.randint(0,2), random.choice(module.statusList), pre_list))
    for i in range(random_machine):
        ThisProb.machine_list.append(module.Machine(i + 1,random.choice(module.statusList)))

    return ThisProb

if __name__ == "__main__":
    random.seed(666)
    population =[]
    for i in range(1,101):
        Sample = random_LoadProb(i)
        Solution, chromo = solver.rule_solver(Sample,i)
        population.append(chromo)
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))

    print(1)