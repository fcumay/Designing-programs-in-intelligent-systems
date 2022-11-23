from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from windows.main_window import Ui_main_window
from windows.play_selection_window import Ui_play_selection_window
from windows.save_select_window import Ui_save_select_window
from windows.start_new_game_window import Ui_start_new_game_window
from windows.game_window import Ui_game_window
from windows.visitor_window import Ui_information_about_visitor
from windows.attraction_window import Ui_information_about_attraction
from windows.buy_place_for_attraction_window import Ui_information_about_new_place_attraction
from windows.main_window2 import Ui_main_window2


def play_button_action():  # запускает окно выбора загрузить сохранение или начать новую игру
    global play_selection
    play_selection = QtWidgets.QDialog()
    ui = Ui_play_selection_window()
    ui.setupUi(play_selection)
    main_window.close()
    ui.button_choose_saves.clicked.connect(button_choose_saves_action)
    ui.button_start_new_game.clicked.connect(button_start_new_game_action)

    play_selection.show()


def exit_and_save_button_action():  # выходит из игры
    sys.exit(app.exec_())
    pass


def button_choose_saves_action():  # запускает окно выбора сохранений
    global save_select_window
    save_select_window = QtWidgets.QDialog()
    ui = Ui_save_select_window()
    ui.setupUi(save_select_window)
    play_selection.close()

    ui.button_upload_save.clicked.connect(show_game_window)

    save_select_window.show()


def button_start_new_game_action():  # запускает окно начала новый игры
    global start_new_game_window
    start_new_game_window = QtWidgets.QDialog()
    ui = Ui_start_new_game_window()
    ui.setupUi(start_new_game_window)
    play_selection.close()
    ui.button_play.clicked.connect(show_game_window)

    start_new_game_window.show()


def show_game_window():
    global game_window
    game_window = QtWidgets.QDialog()
    ui = Ui_game_window()
    ui.setupUi(game_window)

    try:
        save_select_window.close()
    except:
        start_new_game_window.close()

    ui.button_buy_place_for_attraction.clicked.connect(show_information_buy_place_for_attraction_window)
    ui.button_attraction_1.clicked.connect(show_information_about_attraction_window)
    ui.button_attraction_2.clicked.connect(show_information_about_attraction_window)
    ui.button_attraction_3.clicked.connect(show_information_about_attraction_window)
    ui.button_visitor.clicked.connect(show_visitor_window)
    ui.button_return_to_menu.clicked.connect(show_main_window_with_continue)
    game_window.show()


def show_visitor_window():
    global information_about_visitor
    information_about_visitor = QtWidgets.QDialog()
    ui = Ui_information_about_visitor()
    ui.setupUi(information_about_visitor)
    information_about_visitor.show()


def show_information_about_attraction_window():
    global information_about_attraction
    information_about_attraction = QtWidgets.QDialog()
    ui = Ui_information_about_attraction()
    ui.setupUi(information_about_attraction)
    information_about_attraction.show()


def show_information_buy_place_for_attraction_window():
    global information_about_new_place_attraction
    information_about_new_place_attraction = QtWidgets.QDialog()
    ui = Ui_information_about_new_place_attraction()
    ui.setupUi(information_about_new_place_attraction)
    information_about_new_place_attraction.show()


def show_main_window():
    global main_window
    main_window = QtWidgets.QDialog()

    ui_main_window = Ui_main_window()
    ui_main_window.setupUi(main_window)
    ui_main_window.button_enter.clicked.connect(play_button_action)
    ui_main_window.button_exit_and_save.clicked.connect(exit_and_save_button_action)

    main_window.show()


def show_main_window_with_continue():
    global main_window2
    main_window2 = QtWidgets.QDialog()
    game_window.close()
    ui_main_window2 = Ui_main_window2()
    ui_main_window2.setupUi(main_window2)
    ui_main_window2.button_enter.clicked.connect(show_game_window)
    ui_main_window2.button_exit_and_save.clicked.connect(exit_and_save_button_action)

    main_window2.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    show_main_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


class View:
    pass