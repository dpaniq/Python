'''
1. Выводит сообщение об успешном запуске.
    --- [ Сервер начал свою работу ]
2. Принимает данные в многопоточном режиме (receving)
    2.1. Присоединение:
        --- @user: join in
    2.2. Командый запрос:
        --- @user: /some_command
    2.3. Сообщение пользователю:
        --- @user: @user2: message
    2.4. ---
3. Имеет класс user - вся информация о пользователях
    3.1. Количество людей онлайн
        COUNT_USERS: 0
    3.2. Имена пользователей
        {@user:[ip, port]}
    3.3.
4.
'''
# -------------------------------------------------------#
# Библиотеки --------------------------------------------#
# -------------------------------------------------------#
import socket
import time

# -------------------------------------------------------#
# Подключение сервера -----------------------------------#
# -------------------------------------------------------#

# host = socket.gethostbyname(socket.gethostname())
# port = 15200
# print(host)
# server = ('192.168.0.56', 80)  # Локальный адресс сервера
# server = ('89.191.111.198', 5050)  # Внешний Адресс сервера
server = ('', 2533)  # Внешний Адресс сервера
try:

    connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connect.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connect.bind(server)
    print('На старый')
except OSError:
    print('На закрытый')
    connect.close()
    connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connect.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connect.bind(server)

# Базовые сообщения сервера
print("[ Сервер начал свою работу ]")
print("[Ip address]=[port]=[datetime]=[Nickname]=[MSG]")


# -------------------------------------------------------#
# -------------------------------------------------------#
# -------------------------------------------------------#
class user():
    __COUNT_USERS = 0
    __ONLINE_USERS = []
    __DICT_OF_USERS = {}
# -------------------------------------------------------#

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip  # (host, port)
        self.friends = []
        user.__COUNT_USERS += 1
# -------------------------------------------------------#
# FRIEND ------------------------------------------------#
# -------------------------------------------------------#

    @classmethod
    def show_friends(cls, name):
        return cls.__DICT_OF_USERS[name]['object'].friends

    @classmethod
    def add_friends(cls, name, other):
        cls.__DICT_OF_USERS[name]['object'].friends.append(other)

    @classmethod
    def del_friends(cls, name, other):
        cls.__DICT_OF_USERS[name]['object'].friends.remove(other)
# -------------------------------------------------------#
# SEND MESSAGE ------------------------------------------#
# -------------------------------------------------------#

    @classmethod
    def send_message(cls, msg, other):
        ip = cls.__DICT_OF_USERS[other]['ip']

        # # Сообщение другу ---------------------------#
        #     elif msg.startswith('t'):
        #         user.send_message(msg, other)

        # connect.sendto(msg, client)
        connect.sendto(msg, ip)
# -------------------------------------------------------#
# ONLINE / OFFLINE --------------------------------------#
# -------------------------------------------------------#

    @classmethod
    def online(cls, name):
        print('\n' + name, 'появился в сети!')
        cls.__ONLINE_USERS.append(name)

    @classmethod
    def offline(cls, name):
        print('\n' + name, 'вышел из сети!')
        cls.__ONLINE_USERS.remove(name)
# -------------------------------------------------------#
# -------------------------------------------------------#
# -------------------------------------------------------#
# -------------------------------------------------------#
# -------------------------------------------------------#

    @classmethod
    def dict_of_users(cls, name, ip, obj):
        cls.__DICT_OF_USERS[name] = {'ip': ip,
                                     'object': obj}
        print(cls.__DICT_OF_USERS)
# -------------------------------------------------------#

    @classmethod
    def show_all_online(cls):
        return cls.__ONLINE_USERS
# -------------------------------------------------------#
# -------------------------------------------------------#
# Создание экземпляров класса / пользователей -----------#
# -------------------------------------------------------#


def create_instance(cls, user_name, ip):
    obj = globals()[user_name] = cls(user_name, ip)  # Создание
    # Сделать вызов функции сеттер у класса -- -- - -
    user.dict_of_users(user_name, ip, obj)  # Складирование


# -------------------------------------------------------#
# Переменные на сервере ---------------------------------#
# -------------------------------------------------------#
quit = False
# -------------------------------------------------------#
# Прием сообщений ---------------------------------------#
# -------------------------------------------------------#
clients = []
while not quit:
    try:
        # Собираем все приходящие письма
        data, addr = connect.recvfrom(1024)
        read_msg = data.decode('utf-8').split('=')

        if len(read_msg) == 1:  # Появился впервые ------#
            print('MODE #1')
            name = read_msg[0]
        elif len(read_msg) == 2:  # Запрос
            print('MODE #2')
            msg = read_msg[0]
            name = read_msg[1]
        elif len(read_msg) == 3:  # Команды
            print('MODE #3')
            msg = read_msg[0]
            name = read_msg[1]
            other = read_msg[2]
        else:  # Cообщение
            msg = read_msg[0]
            name = read_msg[1]
            other = read_msg[2]
            text = read_msg[3]
# -------------------------------------------------------#
# Обработка сообщений -----------------------------------#
# -------------------------------------------------------#
        if name not in user.show_all_online():
            print('Создаем нового пользователя: ', name)
            create_instance(user, name, addr)
            user.online(name)
            # -------------------------------------------#
        elif msg.startswith('q'):
            user.offline(name)
            # -------------------------------------------#
        else:
            if msg.startswith('/'):
                print('\nЭто командное сообщение')
                # ---------------------------------------#
                # ---------------------------------------#
                if msg == '/list':
                    print('\nМои друзья:')
                    print(user.show_friends(name))
                # ---------------------------------------#
                # ---------------------------------------#
                elif msg == '/add':
                    print('\nДобовить друга:')
                    user.add_friends(name, other)
                # ---------------------------------------#
                # ---------------------------------------#
                elif msg == '/del':
                    print('\nДобовить друга:')
                    user.del_friends(name, other)
                # ---------------------------------------#
                # ---------------------------------------#
                elif msg == '/block':
                    print('\nДобовить друга:')
                    user.block_friends(name, other)
            # -------------------------------------------#
            # Сообщение другу ---------------------------#
            elif msg.startswith('t'):
                user.send_message(text.encode(), other)

            # -------------------------------------------#
        if addr not in clients:
            clients.append(addr)
# -------------------------------------------------------#
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("\n[" + addr[0] + "]=[" + str(addr[1]) +
              "]=[" + itsatime + "]", end="=[text]=")
        print(data.decode("utf-8"))
# -------------------------------------------------------#
# Рассылка всем -----------------------------------------#
# -------------------------------------------------------#
        # for client in clients:
        #     if addr != client:
        #         connect.sendto(data, client)
# -------------------------------------------------------#
    except SyntaxError:
        print("\n[ Сервер прекращает свою работу ]")
        quit = True


# -------------------------------------------------------#
# Завершение подключения---------------------------------#
# -------------------------------------------------------#
del msg
del name
del other
# -------------------------------------------------------#
# Завершение подключения---------------------------------#
# -------------------------------------------------------#
connect.close()
# -------------------------------------------------------#
