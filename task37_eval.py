import math
argument_list = []
for i in range(100):
    argument_list.append(i/10)
formula = input("podaj wzor (niewiadoma oznacz 'x'): ")
for x in argument_list:
    print('{0:3.2f} - {1:6.2f}'.format(x, eval(formula)))
