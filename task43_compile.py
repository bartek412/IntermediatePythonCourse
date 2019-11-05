import math
import time
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range(1000000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min: {} max: {} '.format(min(results_list), max(results_list)))
    stop = time.time()
    print('Czas obliczen: {}'.format(stop-start))

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, 'internal variable', 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min: {} max: {} '.format(min(results_list), max(results_list)))
    stop = time.time()
    print('Czas obliczen: {}'.format(stop-start))