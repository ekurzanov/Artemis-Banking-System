import random
import clipboard

card_database = []


class Card:
    balance = 0
    number = '400000'
    pin = ''

    def __init__(self):
        self.generate_number()
        self.generate_pin()

    def generate_number(self):
        self.number += str(random.randint(1000000000, 9999999999))
        print('Номер вашей карты:', self.number)
        clipboard.copy(self.number)

    def generate_pin(self):
        for i in range(4):
            self.pin += str(random.randint(0, 9))
        print('Ваш PIN:', self.pin, '\n')


def menu():
    while True:
        print('Главное меню\n'
              'Введите номер операции:')
        menu_opt = input('1. Открыть счет в банке\n'
                         '2. Смотреть счет \n'
                         '0. Выход \n')
        if menu_opt == '1':
            create()
        elif menu_opt == '2':
            login()
        elif menu_opt == '0':
            print('До свидания!')
            exit()
        else:
            print('Введен неверный номер операции. Введите числа 1, 2 или 0')


def create():
    card = Card()
    card_database.append(card)


def login():
    if not card_database:
        print('Открытых счетов не найдено. Возврат в главное меню...\n')
        menu()
    global var_card_ind
    var_card_ind = -1
    var_card_number = input('Введите номер вашей карты: \n')
    for obj in card_database:
        var_card_ind += 1
        if obj.number == var_card_number:
            if obj.pin == input('Введите PIN вашей карты: \n'):
                login_menu()
            else:
                print('Введен неправильный PIN')
        else:
            print('Введен неправильный номер карты')


def login_menu():
    print('\nВход выполнен успешно!'
          '\nМеню счета {}'.format(card_database[var_card_ind].number))
    while True:
        log_menu_opt = input('1. Проверить баланс \n'
                             '2. Назад в меню \n'
                             '0. Выход \n')
        if log_menu_opt == '1':
            print('Баланс:', card_database[var_card_ind].balance)
        elif log_menu_opt == '2':
            print('Вы вышли из аккаунта')
            menu()
        elif log_menu_opt == '0':
            print('Bye!')
            exit()
        else:
            print('Введены числа не из диапазона 1, 2 или 0')


menu()
