from View.view import TestApp
from Model.model import Model
from Controller.controller import Controller
if __name__ == '__main__':
    model = Model()
    controller = Controller(model)
    view = TestApp(controller)
    view.run()

