import doctest

class Box:
    def __init__(self, PresenceOfCat: bool, Volume: float):
        if not isinstance (Volume, (int,float)):
            raise TypeError("Объем коробки может быть только типа int и float")
        if Volume <= 0:
            raise TypeError("Объем коробки не может отрицательным")
        self.Volume = Volume

        if not isinstance(PresenceOfCat (bool)):
            raise TypeError("PresenceOfCat может быть только типа bool")
        self.PresenceOfCat = PresenceOfCat

    def is_box_empty(self)->bool:
            """
Данная функция выполняет проверку на наличие кота в коробке
    :param self:
    :return: Есть ли в коробке кот
           """
            ...
    def get_box_bigger(self,Volume_added:float)->float:
            """
            Увеличение коробки
            : param Volume_added: Объем, добавляемый к коробке
            : return: Конечный объем коробки
            """
            ...

class PC:
    def __int__(self, gpu : str, PowerOfPsu: int):
        if not isinstance(PowerOfPsu, (int, float)):
            raise TypeError("Мощность блока питания может быть только типа int и float")
        if PowerOfPsu <= 0:
            raise TypeError("Мощность блока питания не может отрицательным")
        self.PowerOfPsu = PowerOfPsu

        if not isinstance(gpu(str)):
            raise TypeError("Модель видеокарты может быть только типа str")
        self.gpu = gpu
    def get_new_gpu (self)->str:
            """
            Замена видеокарты
          :return: Новая модель видеокарты
            """
            ...
    def lower_psu_power(self,lower_power: int)-> int:
            """
            Уменьшение мощности блока питания
            :param self:
            :param lower_power:
            :return: итоговое значение мощности
            """

            ...
class BookShelf:
    def __int__(self, PopularBook : str, AmountOfBooks: int):
        if not isinstance(AmountOfBooks, (int)):
            raise TypeError("Количество книг на полке может быть только типа int")
        if AmountOfBooksu <= 0:
            raise TypeError("Количество книг на полке не может отрицательным")
        self.AmountOfBooks = AmountOfBooks

        if not isinstance(PopularBook(str)):
            raise TypeError("Самая популярная книга может быть только типа str")
        self.PopularBook = PopularBook

    def add_some_books(self,books_added :int)->int:

            """
            В данной функции добавляем книги на полку
            :param books_added: Кол-во добавляемых книг
            :return: Конечное кол-во книг на полке
            """
            ...
    def select_new_fav_book(self,new_fav_book: str)->str:
        """

        :param new_fav_book: Новая любимая книга
        :return: Новое названике книги
        :raise TypeError("Книга может иметь только тип str")

        """
        ...
if __name__ == "__main__":
    doctest.testmod()
