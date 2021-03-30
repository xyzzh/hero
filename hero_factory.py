from police import Police
from timo import Timo


class HeroFactory:
    def create_hero(self,name):
        if name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂中！")

hero_factory = HeroFactory()
timo_ho = hero_factory.create_hero("Timo")
police_ho = hero_factory.create_hero("Police")
ez = hero_factory.create_hero("EZ")

