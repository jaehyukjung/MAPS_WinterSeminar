import random
import module
import solver
import mutation_solver
import crossover_solver


def random_LoadProb(id):
    random.seed(100)
    random_job = 15
    random_machine = 5

    ThisProb = module.Prob_Instance()
    ThisProb.chromo = module.Chromosome(id)
    for i in range(random_job):
        ThisProb.job_list.append(module.Job(i + 1, random.randint(2, 8), random.randint(6, 14), random.randint(1, 3),
                                            random.randint(0, 2), random.choice(module.STATUSLIST)))
    for i in range(random_machine):
        ThisProb.machine_list.append(module.Machine(i + 1, random.choice(module.STATUSLIST)))

    ThisProb.setup_metrix = module.set_setup_matrtix()
    ThisProb.machine_list = module.check_avail(ThisProb.machine_list)
    module.set_work_speed_matrix(ThisProb.job_list, ThisProb.machine_list)

    return ThisProb


if __name__ == "__main__":
    population = []
    for i in range(1, 501):
        Sample = random_LoadProb(i)
        Solution, chromo = solver.rule_solver(Sample, i)
        population.append((chromo, Solution))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))
    population = sorted(population, key=lambda x: x[0].objective)[:100]

    population2 = []
    for i in range(501, 601):
        Sample = random_LoadProb(i)
        Solution, chromo = mutation_solver.mut_solver(Sample, i, population[i - 501][0])
        population2.append((chromo, Solution))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))

    population3 = []
    for i in range(601, 700):
        Sample = random_LoadProb(i)
        Solution, chromo = crossover_solver.cross_solver(Sample, i, population[i - 601][0], population[i - 600][0])
        population3.append((chromo, Solution))
        print('Sum of Comepletion Time is ' + str(Solution['Objective']))
