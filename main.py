import random
import module
import solver
import numpy as np

def random_LoadProb(n):
    random.seed(n)
    random_job = random.randint(6,8)
    random_machine = random.randint(2,3)

    ThisProb = module.Prob_Instance()

    set_lst = ['A','B','C']
    for i in range(random_job):
        ThisProb.job_list.append(module.Job(i + 1, random.randint(2,8), random.randint(6,14), random.randint(1,3), random.randint(0,2), random.choice(set_lst)))
    for i in range(random_machine):
        ThisProb.machine_list.append(module.Machine(i + 1),random.choice(set_lst))

    return ThisProb

if __name__ == "__main__":
    random.seed(42)

    n = random.randint(1, 1000)
    Sample = random_LoadProb(n)
    Solution = solver.rule_solver(Sample)
    #print('Solved and objective value is ' + str(Solution['Objective']))

