'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
$
# [Пример]
# --------- Cпособ представления и хранения данных
#  [Вид]
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Аккаунт:
    {id: {'nickname': '@nickname',
         'fullname': 'full name',
         'status': 'guest/user/moderator/administrator,
         'rating': <number>,
         'messages:[<list_messages_1>, <list_messages_2>],
         '...'}
    -----------------------------------------------
    0: {'nickname': '@panique',
        'fullname': Bogdan Gromov,
        'status': 'administrator',
        'rating': 1,
        'messages': ['@x40']}

    1: {'nickname': '@x40',
        'fullname': 'Hachiko Marterosyan',
        'status': 'guest',
        'rating': 2,
        'messages': ['@panique']}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Видео:
    'video-idx-idx_a-idx_b': {'Name': 'nameofcall',
                            'Date': 'date-of-call',
                            'Lenght': 'n-seconds',
                            'Video': 'file.mp4'}

    -----------------------------------------------
    'video-789-0-1': {'Name': '@panique+@x40+<date+of_call>',
                    'Date': '2018-04-12-16:54:32',
                    'Lenght': 14233+},
                    'Video': '@panique+@x40+<date+of_call>.mp4'
[... Отправка сразу адресату / хранение на сервере?]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Истории:
    {'stories-idx-idx_a-idx_b': {'Name': 'nameofstories',
                                'Date': 'date-of-stories',
                                'Lenght': 'n-seconds',
                                'Chance': True / False}}
    - ----------------------------------------------
    {'stories-789-0-1': {'Name': '@panique+@x40+date+of_stories',
                        'Date': '2018-04-12-16:54:38',
                        'Lenght': 14233,
                        'Chance': True}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Сообщения:
    {'chat-idx_a-idx_b': {'Name': 'idx-b',
                    'First_chat_datatime': <chat-data-time>
                    'Last_chat_datatime': <last-message-time>
                    'Lenght': 'n-seconds',
                    'Messages:
    - ----------------------------------------------
    {'chat-789-0-1': {'Name': '@panique+@x40+date+of_call',
                'Date': '2018-04-12-16:54:38',
                'Massage': '[]'
                'Lenght': 14233,
                'Chance': True}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# Видео-Логи:
    {'idx-idx_a-idx_b': {'Name': 'nameofcall',
                        'Date': 'date-of-call',
                        'Lenght': 'n-seconds',
                        'Chance': True / False}}
    - ----------------------------------------------
    {'789-0-1': {'Name': '@panique+@x40+date+of_call',
                'Date': 2018 - 04 - 12 - 16: 54: 32,
                'Lenght': 14233,
                'Chance': True}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Истории-Логи:
    {'idx-idx_a-idx_b': {'Name': 'nameofcall',
                        'Date': 'date-of-call',
                        'Lenght': 'n-seconds',
                        'Chance': True / False}}
    - ----------------------------------------------
    {'789-0-1': {'Name': '@panique+@x40+date+of_call',
                'Date': 2018 - 04 - 12 - 16: 54: 32,
                'Lenght': 14233,
                'Chance': True}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Сообщения-Логи:
    {'idx-idx_a-idx_b': {'Name': 'nameofcall',
                        'Date': 'date-of-call',
                        'Lenght': 'n-seconds',
                        'Chance': True / False}}
    - ----------------------------------------------
    {'789-0-1': {'Name': '@panique+@x40+date+of_call',
                'Date': 2018 - 04 - 12 - 16: 54: 32,
                'Lenght': 14233,
                'Chance': True}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

'''
