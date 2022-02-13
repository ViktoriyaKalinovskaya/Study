class Tomato:
    states = {1: 'зелёный помидор', 2: 'желтый помидор', 3: 'спелый помидор'}
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
            print('Помидор созрел!')

class TomatoBush(Tomato):
    def __init__(self, tomatoes):
        super().__init__(tomatoes)
        self.tomatoes = [Tomato(i) for i in range(tomatoes)]
    def grow_all(self):
        for k in self.tomatoes:
            k._state += 1
    def all_are_ripe(self):
        true = []
        for a in self.tomatoes:
            if a._state == 3:
                true.append(True)
                if True in true: print(True)
                else: print(False)
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
        else: print('Ещё не все плоды созрели!')
    @staticmethod
    def knowledge_base():
        pass

Gardener.knowledge_base()
tomatoes = TomatoBush(5)
gardener = Gardener('Maksim', tomatoes)
print(tomatoes.grow())
