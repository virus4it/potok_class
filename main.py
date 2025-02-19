from threading import Thread
from time import sleep


ENEMIES = 100



class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global ENEMIES
        days = 0
        print(f"{self.name}, на нас напали!")

        while ENEMIES > 0:
            days += 1
            sleep(1)

            if ENEMIES > self.power:
                ENEMIES -= self.power
            else:
                ENEMIES = 0
            print(f"{self.name}, сражается {days} день(дня)..., осталось {ENEMIES} воинов.")


        print(f"{self.name} одержал победу спустя {days} дней(дня)!")





first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()


print("Все битвы закончились!")
