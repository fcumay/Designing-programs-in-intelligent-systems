from model import Model
from view import View
from enteties.Player import Player

class Controller(object):
    def __init__(self):
        model = Model()
        view = View()
        player = Player()


    def controller(self, model):
        pass

    def update(self):
        pass

    def show(self):
        pass

    def choose_save(self):
        pass

    def upload_save(self):
        pass

    def create_new_game(self):
        pass

    def let_visitor_in_park(self, visitor, visitors_in_park):
        pass

    def delete_visitor_from_park(self, visitor, visitors_in_park):
        pass

    def put_visitor_in_queue(self, visitor, attraction):
        pass

    def buy_new_attraction(self, money):
        pass

    def sell_attraction(self, attraction):
        pass

    def buy_place_for_attraction(self, money):
        pass
