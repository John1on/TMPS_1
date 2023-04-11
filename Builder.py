from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

CocktailBase = namedtuple('CocktailBase', ['Wineglass'])


class Wineglass(Enum):
    COLLINS = auto()
    HURRICANE = auto()

class Alcohol(Enum):
    WHITE_RUM = auto()
    DARK_RUM = auto()
    FINLANDIA = auto()
    DE_KUYPER = auto()

class Topping(Enum):
    SUGAR_SIROP = auto()
    SPRITE = auto()
    PINEAPPLE_JUICE = auto()
    COCONUT_MILK = auto()

class Fruit(Enum):
    LIME = auto()
    MINT = auto()
    PINEAPPLE = auto()
    ORANGE = auto()

class Cocktail:
    def __init__(self , name):
        self.name = name
        self.winegalss = None
        self.alcohol = []
        self.topping = []
        self.fruit = []
        self.price = None

    def __str__(self):
        info:   str = f'Cocktail name: {self.name} \n' \
                f'Wineglass type: {self.winegalss.Wineglass.name} \n' \
                f'Alcohol type: {[it.name for it in self.alcohol]} \n' \
                f'Topping: {[it.name for it in self.topping]} \n' \
                f'Fruit: {[it.name for it in self.fruit]} \n'\
                f'Price: {self.price} lei'
        return info

class Builder(ABC):
    @abstractmethod
    def prepare_wineglass(self) -> None: pass

    @abstractmethod
    def add_alcohol(self) -> None: pass

    @abstractmethod
    def add_topping(self) -> None: pass

    @abstractmethod
    def add_fruit(self) -> None: pass

    @abstractmethod
    def get_coctail(self) -> None: pass

class MohitoCoctailBuilder(Builder):

    def __init__(self):
        self.cocktail = Cocktail("Mohito")
        self.cocktail.price = 100

    def prepare_wineglass(self) -> None:
        self.cocktail.winegalss = CocktailBase(Wineglass.COLLINS)

    def add_alcohol(self) -> None:
        self.cocktail.alcohol.extend([
            it for it in (
                Alcohol.WHITE_RUM,
                Alcohol.FINLANDIA,
            )
        ])

    def add_topping(self) -> None:
        self.cocktail.topping.extend([
            it for it in (
                Topping.SUGAR_SIROP,
                Topping.SPRITE,
            )
        ])

    def add_fruit(self) -> None:
        self.cocktail.fruit.extend([
            it for it in (
                Fruit.LIME,
                Fruit.MINT,
            )
        ])
    
    def get_coctail(self) -> Cocktail:
        return self.cocktail

class PinoColadaCocktailBuilder(Builder):

    def __init__(self):
        self.cocktail = Cocktail("Pino Colada")
        self.cocktail.price = 125

    def prepare_wineglass(self) -> None:
        self.cocktail.winegalss = CocktailBase(Wineglass.HURRICANE)

    def add_alcohol(self) -> None:
        self.cocktail.alcohol.extend([
            it for it in (
                Alcohol.DARK_RUM,
                Alcohol.WHITE_RUM,
            )
        ])

    def add_topping(self) -> None:
        self.cocktail.topping.extend([
            it for it in (
                Topping.PINEAPPLE_JUICE,
                Topping.COCONUT_MILK,
            )
        ])

    def add_fruit(self) -> None:
        self.cocktail.fruit.extend([
            it for it in (
                Fruit.PINEAPPLE,
                Fruit.ORANGE,
            )
        ])
    
    def get_coctail(self) -> Cocktail:
        return self.cocktail

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_cocktail(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_wineglass()
        self.builder.add_alcohol()
        self.builder.add_topping()
        self.builder.add_fruit()

if __name__ == "__main__":
    director = Director()
    for it in (MohitoCoctailBuilder, PinoColadaCocktailBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_cocktail()
        cocktail = builder.get_coctail()
        print(cocktail)
        print('-----------------------------------')
