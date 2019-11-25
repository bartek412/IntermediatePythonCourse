cake01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7}
cake02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3}
cakes_list = [cake01, cake02]


def show_cake_info(acake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        acake['taste'], acake['glaze'], acake['text'], acake['weight']))


for cake in cakes_list:
    show_cake_info(cake)
