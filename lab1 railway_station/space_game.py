import time
from map import GameMap
from train import Train
from os import system


def menu(x, train,first_time):


    while x.check_overloading(train):
        system('cls')
        x.spawn()
        print(f'Поезд на {train.curr_station.name} станции              В поезде {train.capacity}')
        x.show_condition()
        print('Что сделать?')
        key = input('(1) Следующая станция\n(2) Загрузить поезд\n(3) Разгрузить поезд\n')
        if key == '1':
            train.show_stations()
            stations_state = int(input('\nКуда поедем?\n'))
            while (stations_state >= train.follow_stations):
                stations_state = int(input('\nХорошо подyмайте\n'))
            train.go_to_station(stations_state)
            print('...едем...')
            time.sleep(2)
            continue
        elif key == '2':
            train.loading()
            print('загружаю...')
            time.sleep(3)
        elif key == '3':
            train.unloading()
            print('разгружаю...')
            time.sleep(3)
        elif key == 'p':
            print('Игра сохранена')
            save(x,train,time.time()-first_time)
            exit()
        x.check_overloading(train)


    print('ПОТРАЧЕНО')


def save(x, train,time):
    with open("rec.txt", 'w+') as f:
        for station in x.stations:
            f.write(str(station.capacity) + '\n')
        f.write(str(train.capacity)+'\n')
        f.write(str(time))
def continue_game(x, train):
    data=[]
    with open("rec.txt", 'r+') as f:
        for line in f:
            data.append(float(line))
    for line in range(len(x.stations)):
        x.stations[line].capacity=data[line]
    train.capacity=data[len(x.stations)]
    return data[len(x.stations)+1]





def run():
    x = GameMap()
    train = Train(x)
    flag = int(input(''' 
H   ┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈
E   ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
L   ▏MY TRAIN▕╱▔▔╲┈
L   ▏         ▔▔╲╱▏
O   ▏1.NEW   ▕ ▕▉▕╱╲
!   ▇2.CONTINUE▔▔╲ ▕
!   ▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱ 
!   ┈┈╲▂╱┈┈┈┈┈╲▂╱
       \n '''))
    if flag == 2:
        my_time=continue_game(x, train)
    else:
        my_time=0
    first_time = time.time()-my_time
    menu(x, train,first_time)
    final_time = time.time() - first_time
    print('Ваш счёт:' ,round(final_time,1))




if __name__ == '__main__':
    run()

    # with open("rec.txt", 'w+') as f:
    #     f.write(str(final_time))
