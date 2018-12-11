'''
Название модуля - Профиль
[Выполнено] - работа над элементом завершенна
[Изменения] - должны быть внесены корректировки
[Простойка] - требует работы
'''


class User:
    '''|User|:
            * Взаимодействие с контентом:                  - [Простойка]
                - случайный звонок:
                    & симпатия
                    & следующий собеседник
                    & оставить жалобу
                - история:
                    - Посмотреть истории
                    - Оставить историю
            * Взаимодействие с аккаунтами:                 - [Простойка]
                - написать другу
                - удалить друга
            * Фильтр:                                      - [Простойка]
                - Выбрать критерии:
                    & Выбрать страну(-ы) общения
                    & Выбрать пол
                    & Выбрать возраст
                -
            * Настроки:
                - Чат
                - Друзья
                - Профиль
                -'''

    __IDENTIFICATE = 0  # Счетчик аккаунтов

    def __init__(self, nickname, name=None, status='user'):
        self.__nickname = '#' + nickname
        self.__name = name
        self.__status = status
        self.__id = User.__IDENTIFICATE
        User.__IDENTIFICATE += 1

    @property
    def get_information(self):
        return ('@property\t| Id: {} | Никнейм: {} | Имя: {} | Статус: {}'.format(
            self.__id,
            self.__nickname,
            self.__name,
            self.__status))

    @get_information.setter
    def get_information(self, sett):
        print('Изминения внесены...')
        self.__nickname = sett['nickname']
        self.__name = sett['name']
        self.__status = sett['status']
        return ('\t| Id: {} | Никнейм: {} | Имя: {} | Статус: {}'.format(
            self.__id,
            self.__nickname,
            self.__name,
            self.__status))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Guest(User):
    def __init__(self, nickname):
        super().__init__(nickname)
        self.get_information = {'nickname': 'guest12312',
                                'name': None,
                                'status': 'guest'}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Moderator(User):
    '''|MODERATOR|:
            * Осуществляет контроль за поступающим контентом:
                - разблокировка/блокировка видео
                -
            * Взаимодействие с аккаунтами
                - разблокировка/блокировка аккаунтов
            * Другие... '''

    def __init__(self, nickname, name):
        super().__init__(nickname, name)
        self.status = 'Moderator'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Administrator(User):
    '''|Administrator|:
        * Осуществляет контроль за поступающим контентом:
            - разблокировка/блокировка видео
            -
        * Взаимодействие с аккаунтами
            - разблокировка/блокировка аккаунтов
            - назначение статуса пользователям
        * Другие... '''

    def __init__(self, nickname, name):
        super().__init__(nickname, name)
        self.status = 'Administrator'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
user = User('user', 'user')
mode = Moderator('mode', 'mode')
admin = Administrator('adm', 'adm')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# --ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-ВЫВОД-- #
print(user.get_information)
print(mode.get_information)
print(admin.get_information)

user.__qwe = 221
user.__id = 12312
mode.__id = 4
print(user.__id)
print(user.get_information)

# get_information(id, nickname, name, status):
user.get_information = {'nickname': 'bogdan',
                        'name': 'gromov', 'status': 'boss'}
print(user.get_information)

guest = Guest('grooa')
print(guest.get_information)
