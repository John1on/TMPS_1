import copy

class Prototype:
    _cocktail = None
    _volume = None

    def clone(self):
        pass

    def get_coctail(self):
        return self._cocktail

    def get_volume(self):
        return self._volume

class Mohito(Prototype):
    def __init__(self, float):
        self._cocktail = "Mohito"
        self._volume = 300

    def clone(self):
        return copy.copy(self)

class Pino_Colada(Prototype):
    def __init__(self, float):
        self._cocktail = "Pina_Colada"
        self._volume = 200

    def clone(self):
        return copy.copy(self)

class Object:
    _cocktail1volume1 = None
    _cocktail1volume2 = None
    _cocktai21volume1 = None
    _cocktai21volume2 = None

    @staticmethod
    def __init__():
        Object._cocktail1volume1 = Mohito(1)
        Object._cocktail1volume2 = Mohito(2)
        Object._cocktail2volume1 = Pino_Colada(1)
        Object._cocktail2volume2 = Pino_Colada(2)

    @staticmethod
    def getcocktail1volume1():
        return Object._cocktail1volume1.clone()

    @staticmethod
    def getcocktail1volume2():
        return Object._cocktail1volume2.clone()

    @staticmethod
    def getcocktail2volume1():
        return Object._cocktail2volume1.clone()

    @staticmethod
    def getcocktail2volume2():
        return Object._cocktail2volume2.clone()

   

def main():
    Object.__init__()

    instance = Object.getcocktail1volume1()
    print(f'{instance.get_coctail()}, {instance.get_volume()}')

    instance = Object.getcocktail1volume2()
    print(f'{instance.get_coctail()}, {instance.get_volume()}')

    instance = Object.getcocktail2volume1()
    print(f'{instance.get_coctail()}, {instance.get_volume()}')

    instance = Object.getcocktail2volume2()
    print(f'{instance.get_coctail()}, {instance.get_volume()}')

if __name__ == "__main__":
    main()
