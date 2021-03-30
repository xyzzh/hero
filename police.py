from Hero import Hero


class Police(Hero):
    hp = 900
    power = 200
    name = "Police"

    def speak_lines(self):
        print("Police:见识一下法律的子弹！")

police_ho = Police()
police_ho.speak_lines()
