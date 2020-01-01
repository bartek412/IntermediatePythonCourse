import pickle
import glob
import types


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_content = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer = """
</table>"""

    with open(path, "w") as f:
        f.write(template_header)
        for instance in cls.bakery_offer:
            content = template_content.format(instance.name, instance.kind, instance.taste, instance.additives,
                                              instance.filling)
            f.write(content)
        f.write(template_footer)


class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives=[], filling='', gluten_free=False, text=''):
        self.name = name
        self.kind = kind if kind in self.known_kinds else 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''

    @property
    def Text(self):
        return self._text()

    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives_list):
        self.additives.extend(additives_list)

    def show_info(self):
        print(self.name.upper())
        print('Kinds:   ', self.kind)
        print('Taste:   ', self.taste)
        if self.additives:
            print('Additives:   ', self.additives)
        if self.filling:
            print('Filling:     ', self.filling)
        print('GlutenFree:      ', self.__gluten_free)
        print('Text:        ', self.__text)
        print('-' * 25)

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path + '*.bakery')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False, 'happy new year')
cake02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'])
cake03 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', gluten_free=True, text='xd')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

cake02.set_filling('vanilla cream')
cake03.add_additives(['cocoa powder', 'coconuts'])

cake01.Text = 'Happy birthday'
cake02.Text = 'Happy birthday'

for cake in Cake.bakery_offer:
    # print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(cake.name, cake.kind, cake.taste,
    #                                                                        cake.additives, cake.filling))
    cake.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(Cake))

cake01.save_to_file('cake01.bakery')
cake02.save_to_file('cake02.bakery')
cake05 = Cake.read_from_file('cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files(''))

# static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, 'c:/temp/cake01.html')

# class method
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html('c:/temp/all_cakes.html')