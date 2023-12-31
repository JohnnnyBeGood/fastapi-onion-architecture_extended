## О проекте
Это дополнение к проекту [Артёма Шумейко](https://www.youtube.com/@artemshumeiko)

[Видео о луковой архитектуре](https://www.youtube.com/watch?v=8Im74b55vFc)  
[Видео о паттерне Unit of work](https://www.youtube.com/watch?v=TaYg23VkCRI)

У Артёма представлены четыре варианта ответа сервера: 
- конкретный пользователь по его ***id***, либо все пользователи сразу
- конкретное задание по его ***id***, либо все задания сразу

я сделал дополнение -  возможность получить от сервера список следующего вида:

| название        | автор      | ответственный  |
| -----------     | ---------- | ----------     |
| купить овощи    | Роман      |  Иван          |
| помыть овощи    | Роман      |  Антон         |
| нарезать овощи  | Екатерина  |  Дмитрий       |
| достать кастрюлю| Фома       |  Антон         |
| вскипятить воду | Альберт    |  Феликс        |
| положить овощи  | Роман      |  Клава         |




### Запуск приложения
1. Создать виртуальное окружение и установить зависимости
2. Вызвать в терминале `python3 src/main.py`

либо если вы используете VS Code, вот *launch.json*

``` json
"version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "jinja": true,
            "justMyCode": true
        }
    ]
```

самое главное запускать/нажимать  **F5** когда открыт файл ***main.py*** и в редакторе
этот файл активен


~~### Настройка Alembic для асинхронного драйвера~~

по данной инструкции создать БД у меня не получилось, поэтому я в коде сделал,
что при запуске выполняется команда:


```python
Base.metadata.create_all
```


### Документация к API
![Alt text](docs/github/openapi.png)
