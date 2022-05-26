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
        station.append(self.model.train.curr_station.name)
        return station

    def next_station(self, station):
        if self.check_follow_station(station):
            self.model.train.go_to_station(station)
            self.spawn()
            return True
        else:
            return False

    def check_follow_station(self, station):
        return True if station.lower() in self.model.train.show_stations() else False

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
