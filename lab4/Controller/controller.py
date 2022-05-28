from Model.model import Model


class Controller:
    def __init__(self, model):
        self.model = model

    def new_game(self):
        self.model.run(1)

    def continue_game(self):
        self.model.run(2)

    def update(self):
        station = [station.capacity for station in self.model.x.stations]
        station.append(self.model.train.capacity)
        if self.model.train.curr_station == None:
            station.append(self.model.x.stations[0].name)
            self.model.train.curr_station = self.model.x.stations[0]
        else:
            station.append(self.model.train.curr_station.name)
        return station

    def next_station(self, station):
        key = self.check_stations(station)
        if not key:
            return False
        else:
            self.model.train.curr_station = self.model.x.graph[self.model.train.curr_station][key - 1]
            self.spawn()
            return True

    def check_stations(self, st):
        if self.model.train.curr_station == None:
            self.model.train.curr_station = self.model.x.stations[0]
        next_station = [station.name for station in self.model.x.graph[self.model.train.curr_station]]
        if st in next_station:
            for i in range(len(next_station)):
                if st == next_station[i]:
                    st = i
            return st + 1
        else:
            return False

    def spawn(self):
        self.model.x.spawn()
        self.save()

    def load(self, num):
        if self.check_load(num):
            self.model.train.loading(int(num))
            return True
        else:
            return False

    def check_load(self, num):
        return False if not (num.isdigit()) or int(num) > self.model.train.curr_station.capacity else True

    def unload(self, num):
        if self.check_unload(num):
            self.model.train.unloading(int(num))

            return True
        else:
            return False

    def check_unload(self, num):
        return False if not (num.isdigit()) or int(num) > self.model.train.capacity else True

    def check_overload(self):
        return True if self.model.check_overload() else False

    def wasted(self):
        return str(self.model.wasted())

    def save(self):
        self.model.save()
