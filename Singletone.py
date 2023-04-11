class Singleton(type):
    _instances  = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]
    
class MySingleton(metaclass=Singleton):
    def __init__(self):
        self.name = "Valeria"

    def gate_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

if __name__ == "__main__":
    singleton1 = MySingleton()
    singleton2 = MySingleton()
    singleton3 = MySingleton()
    print(id(singleton1), id(singleton2), id(singleton3))
    print("My friend is " + singleton1.gate_name())
    singleton1.set_name("Galina")
    print("My friend is " + singleton2.gate_name())
    singleton3.set_name("Olga")
    print("My friend is " + singleton3.gate_name())
