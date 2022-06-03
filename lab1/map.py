import random
from station import Station


class GameMap:
    def __init__(self):
        a = Station('a')
        b = Station('b')
        c = Station('c')
        d = Station('d')
        e = Station('e')
        f = Station('f')
        self.__stations = [a, b, c, d, e, f]
        self.__graph = {self.__stations[0]: [self.__stations[1], self.__stations[2]],
                        self.__stations[1]: [self.__stations[0], self.__stations[3], self.__stations[4]],
                        self.__stations[2]: [self.__stations[0], self.__stations[5]],
                        self.__stations[3]: [self.__stations[1]],
                        self.__stations[4]: [self.__stations[1], self.__stations[5]],
                        self.__stations[5]: [self.__stations[2], self.__stations[4]]}

    def spawn(self):
        self.__stations[random.randint(0, 5)].capacity += 5

    @property
    def graph(self):
        return self.__graph

    @property
    def stations(self):
        return self.__stations

    @graph.setter
    def graph(self, x):
        self.__graph = x

    @stations.setter
    def stations(self, x):
        self.__stations = x

    def show_condition(self):
        for station in self.__stations:
            print(f'На станции [{str(station.name)}] -- {str(station.capacity)} товаров.')
