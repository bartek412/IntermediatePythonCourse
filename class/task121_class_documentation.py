class Cake:

    """
       Cake class for our bakery solution
    """

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        """

        :param name: name of cake
        :param kind:
        :param taste:
        :param additives:
        :param filling:
        """

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):

        """
        :return: the most important attributes of the object
        """

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

