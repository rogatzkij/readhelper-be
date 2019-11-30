
# back.readhelper.com



## Работа с пользователем
~~~
    back.readhelper.com/user/
~~~
### Регистрация 
#### Запрос
~~~
POST back.readhelper.com/user/regisration

BODY:
{
    "email":"sample@mail.com",
    "name":"sample@mail.com",
    "login":"sample@mail.com",
    "password":"sample@mail.com",
}
~~~
#### Ответ
~~~
STATUS: 200 OK

BODY:
{
    "email":"sample@mail.com",
    "name":"sample@mail.com",
    "login":"sample@mail.com",

    "session":"eedd5521-8e7f-4d29-9c05-98ec63e750a3",
}
~~~
### Авторизация
#### Запрос
~~~
POST back.readhelper.com/user/authorization

BODY:
{
    "login":"sample@mail.com",
    "password":"sample@mail.com",
}
~~~
#### Ответ
~~~
STATUS: 200 OK

BODY:
{   
    "email":"sample@mail.com",
    "name":"sample@mail.com",
    "login":"sample@mail.com",
    
    "session":"eedd5521-8e7f-4d29-9c05-98ec63e750a3",
}
~~~
### Получить список книг
#### Запрос
~~~
GET back.readhelper.com/user/books

HEADER:
session:"eedd5521-8e7f-4d29-9c05-98ec63e750a3"
~~~
#### Ответ
~~~
STATUS 200 OK

BODY:
{
    books: [
        {
            "id":"84ade7a1-4791-4782-9d07-e0b62b0436b",
            "filename":"alice.txt",
            "current":1,
            "count":250,
        },
        {
            "id":"9658f233-14ae-4086-8d22-7d1323bf1702",
            "filename":"mumin.txt",
            "current":1,
            "count":250,
        },
    ]
}
~~~
### Выход
#### Запрос
~~~
GET back.readhelper.com/user/logout

HEADER:
session:"eedd5521-8e7f-4d29-9c05-98ec63e750a3"
~~~
#### Ответ
~~~
STATUS 200 OK
~~~
#### ~~Редактирования~~
#### ~~Получить данные о пользователе~~


## Работа с книгой

### Загрузить книгу
#### Запрос
#### Ответ

### Удалить книгу
#### Запрос
#### Ответ

### Получить страницу
#### Запрос
GET back.readhelper.com/books/get_page
~~~
{
    "id":"eedd5521-8e7f-4d29-9c05-98ec63e750a3",
    "possition":0,
    "limit":50,
}
~~~
#### Ответ
~~~
STATUS 200 OK

BODY:
{
        "words": [
        {
            "id":"0123",                        // id  в словаре
            "position":15,                      // позиция в книге
            "word":"lego",                      // исходное слово
            "level":"90",
            "status":"LEARNING",                // NEW, LEARNING, KNOWN
            "translate":["кубики","штучка"],    // перевод
            "postfix":"!?",                     // знаки препиания
        },
        {
            "id":"0123",                        // id  в словаре
            "position":15,                      // позиция в книге
            "word":"lego",                      // исходное слово
            "level":"90",
            "status":"LEARNING",                // NEW, LEARNING, KNOWN
            "translate":["кубики","штучка"],    // перевод
            "postfix":"!?",                     // знаки препиания
        },
    ]
}
~~~

### Получить информацию о книге
#### Запрос
~~~
{
    "session":"eedd5521-8e7f-4d29-9c05-98ec63e750a3"
    "id":"eedd5521-8e7f-4d29-9c05-98ec63e750a3",
}
~~~
#### Ответ
~~~
STATUS: 200 OK
BODY:
    {
        "id":"84ade7a1-4791-4782-9d07-e0b62b0436b",
        "name":"Алиса в стране чудес",
        "current":1,
        "count":250,
    }
~~~

### Поставить закладку
#### Запрос
#### Ответ

## Работа со словарем






