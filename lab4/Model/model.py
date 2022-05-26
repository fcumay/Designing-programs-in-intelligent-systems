import random
import time
from os import system


class Model:

    def __init__(self):
        self.x = GameMap()
        self.train = Train(self.x)
        self.flag = 0
        self.first_time = 0

    def menu(self):
        while x.check_overloading(train):

            x.spawn()
            print(f'Поезд на {train.curr_station.name} станции              В поезде {train.capacity}')
            x.show_condition()
            print('Что сделать?')
            key = input('(1) Следующая станция\n(2) Загрузить поезд\n(3) Разгрузить поезд\n')
            if key == '1':
                train.show_stations()
                stations_state = int(input('\nКуда поедем?\n'))
                while (stations_state >= train.follow_stations):
                    stations_state = int(input('\nХорошо подyмайте\n'))
                train.go_to_station(stations_state)
                print('...едем...')
                time.sleep(2)
                continue
            elif key == '2':
                train.loading()
                print('загружаю...')
                time.sleep(3)
            elif key == '3':
                train.unloading()
                print('разгружаю...')
                time.sleep(3)
            elif key == 'p':
                print('Игра сохранена')
                save(x, train, time.time() - first_time)
                exit()
            x.check_overloading(train)

        print('ПОТРАЧЕНО')

    def save(self, x, train, time):
        with open("rec.txt", 'w+') as f:
            for station in x.stations:
                f.write(str(station.capacity) + '\n')
            f.write(str(train.capacity) + '\n')
            f.write(str(time))

    def continue_game(self):
        data = []
        with open("rec.txt", 'r+') as f:
            for line in f:
                data.append(float(line))
        for line in range(len(self.x.stations)):
            self.x.stations[line].capacity = data[line]
        self.train.capacity = data[len(self.x.stations)]
        print(self.train.follow_stations)
        return data[len(self.x.stations) + 1]

    def run(self, flag):
        self.flag = flag
        if self.flag == 2:
            my_time = self.continue_game()

        else:
            my_time = 0
        self.first_time = time.time() - my_time
        final_time = time.time() - self.first_time
        print('Ваш счёт:', round(final_time, 1))


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
    def __init__(self, game_map, size=25, capacity=0):
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__size = size
        self.__capacity = capacity

    def go_to_station(self, key):
        stations = self.show_stations()

        for i in range(len(stations)):
            if str(key).lower() == stations[i]:
                key = i
                

        self.__curr_station = self.__game_map.graph[self.__curr_station][key]
        self.show_stations()

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

    def show_stations(self):
        next_station = [station.name for station in self.__game_map.graph[self.__curr_station]]
        return next_station

    @property
    def follow_stations(self):
        return len(self.__game_map.graph[self.__curr_station])

    @property
    def curr_station(self):
        return self.__curr_station

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @curr_station.setter
    def curr_station(self, station):
        self.__curr_station = station


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
