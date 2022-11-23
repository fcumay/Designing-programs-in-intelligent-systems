from enteties.Player import Player
from enteties.Visitor import Visitor
from enteties.attraction import Attraction
from enteties.Save import Save


class Model(object):
    def __init__(self):
        park_name = ""
        player = Player()
        visitors_in_park = dir(Visitor())
        visitors_outside_park = dir(Visitor())
        attractions = dir(Attraction())
        places_for_attractions = 2
        price_of_place_for_attraction = 10
        balance = 220
        time = (int(), int())
        saves = dir(Save())

    def model(self):
        pass

    def choose_save(self, saves):
        pass

    def upload_save(self, save):
        pass

    def create_new_game(self):
        pass

    def let_visitor_in_park(self, visitor, visitors_in_park):
        pass

    def delete_visitor_in_park(self, visitor, visitors_in_park):
        pass

    def put_visitor_in_queue(self, visitor, attraction):
        pass

    def buy_new_attraction(self, money):
        pass

    def sell_attraction(self, attraction):
        pass

    def buy_place_for_attraction(self, money):
        pass

    def check_capacity_of_attractions(self, attractions, place_for_attractions):
        pass
