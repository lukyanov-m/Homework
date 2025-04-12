# Мой банк

## Описание:

Это учебный проект. Он будет развиваться и пополняться новыми функциями по мере наполнения меня знаниями. 
В конце концов это должно стать полноценным банковским приложением.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/lukyanov-m/Homework.git
```
2. Установите зависимости:

Смотри pyproject.toml

## Использование:
**Т.к. приложение находится в разработке, весь функционал находится в ветке develop**

В модуле main можете подставить свои данные и получить соответствующие результаты. Примеры данных так же можно подсмотреть там.

Функции реализованные в проекте:
1. mask_account_card - *Принимает тип и номер карты или счета, а возвращает тип и замаскированный номер*
2. get_date - *Принимает строку с датой и временем ГГГГ-ММ-ДД+время, возвращает дату в формате ДД.ММ.ГГГГ*
3. filter_by_state - *Функция фильтрует список словарей с процессами по состоянию их выполнения*
4. sort_by_date - *Функция сортирует список словарей с процессами по времени*
