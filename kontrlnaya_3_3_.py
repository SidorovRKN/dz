class Tomato:
    states = {0: 'посажен', 1: "первые ростки", 2: "зацвел", 3: "зеленые плоды", 4: "красные плоды"}

    def __init__(self, index):
        self._index = index
        self.s = 0
        self._state = self.states[self.s]

    def grow(self):
        self.s += 1
        self._state = self.states[self.s]

    def is_ripe(self):
        if self._state == self.states[4]:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        counter = 0
        for i in self.tomatoes:
            if i.is_ripe():
                counter += 1
        if counter == len(self.tomatoes):
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('не все созрели')

    @staticmethod
    def knowledge_base():
        print('fhvbuefhwwreiuohvnueilhdnrvfoue')


tomatos = TomatoBush(10)
ivanich = Gardener(name="Иваныч", plant=tomatos)
ivanich.work()
ivanich.work()
ivanich.work()
print(tomatos.all_are_ripe())
ivanich.harvest()
ivanich.work()
ivanich.harvest()
print(tomatos.tomatoes)
print('РАСИЯ')