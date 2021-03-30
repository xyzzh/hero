class Hero:
    hp = ""
    power = ""
    name = ""

    def fight(self,enemy_hp,enemy_power):
        my_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_hp > enemy_final_hp:
            print(f"{self.name}获胜！")
        elif my_hp < enemy_final_hp:
            print("敌方获胜！")
        else:
            print("平局！")

