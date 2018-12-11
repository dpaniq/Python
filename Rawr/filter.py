
'''
Сообщния отсылаются сразу адрессату?
Где хоранятся сооьбщения если пользователь не в сети?
Когда пользователь заходит, как всплывают сообщения?

'''
import pprint

contries_dict = {
    'A': ['Algeria', 'Andorra', 'Angola',
          'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
          'Austria', 'Azerbaijan'],
    'B': ['Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
          'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
          'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
          'Burundi'],
    'C': ['Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
          'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
          'Comoros', 'Congo, Democratic Republic of the', 'Congo',
          'Republic of the Costa Rica', 'Côte d’Ivoire', 'Croatia',
          'Cuba', 'Cyprus', 'Czech Republic'],
    'D': ['Denmark', 'Djibouti', 'Dominica', 'Dominican Republic'],
    'E': ['East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador',
          'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia'],
    'F': ['Fiji', 'Finland', 'France'],
    'G': ['Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
          'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana'],
    'H': ['Haiti', 'Honduras', 'Hungary'],
    'I': ['Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
          'Israel', 'Italy'],
    'J': ['Jamaica', 'Japan', 'Jordan'],
    'K': ['Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
          'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan'],
    'L': ['Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
          'Liechtenstein', 'Lithuania', 'Luxembourg'],
    'M': ['Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
          'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
          'Mexico', 'Micronesia, Federated States of', 'Moldova',
          'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
          'Myanmar (Burma)'],
    'N': ['Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
          'Nicaragua', 'Niger', 'Nigeria', 'Norway'],
    'O': ['Oman'],
    'P': ['Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
          'Peru', 'Philippines', 'Poland', 'Portugal'],
    'Q': ['Qatar'],
    'R': ['Romania', 'Russia', 'Rwanda'],
    'S': ['Saint Kitts and Nevis', 'Saint Lucia',
          'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
          'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
          'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
          'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
          'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
          'Sudan, South', 'Suriname', 'Swaziland', 'Sweden',
          'Switzerland', 'Syria'],
    'T': ['The Bahamas', 'The Gambia', 'Taiwan', 'Tajikistan',
          'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
          'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu'],
    'U': ['Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
          'United States', 'Uruguay', 'Uzbekistan'],
    'V': ['Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam'],
    'W': [],
    'X': [],
    'Y': ['Yemen'],
    'Z': ['Zambia']}


account = {'nickname': {'fullname': 'name surname',
                        'age': '08/04/1994',
                        'country': 'Latvia',
                        'sex': 'man'},
           'technical': {'ip': ('0.0.0.0', 0),
                         'object': '<main>.__object-in-memmory'},
           'filter': {'seek': ['female'],
                      'age_from': 18,
                      'age_till': 34,
                      'friends': ['name1', 'name2', 'name3'],
                      'countries': ['Latvia', 'Russia', 'Armenia']}}

print('Было: ')
pprint.pprint(account)

# -------------------------------------------------------#


def change_name(change_name, obj):
    obj['nickname']['fullname'] = change_name


def change_age(age, obj):
    obj['nickname']['age'] = age


def change_country(country, obj):
    obj['nickname']['country'] = country


def change_seek(seek, obj):
    obj['nickname']['seek'] = seek


# -------------------------------------------------------#
q = True
while q:
    menu = input('''
        --- Меню ---
        1. Изменить профиль
        2. Фильтр
        3. Выход из программы''')

    if menu == '1':
        submenu = input('''
            --- Изменить профиль ---
                1. Сменить имя
                2. Возраст
                3. Страна
                4. Пол
               ''')
# -------------------------------------------------------#
        if submenu == '1':
            new_name = input('Ввидите новое имя: ')
            change_name(new_name, account)
            continue
# -------------------------------------------------------#
        elif submenu == '2':
            year = input('Сколько вам лет: ')
            month = input('Ввидите месяц рождения:')
            day = input('Ввидите день рождения: ')
            age = '{}/{}/{}'.format(day, month, 2018 - int(year))
            change_age(age, account)
            continue
# -------------------------------------------------------#
        elif submenu == '3':
            country = input('Выберите страну: ')
            change_country(country, account)
            continue
# -------------------------------------------------------#
        elif submenu == '4':
            seek = input('''
                1. Мужчина
                2. Женщина
                3. Любое''')

            change_seek(seek, account)
            continue
# -------------------------------------------------------#
# -------------------------------------------------------#
        else:
            print('Что-то другое')
    elif menu == '2':
        submenu = input('''
                --- Изминения в фильтре ---
                    1. Кого ищу
                    2. От скольки лет
                    3. До скольки лет
                    4. Мои друзья
                    5. Страны''')
    else:
        q = False

print('\nСтало')
pprint.pprint(account)
