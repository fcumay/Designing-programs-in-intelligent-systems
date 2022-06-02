class Controller:
    def __init__(self, model):
        self.model = model

    def new_game(self):
        self.model.run(1)

    def continue_game(self):
        self.model.run(2)

    def update(self):
        return self.model.update()

    def spawn(self):
        self.model.x.spawn()
        self.save()

    def next_station(self, station):
        if self.model.next_station(station):
            self.spawn()
            return ''
        else:
            return 'Input valid name of station.'

    def load(self, num):
        if self.model.check_load(num):
            self.model.train.loading(int(num))
            return ''
        else:
            return 'Input valid number of goods.'

    def unload(self, num):
        if self.model.check_unload(num):
            self.model.train.unloading(int(num))
            return ''
        else:
            return 'Input valid number of goods.'

    def check_overload(self):
        return True if self.model.check_overload() else False

    def save(self):
        self.model.save()
