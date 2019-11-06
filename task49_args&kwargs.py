def calculate_paint(efficency_ltr_per_m2, *args):
    return sum(args)*efficency_ltr_per_m2


print(calculate_paint(2, 10, 12, 28))
area = [18, 21, 32, 42]
print(calculate_paint(2, *area))


def log_it(*args):
    with open(r'C:\Users\barte\Documents', 'a') as f:
        for string in args:
            f.write(string + ' ')
        f.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')