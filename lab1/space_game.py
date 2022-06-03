import time
from map import GameMap
from train import Train
from os import system
import argparse
import json

parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-p", "--previous", action="store_true", help="Continue previous simulation")
parser.add_argument("-t", "--template", action="store_true", help="Start simulation using template")
parser.add_argument("-n", "--next", type=str, help="Next station")
parser.add_argument("-l", "--loading", type=int, help="Loading train. Input number of goods")
parser.add_argument("-u", "--unloading", type=int, help="Unloading train. Input number of goods")
args = parser.parse_args()


def start(file):
    with open(file, "r") as jf:
        option = json.load(jf)
    for i in range(len(x.stations)):
        x.stations[i].capacity = option['capacity'][i]
    train.capacity = option['train']
    for station in x.stations:
        if station.name == option['station']:
            train.curr_station = station


def save(x, train):
    dict = {
        "capacity": [station.capacity for station in x.stations],
        "train": train.capacity,
        "station": train.curr_station.name}
    json_object = json.dumps(dict, indent=4)

    with open("rec.json", "w") as outfile:
        outfile.write(json_object)


def move(x, train):
    if args.loading:
        print('Loading...')
        if train.loading(args.loading):
            time.sleep(3)
        else:
            print('INVALID INPUT')
    if args.unloading:
        print('Unloading...')
        if train.unloading(args.unloading):
            time.sleep(3)
        else:
            print('INVALID INPUT')
    if args.next:
        print('Go...')
        time.sleep(2)
        train.next_station(args.next)
        x.spawn()


if __name__ == '__main__':
    file = 'rec.json'
    if args.template:
        file = "new.json"
    x = GameMap()
    train = Train(x)
    start(file)
    move(x, train)
    print('a--b,c\nb--a,d,e\nc--a,f\nd--b\ne--b,f\nf--c,e')
    print(f'Поезд на {train.curr_station.name} станции   В поезде {train.capacity}')
    x.show_condition()
    save(x, train)

# python space_game.py -p
