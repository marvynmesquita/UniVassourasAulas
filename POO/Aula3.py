import keyboard

class Car:
    def __init__(self, isRunning):
        self.isRunning = False

    def start(self):
        self.isRunning = True
    def stop(self):
        self.isRunning = False

carro = Car(False)

while True:
    if keyboard.is_pressed('space'):
        carro.start()
        print('O carro esta andando')
    else:
        carro.stop()
