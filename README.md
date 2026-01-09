# # Diplom_Yandex_Samokat

## Вторая часть дипломного проекта курса по тестированию.


## Автоматизация теста к API
> Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получение заказа по треку заказа.
Проверить, что код ответа равен 200.

Программа для тестирования представлена в файле [order_test.py](https://github.com/irinasimonova8888/Diplom_Yandex_Samokat/blob/main/order_test.py)
Вспомогательные функции и переменные описаны в файлах [data.py](https://github.com/irinasimonova8888/Diplom_Yandex_Samokat/blob/main/data.py), [configuration.py](https://github.com/irinasimonova8888/Diplom_Yandex_Samokat/blob/main/configuration.py) и [sender_stand_request.py](https://github.com/irinasimonova8888/Diplom_Yandex_Samokat/blob/main/sender_stand_request.py)


## Структура проекта:

- configuration.py             # Базовые URL и пути API
- data.py                      # Тестовые данные (тела запросов, токены)
- sender_stand_request.py      # Функции для отправки HTTP-запросов
- order_test.py                # Тест создания заказа и получения заказа по номеру трэка

Чтобы запустить тесты в VS Code необходимо:
1. Подготовка окружения
Установить: Python 3.9+, VS Code, Расширение Python в VS Code (от Microsoft)
Установить зависимости: Открыть терминал в VS Code и выполнить команду ( pip install requests pytest)
2. Настройка интерпретатора Python
-Нажми Ctrl+Shift+P
-Введи: Python: Select Interpreter
-Выбери подходящую версию Python (например, Python 3.11)
- Проверь, что в левом нижнем углу VS Code отображается выбранная версия.
3. Настройка тестов
-Открой панель Testing (значок колбы в боковой панели).
-Если тесты не обнаружены — нажми Ctrl+Shift+P → введи:
"Python: Configure Tests"
3.Выбери:
Фреймворк: pytest
Папка с тестами: /корень
4. Запуск тестов
 Через панель Testing 
В панели слева нажми на значок колбы
Дождись, пока тесты появятся
Нажми на кнопку ▶️ Run All Tests или отдельный тест