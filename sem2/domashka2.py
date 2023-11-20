from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class Sword(IGameItem):
    def open(self):
        print('Sword!')


class Shield(IGameItem):
    def open(self):
        print('Shield!')


class Potion(IGameItem):
    def open(self):
        print('Potion!')


class Scroll(IGameItem):
    def open(self):
        print('Scroll!')


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


class SwordGenerator(ItemFabric):
    def create_item(self):
        return Sword()


class ShieldGenerator(ItemFabric):
    def create_item(self):
        return Shield()


class PotionGenerator(ItemFabric):
    def create_item(self):
        return Potion()


class ScrollGenerator(ItemFabric):
    def create_item(self):
        return Scroll()


if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator(), SwordGenerator(), ShieldGenerator(), PotionGenerator(), ScrollGenerator()]

    for i in range(20):
        index = randint(0, 9)
        if index < 5:
            rewards[index].create_item().open()
        elif index < 8:
            GoldGenerator().create_item().open()
        else:
            GemGenerator().create_item().open()
