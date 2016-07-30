class Person(object):
    _all = []

    def __init__(self,name,age,country,total):
        self._all.append(self)
        self.name = name
        self.age = age
        self.country = country
        self.total = total
