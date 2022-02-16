class Tomato:
    states = {1: 'Помидор зелёный', 2: 'Помидор ещё желтый', 3: 'Помидор созрел'}
    key = []
    for j in states.keys():
        key.append(j)
    def __init__(self, index):
        self._index = index
        self._state = self.key[0]
    def grow(self):
        if self._state < 3:
            self._state += 1
        return self._state
    def is_ripe(self):
        if self._state == 3:
            return True

class TomatoBush:
    def __init__(self, tomatoes):
        self.tomatoes = [Tomato(i) for i in range(tomatoes)]
    def grow_all(self):
        for k in self.tomatoes:
            k.grow()
    def all_are_ripe(self):
        true = []
        for a in self.tomatoes:
            if a.is_ripe() == True:
                true.append(True)
            else:
                true.append(False)
        if False in true: return False
        else: return True
    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe() == True:
            self._plant.give_away_all()
            print('Урожай собран!')
        else:
            print('Ещё не все плоды созрели!')
    @staticmethod
    def knowledge_base():
        pass

Gardener.knowledge_base()
tomatoes = TomatoBush(5)
gardener = Gardener('Maksim', tomatoes)
gardener.work()
gardener.harvest()
while tomatoes.all_are_ripe() == False:
    gardener.work()
gardener.harvest()
