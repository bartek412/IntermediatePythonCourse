class Cake:
    def __init__(self, name, kind, taste, addictions=[], filling=''):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'])
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet')

bakery_offer = [cake01, cake02, cake03]
for cake in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(cake.name, cake.kind, cake.taste,
                                                                                 cake.addictions, cake.filling))