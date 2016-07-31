

FUDD = 'Elmer Fudd'
PORKY = 'Porky Pig'
BUGS = 'Bugs Bunny'

class RabbitSeason(Exception):
    pass

class Duck(object):
    def __init__(self):
        self.a = 1
        self.b = 2

    def add(self):
        return self.a + self.b

    def throw_rabbit(self):
        raise RabbitSeason

    def evade(self, pursuer):
        if pursuer == FUDD:
            self.throw_rabbit()
        if pursuer == PORKY:
            return False
        return True

def foobar(*args, **kwargs):
    if args:
        print(args)
    else:
        print('no *args')
    if kwargs:
        print(kwargs)
    else:
        print('no *kwargs')
