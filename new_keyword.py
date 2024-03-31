class Singleton:
    mainobj = None
    def __new__(cls):
        if cls.mainobj is None:
            cls.mainobj = super().__new__(cls)
        return cls.mainobj
    def dis(self):
        print(self)

a = Singleton()
a.dis()
b = Singleton()
b.dis()