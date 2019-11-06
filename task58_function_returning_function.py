from datetime import datetime


def create_function(span):
    convert = {'m': 60, 'h': 3600, 'd': 86400}
    source = '''
def f(start, end):
    duration_in_s = (end - start).total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(convert[span])
    exec(source, globals())
    return f


f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
