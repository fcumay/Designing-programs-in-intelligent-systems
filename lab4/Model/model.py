import random
import time


class Model:

    def __init__(self):
        self.x = GameMap()
        self.train = Train()
        self.flag = 0
        self.first_time = 0

    def save(self):
        with open("rec.txt", 'w+') as f:
            for station in self.x.stations:
                f.write(str(station.capacity) + '\n')
            f.write(str(self.train.capacity) + '\n')
            f.write(str(self.wasted()))

    def continue_game(self):
        data = []
        with open("rec.txt", 'r+') as f:
            for line in f:
                data.append(float(line))
        for line in range(len(self.x.stations)):
            self.x.stations[line].capacity = data[line]
        self.train.capacity = data[len(self.x.stations)]
        return data[len(self.x.stations) + 1]

    def run(self, flag):
        self.flag = flag
        if self.flag == 2:
            my_time = self.continue_game()

        else:
            my_time = 0
        self.first_time = time.time() - my_time

    def check_overload(self):
        return self.x.check_overloading(self.train)

    def wasted(self):
        final_time = time.time() - self.first_time
        return round(final_time, 1)

    def update(self):
        if self.check_overload():
            station = [f'Station {station.name.upper()} : {station.capacity}' for station in self.x.stations]
            station.append(f'Train: {self.train.capacity}')
            if self.train.curr_station == None:
                station.append(f'={self.x.stations[0].name}=')
                self.train.curr_station = self.x.stations[0]
            else:
                station.append(f'={self.train.curr_station.name}=')
        else:
            station = ['Oh,no!  :c', 'WASTED', 'Will you try again?', 'Now your score is', str(self.wasted()), '', '',
                       'WASTED']
        return station

    def check_stations(self, st):
        if self.train.curr_station == None:
            self.train.curr_station = self.x.stations[0]
        next_station = [station.name for station in self.x.graph[self.train.curr_station]]
        if st in next_station:
            for i in range(len(next_station)):
                if st == next_station[i]:
                    st = i
            return st + 1
        else:
            return False

    def next_station(self, station):
        key = self.check_stations(station)
        if not key:
            return False
        else:
            self.train.curr_station = self.x.graph[self.train.curr_station][key - 1]
            return True

    def check_load(self, num):
        return False if not (num.isdigit()) or int(num) > self.train.curr_station.capacity else True

    def check_unload(self, num):
        return False if not (num.isdigit()) or int(num) > self.train.capacity else True


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

    def check_overloading(self, train):
        for station in self.__stations:
            if station.capacity >= station.size or train.capacity >= 25:
                return False
        return True

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


class Train:

    def __init__(self, size=25, capacity=0):
        self.__size = size
        self.__capacity = capacity
        self.__curr_station = None

    def loading(self, num):
        if self.__capacity + num <= self.__size:
            self.__capacity += num
            self.__curr_station.capacity -= num
        else:
            buf = self.__size - self.__capacity
            self.__capacity = self.__size
            self.__curr_station.capacity += -buf + num

    def unloading(self, num):
        self.__capacity -= num
        self.__curr_station.capacity += num

    @property
    def curr_station(self):
        return self.__curr_station

    @curr_station.setter
    def curr_station(self, station):
        self.__curr_station = station

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity


class Station:
    def __init__(self, name, capacity=5, size=25):
        self.__capacity = capacity
        self.__size = size
        self.__name = name

    @property
    def size(self):
        return self.__size

    @property
    def capacity(self):
        return self.__capacity

    @property
    def name(self):
        return self.__name

    @size.setter
    def size(self, x):
        self.__size = x

    @capacity.setter
    def capacity(self, x):
        self.__capacity = x

    @name.setter
    def name(self, x):
        self.__name = x
