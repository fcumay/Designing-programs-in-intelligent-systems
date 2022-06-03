class Train:
    def __init__(self, game_map, size=25, capacity=0):
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__size = size
        self.__capacity = capacity

    def loading(self, num):
        if self.__capacity + num <= self.__size and num < self.__curr_station.capacity:
            self.__capacity += num
            self.__curr_station.capacity -= num
            return True

    def unloading(self, num):
        if self.__capacity >= num and self.__curr_station.capacity + num <= self.__curr_station.size:
            self.__capacity -= num
            self.__curr_station.capacity += num
            return True

    def check_stations(self, st):
        next_station = [station.name for station in self.__game_map.graph[self.__curr_station]]
        if st in next_station:
            for i in range(len(next_station)):
                if st == next_station[i]:
                    st = i
            return st + 1
        else:
            return False

    def next_station(self, station):
        key = self.check_stations(station)
        if key:
            self.__curr_station = self.__game_map.graph[self.__curr_station][key - 1]
        else:
            pass

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