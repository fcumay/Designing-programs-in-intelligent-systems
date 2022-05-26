from Model.model import Model
class Controller:
    def __init__(self,model):
        self.model=model

    def new_game(self):
        self.model.run(1)

    
    def continue_game(self):
        self.model.run(2)


    def update(self):
        station=[station.capacity for station in self.model.x.stations]
        station.append(self.model.train.capacity)
        station.append(self.model.train.curr_station.name)
        return station

    def next_station(self,station):
        self.model.train.go_to_station(station)
        self.spawn()

    def spawn(self):
        self.model.x.spawn()

    def load(self,num):
        self.model.train.loading(num)

    def unload(self,num):
        self.model.train.unloading(num)
