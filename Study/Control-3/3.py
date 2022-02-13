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
    def is_ripe(self):
        if self._state == 3:
            print('Помидор созрел!')

class TomatoBush:
    def __init__(self, tomatoes):
        self.tomatoes = [Tomato(i) for i in range(tomatoes)]
    def grow_all(self):
        for k in self.tomatoes:
