import random


class Card:
    balance = 0
    number = '400000'
    pin = ''

    def __init__(self):
        self.generate_number()
        self.generate_pin()

    def generate_number(self):
        for i in range(10):
            self.number += str(random.randint(0, 9))
            i += 1
        print('Номер вашей карты:', self.number)

    def generate_pin(self):
        for i in range(4):
            self.pin += str(random.randint(0, 9))
            i += 1
        print('Ваш PIN:', self.pin, '\n')


card_database = []


def menu():
    while True:
        print('Главное меню\n'
              'Выберите номер операции:')
        menu_opt = int(input('1. Открыть счет в банке\n'
                             '2. Смотреть счет \n'
                             '0. Выход \n'))
        if menu_opt == 1:
            create()
        elif menu_opt == 2:
            login()
        elif menu_opt == 0:
            print('До свидания!')
            exit()
        else:
            print('Введен неверный номер операции. Введите числа 1, 2 или 0')


def create():
    card = Card()
    card_database.append(card)


i = 0


def login():
    var_card_number = input('Введите номер вашей карты: \n')
    if any(instance.number == var_card_number for instance in card_database):
        for element in card_database:
            if element.number == var_card_number:
                i = card_database.index(element)
        var_card_pin = input('Введите PIN вашей карты: \n')
        if card_database[i].pin == var_card_pin:
            login_menu()
        else:
            print('Введен нерпавильный PIN')
    else:
        print('Введен неправильный номер карты')


def login_menu():
    print('Вход выполнен успешно!\n'
          '\nМеню счета')
    while True:
        log_menu_opt = int(input('1. Проверить баланс \n'
                                 '2. Назад в меню \n'
                                 '0. Выход \n'))
        if log_menu_opt == 1:
            print(card_database[i].balance)
        elif log_menu_opt == 2:
            print('Вы вышли из аккаунта!')
            menu()
        elif log_menu_opt == 0:
            print('Bye!')
            exit()
        else:
            print('Введены числа не из диапазона 0, 1, 2')


menu()
