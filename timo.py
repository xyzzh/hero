
from Hero import Hero
from police import Police


class Timo(Hero):
    hp = 500
    power = 180
    name = "Timo"

    def speak_lines(self):
        print("Timo:提莫队长正在待命！")

timo_ho = Timo()
timo_ho.speak_lines()
timo_ho.fight(Police.hp, Police.power)