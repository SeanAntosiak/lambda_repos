import random as rnd


class Product:
    '''
    A class containing information on company products
    '''

    def __init__(self,
                 name,
                 price=10,
                 weight=20,
                 flammability=0.5,
                 identifier=rnd.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        A function(method) that determines how likley a product is to be stolen
        '''

        val = self.price/self.weight

        if val < 0.5:
            return('Not so stealable...')

        elif (val >= 0.5) & (val < 1):
            return('Kinda stealable.')

        else:
            return('Very stealable!')

    def explode(self):
        '''
        A function that determines how big of an explosion a product will cause
        '''
        val = self.weight*self.flammability

        if val < 10:
            return('...fizzle.')

        elif (val >= 10) & (val < 50):
            return('...boom!')

        else:
            return('...BABOOM!!')


class BoxingGlove(Product):
    '''
    Creates the boxing glove class
    '''

    def __init__(self,
                 name,
                 price=10,
                 weight=10,
                 flammability=0.5,
                 identifier=rnd.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

        super()

    def explode(self):
        '''
        Reminds you that boxing gloves are not inherantly explosive
        '''

        return("...it's a glove")

    def punch(self):
        '''
        Lets you know how hard you are going to get hit
        '''

        if self.weight < 5:
            return('That tickles.')

        elif (self.weight >= 5) & (self.weight < 15):
            return('Hey that hurt!')

        else:
            return('OUCH!')
