task_ai_fund = {
  "id": 0,
  "question": "",
  "data": ["","", None],
  "teg": [""],
  "helper": None
}, {
  "id": 1,
  "question": "Определить, является ли строка палиндромом (читается одинаково слева направо и справа налево)",
  "data": ["radar","radar", None],
  "teg": ["easy","str"],
  "helper": None
}, {
  "id": 2,
  "question": "Отсортировать список чисел в порядке возрастания без использования встроенной функции sorted()",
  "data": ["nums = [3, 1, 4, 1, 5]","[1, 1, 3, 4, 5]", None],
  "teg": ["list", "sort"],
  "helper": None
}, {
  "id": 3,
  "question": "Найти частоту каждого символа в строке и вернуть результат в виде словаря",
  "data": ["hello","{'h': 1, 'e': 1, 'l': 2, 'o': 1}", None],
  "teg": ["dict","char"],
  "helper": None
}, {
  "id": 4,
  "question": "Найти все простые числа до заданного числа n. (Решето Эратосфена)",
  "data": ["n = 10","[2, 3, 5, 7]", None],
  "teg": ["list"],
  "helper": None
}, {
  "id": 5,
  "question": "Сгенерировать первые n чисел Фибоначчи",
  "data": ["n = 10","[0, 1, 1, 2, 3]", None],
  "teg": ["list"],
  "helper": None
}, {
  "id": 6,
  "question": "Написать функцию для вычисления факториала числа с использованием рекурсии. Обработать случай отрицательных чисел",
  "data": ["n = 5","120", None],
  "teg": ["recursion"],
  "helper": None
}, {
  "id": 7,
  "question": "Написать функцию, которая принимает имя файла и возвращает кортеж (количество строк, количество слов)",
  "data": ["Файл text.txt с содержимым: Hello world Python is great","(2,5)", None],
  "teg": ["file", "open", "txt"],
  "helper": None
}, {
  "id": 8,
  "question": "Реализовать класс BankAccount с методами: deposit(amount) (внести средства), withdraw(amount) (снять средства), get_balance() (вернуть текущий баланс).",
  "data": ["account = BankAccount(100)","120", None],
  "teg": ["easy","class"],
  "helper": None
}, {
  "id": 9,
  "question": "Найти общие элементы двух списков, используя множества",
  "data": ["list1 = [1, 2, 3, 4] list2 = [3, 4, 5, 6]","{2,4}", None],
  "teg": ["easy","set"],
  "helper": None
}, {
  "id": 10,
  "question": "Создать декоратор, который измеряет время выполнения функции в секундах.",
  "data": ["n = 1000","Функция выполнилась за 0.0001 секунд(ы)", None],
  "teg": ["medium","function","time"],
  "helper": None
}, {
  "id": 11,
  "question": "Создать класс Stack, реализующий основные операции стека: push, pop, peek и is_empty. # Создаем класс Stack для реализации структуры данных стек",
  "data": ["stack.push(30)-stack.pop()","print(stack.peek())", None],
  "teg": ["medium","class", "stack"],
  "helper": None
}, {
  "id": 12,
  "question": "Написать функцию бинарного поиска элемента в отсортированном списке.",
  "data": ["Список nums = [1, 3, 5, 7, 9], элемент target = 5","Индекс 2", None],
  "teg": ["list"],
  "helper": None
}, {
  "id": 13,
  "question": "Реализовать обход бинарного дерева в порядке in-order (левый узел → корень → правый узел)",
  "data": ["in-order (левый узел → корень → правый узел).","[4, 2, 5, 1, 3]", None],
  "teg": ["medium", "class","recursion", "in-order"],
  "helper": None
}, {
  "id": 14,
  "question": "Сохранить словарь в JSON-файл и загрузить его обратно.",
  "data": ["Словарь data = name: Alice, age: 30, city: Moscow", " После загрузки из файла должен вернуться исходный словарь.", None],
  "teg": ["open","file","json","dict"],
  "helper": None
}, {
  "id": 15,
  "question": "Написать функцию, которая обрабатывает деление на ноль и неверный тип данных.",
  "data": ["Успешный случай: a = 10, b = 2.Ошибка деления: a = 5, b = 0.Ошибка типа: a = 10, b = 2.","5.0-Деление на ноль невозможно-Некорректный тип данных", None],
  "teg": ["easy","except"],
  "helper": None
}, {
  "id": 16,
  "question": "Создать класс Node и класс LinkedList для реализации односвязного списка с методами добавления, удаления и поиска элементов.",
  "data": ["ll.append(10)(20)(30)","Вывод: 10 -> 30", None],
  "teg": ["medium","class","node","linkedlist"],
  "helper": ["""# class node
  # Значение, которое хранит узел
  # Ссылка на следующий узел (по умолчанию None)
# class LinkedList
    # def __init__ 
        # Начало списка. Если список пуст — `head` = None
    # def append(
        # Создаётся новый узел с переданным значением
        # if  Если список пуст (head == None)
            # Новый узел становится первым элементом  
            # Завершение метода
        # Иначе начинаем с первого элемента
        # while Пока есть следующий узел...
            # ...переходим к нему
        # Вставляем новый узел в конец списка
        
    # def delete(  
        # if  Если список пуст, ничего не делаем
            # Завершение метода
        # if Если удаляемый элемент — первый
            # Сдвигаем `head` на следующий элемент
            # Завершение метода
        # Иначе начинаем обход списка
        # while  Пока есть следующий узел...
            # if  Если нашли нужный элемент...
                # Пропускаем его (удаляем из цепочки)
            # Переход к следующему узлу
    # def display(self):  
            # Список для хранения значений
            # Начинаем с головы списка
            # while # Пока текущий узел не None
                # Добавляем значение в список (строкой)
                # Переходим к следующему узлу
            # Выводим все значения через " -> """]
}, {
  "id": 17,
  "question": "Написать функцию для проверки корректности email-адреса с помощью регулярного выражения.",
  "data": ["email = user@example.com (валидный) email = invalid_email (невалидный)","Ожидаемый результат: True и False", None],
  "teg": ["easy","re", "pattern"],
  "helper": None
}, {
  "id": 18,
  "question": "Используя map, filter и reduce, преобразовать список чисел:",
  "data": ["", None],
  "teg": ["easy","lambda","map","filter","reduce","functools"],
  "helper": None
}, {
  "id": 19,
  "question": "Написать функцию, которая принимает две даты и возвращает разницу между ними в днях.",
  "data": ["date1 = 2023-01-01/2023-02-01","Ожидаемый результат: 31 день.", None],
  "teg": ["datetime"],
  "helper": None
}, {
  "id": 20,
  "question": "Создать декоратор для кэширования результатов функции и ускорения повторных вычислений.",
  "data": ["Входные данные: Функция вычисления чисел Фибоначчи:","55", None],
  "teg": ["medium","function",""],
  "helper": None
}, {
  "id": 21,
  "question": "Реализовать алгоритм сортировки слиянием для списка чисел.",
  "data": ["nums = [5, 2, 9, 1, 5, 6]","Ожидаемый результат: [1, 2, 5, 5, 6, 9].", None],
  "teg": ["medium","list", "sort", "merge sort"],
  "helper": ["array.extend()", "append"]
}, {
  "id": 22,
  "question": "Создать генератор, который возвращает квадраты чисел от 1 до n.",
  "data": ["Входные данные: n = 5.","Ожидаемый результат: Последовательность 1, 4, 9, 16, 25.", None],
  "teg": ["easy", "generator", "yield"],
  "helper": ["yield"]
}, {
  "id": 23,
  "question": "Написать функцию для чтения CSV-файла и подсчета средней величины столбца с числами. Входные данные: Файл data.csv с содержимым:",
  "data": ["Чтение и запись CSV-файла","Файл data.csv с содержимым", None],
  "teg": ["easy"],
  "helper": ["CSV", "csv.DictReader"]
}, {
  "id": 24,
  "question": "Реализация паттерна Singleton Задача: Создать класс DatabaseConnection, гарантирующий только один экземпляр класса.",
  "data": ["Ожидаемый результат: db1 is db2 должно быть","True", None],
  "teg": ["easy", "class"],
  "helper": ["__new__", "Singleton"]
}, {
  "id": 25,
  "question": "Написать функцию, которая получает данные с публичного API и возвращает результат.",
  "data": ["Входные данные: URL https://jsonplaceholder.typicode.com/todos/1.","Вывод данных задачи (например, {'userId': 1, 'id': 1, ...}).", None],
  "teg": ["easy", "requests"],
  "helper": None
}, {
  "id": 0,
  "question": "",
  "data": ["","", None],
  "teg": [""],
  "helper": None
}, {
  "id": 0,
  "question": "",
  "data": ["","", None],
  "teg": [""],
  "helper": None
}, {
  "id": 0,
  "question": "",
  "data": ["","", None],
  "teg": [""],
  "helper": None
}

