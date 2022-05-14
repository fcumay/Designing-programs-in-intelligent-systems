class Train:
    def __init__(self, game_map, size=25, capacity=0):
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__size = size
        self.__capacity = capacity

    def go_to_station(self, key):
        self.__curr_station = self.__game_map.graph[self.__curr_station][key]

    def loading(self):
        print('На станции:', self.__curr_station.capacity)
        print('В поезде:', self.capacity)
        kolvo = int(input('Сколько загрузить: '))
        while kolvo < 0 or self.__curr_station.capacity - kolvo < 0:
            print('На станции:', self.__curr_station.capacity)
            print('В поезде', self.capacity)
            kolvo = int(input('Сколько загрузить: '))
        if self.__capacity + kolvo <= self.__size:
            self.__capacity += kolvo
            self.__curr_station.capacity -= kolvo
        else:
            buf = self.__size - self.__capacity
            self.__capacity = self.__size
            self.__curr_station.capacity += -buf + kolvo

    def unloading(self):
        print('На станции:', self.__curr_station.capacity)
        print('В поезде:', self.capacity)
        kolvo = int(input('Сколько выгрузить '))
        while kolvo < 0 or self.__capacity - kolvo < 0:
            print('На станции:', self.__curr_station.capacity)
            print('в поезде сейчас столько груза:', self.capacity)
            kolvo = int(input('В поезде: '))
        self.__capacity -= kolvo
        self.__curr_station.capacity += kolvo

    # def __str__(self):
    #     for station in self.__game_map.graph[self.__curr_station]:
    #         return f"{station.name} "
    def show_stations(self):
        for station in self.__game_map.graph[self.__curr_station]:
            print(station.name, end=' ')

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
    def curr_station(self,station):
        self.__curr_station=station