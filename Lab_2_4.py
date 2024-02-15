
class Fish: # Определяет среднестатистическую рыбу
    animal = "Fish"

    def __init__(self, name:str, last_name:str):
        self.name = name
        self._last_name = last_name # Данная информация является секретной
                                    # И не должна быть известна рядовому пользователю

    def isbig(self): # Данный метод позволяет узнать насколько велика рыба
        print("Yes")

    def ismute(self):# Данный метод позволяет узнать умеет ли рыба говорить (будет унаследован)
        print("Yes")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}"


class Trout(Fish): # Другая разновидность рыб
    pass
    def isbig(self): # Данный метод был перегружен из-за того что форель меньше обычной рыбы
        print("No")

fish = Fish("Gary","Williamson")
trout = Trout("Wary","Gilliamson")
print("Имя? -> ",end="")
print(fish)
print("Животное? -> ",end="")
print(fish.animal)
print("Велика ли рыба? -> ",end="")
fish.isbig()
print("Нема ли рыба? -> ",end="")
fish.ismute()
print("")
print("Имя? -> ",end="")
print(trout)
print("Животное? -> ",end="")
print(trout.animal)
print("Велика ли рыба? -> ",end="")
trout.isbig()
print("Нема ли рыба? -> ",end="")
trout.ismute()
