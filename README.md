# Банковская Система "Артемида"
Проект эмулирует работу банковской системы, которая может быть реализована в отделениях банка, банкоматах и личном кабинете клиента.

# Описание работы программы
Программа позволяет создавать и просматривать счет пользователя, а также завершать свою работу.

## I. Главное меню
После запуска программы открывается **Главное меню**. Оно включает список операций, которые можно выполнить:
```
1. Открыть счет в банке
2. Смотреть счет
0. Выход
```

**Каждая операция выполняет определенное действие:**<br/>
`1. Открыть счет в банке` - выпускается карта с уникальным номером из 16 цифр, который всегда начинается на '400000...' (Идентификационный номер эмитента), и её PIN;<br/>
`2. Смотреть счет`- появляется запрос на ввод номера карты и её PIN. В случае получения корректных данных открывается [II. Меню счета](#ii-меню-счета);<br/>
`0. Выход` - завершает выполнение программы.<br/>

Необходимо ввести номер операции `1`, `2` или `0` для продолжения работы.

## II. Меню счета
Выводится сообщение об успешной аутентификации и открывается Меню счета:
```
1. Проверить баланс
2. Назад в меню
0. Выход 
```

**Каждая опция выполняет определенное действие аналогично Главному меню:**<br/>
`1. Проверить баланс` - выводится баланс счета (в данной версии);<br/>
`2. Назад в меню` - возвращает пользователя в Главное меню;<br/>
`0. Выход` - функция завершает выполнение программы.<br/>

Необходимо ввести номер операции `1`, `2` или `0` для продолжения работы.
