from random import randint, sample, uniform


class Product(object):

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = randint(1000000, 10000000)

    def stealability(self):
        steal_rating = self.price / self.weight

        low = 0.5
        mid = 1.0

        one = 'not that stealable.'
        two = 'kinda stealable.'
        three = 'very stealable.'

        if steal_rating < low:
            return one
        elif steal_rating >= low and steal_rating < mid:
            return two
        else:
            return three

    def explode(self):
        flammability_rating = self.flammability * self.weight

        low = 10
        mid = 50

        one = '...fizzle'
        two = '...boom!'
        three = '...DOOOOOOM!!'

        if flammability_rating < low:
            return one
        elif flammability_rating >= low and flammability_rating < mid:
            return two
        else:
            return three


class BoxingGlove(Product):

    def __init__(self, name):
        super().__init__(name)
        print(self.price)
        self.weight = 10

    def explode(self):
        return print(f'...its a glove')

    def punch(self):
        steal_rating = self.price / self.weight
        low = 5
        mid = 1
        if steal_rating < low:
            return print(f'That Tickles.')
        elif steal_rating >= low and steal_rating < mid:
            return print(f'Hey that hurt!')
        else:
            return print(f'OUCH!')
