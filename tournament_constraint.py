import constraint
import time

problem = constraint.Problem()

def make_var(i, j, m):
  return 'p_{}_{}_{}'.format(i, j, m)

num_teams = 15
num_days = 14

for i in range(1, num_teams):
  for j in range(1, num_teams):
    for m in range(1, num_days):
      variable = make_var(i, j, m)
      problem.addVariable(variable, [0, 1])


for m in range(1, num_days):
  same = [make_var(i, i, m) for i in range(1, num_teams)]
  problem.addConstraint(constraint.InSetConstraint([0]), same)

for m in range(1, num_days):
  for i in range(1, num_teams):
    oneTeam = [make_var(i, j, m) for j in range(1, num_teams)]
    problem.addConstraint(constraint.InSetConstraint([0, 1]), oneTeam)

for i in range(1, num_teams):
  for j in range(i + 1, num_teams):
    pairs = [make_var(i, j, m) for m in range(1, num_days)]
    pairs += [make_var(j, i, m) for m in range(1, num_days)]
    problem.addConstraint(constraint.MaxSumConstraint(1), pairs)


now = time.time()
sol = problem.getSolution()
later = time.time()
difference = int(later - now)
print(difference)
