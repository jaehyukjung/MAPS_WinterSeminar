import random
import module
import solver

def random_LoadProb(n):
    random.seed(n)
    random_job = random.randint(6,8)
    random_machine = random.randint(2,3)

    ThisProb = module.Prob_Instance()

    for i in range(random_machine):
        ThisProb.machine_list.append(module.Machine(i + 1))

if __name__ == "__main__":
    random.seed(42)
    Sample = module()
    Solution = solver.rule_solver(Sample)
    print('Solved and objective value is ' + str(Solution['Objective']))

