projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
for name,leader in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(name,leader))

print('----------------------------------------------')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for name,date,leader in zip(projects,dates,leaders):
    print('The leader of "{}" started {} is {}'.format(name, date, leader))

print('----------------------------------------------')

for i,(name,date,leader) in enumerate(zip(projects, dates, leaders)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1, name, date, leader))