# Задача "За честь и отвагу!"
from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power, count_warriors=100): # name, power будут передаваться при создании объекта класса
        super().__init__()
        self.name = name
        self.power = power
        self.count_warriors = count_warriors
        self.day_counter = 0
        self.start()

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.count_warriors > 0:
            warriors_kill = min(self.count_warriors, self.power)
            self.count_warriors -= warriors_kill
            self.day_counter += 1
            print(f'{self.name} сражается {self.day_counter} дней(дня)..., осталолось {self.count_warriors} воинов.')
            time.sleep(1)
            if self.count_warriors == 0:
                print(f'{self.name} одержал победу спустя {self.day_counter} дней(дня)!')
                return None

if __name__ == '__main__':
    knight_1 = Knight('Sir Lancelot', 10)   # создание потока
    knight_2 = Knight("Sir Galahad", 20)
    knight_1.join()
    knight_2.join()
    print("Все битвы закончились!")

