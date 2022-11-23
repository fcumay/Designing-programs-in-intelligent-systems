from Player import Player
from Visitor import Visitor
from attraction import Attraction


class Save(object):
    def __init__(self):
        park_name = str()
        player = Player()
        visitors_in_park = dir(Visitor())
        visitors_outside_park = dir(Visitor())
        attractions = dir(Attraction())
        places_for_attractions = int()
        balance_of_park = int()
        time = (int(), int())
