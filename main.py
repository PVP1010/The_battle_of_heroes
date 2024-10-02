class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        else:
            print(f"{self.name} не может атаковать, так как он мертв!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_number}:")
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            else:
                print(f"{self.computer.name} мертв.")

            print(f"{self.player.name} здоровье: {self.player.health}")
            print(f"{self.computer.name} здоровье: {self.computer.health}")

            round_number += 1

        if self.player.is_alive():
            print("\nПоздравляем, вы победили!")
        else:
            print("\nК сожалению, вы проиграли. Победил компьютер.")


if __name__ == "__main__":
    game = Game()
    game.start()