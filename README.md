Учебная виртуальная машина (УВМ) - Вариант №13
Общее описание
Данный проект представляет собой реализацию ассемблера и интерпретатора для учебной виртуальной машины (УВМ) согласно варианту №13 задания. Проект выполнен в рамках практической работы по дисциплине "Архитектура вычислительных систем" или аналогичной.

Проект реализует полный цикл обработки программ для УВМ:

Ассемблер, преобразующий текстовое описание программы в YAML-формате в промежуточное представление и далее в бинарный машинный код

Интерпретатор, исполняющий бинарный код на виртуальной машине с поддержкой стека, памяти и арифметико-логических операций

Соответствие варианту №13
Спецификация УВМ для варианта №13 включает следующие команды:

load_const (загрузка константы на стек)

Код операции A = 46

Аргумент B = константа (26 бит)

Размер команды: 4 байта

Тестовый пример: A=46, B=630 → 0xAE, 0x9D, 0x00, 0x00

read (чтение значения из памяти на стек)

Код операции A = 44

Аргумент B = адрес (18 бит)

Размер команды: 3 байта

Тестовый пример: A=44, B=496 → 0x2C, 0x7C, 0x00

write (запись значения с вершины стека в память)

Код операции A = 51

Аргумент B = адрес (18 бит)

Размер команды: 3 байта

bswap (побайтовый разворот 32-битного значения на стеке)

Код операции A = 53

Размер команды: 1 байт

Тестовый пример: A=53 → 0x35

Этапы реализации
Практическая работа выполнена в соответствии с требованиями и состоит из 5 этапов, каждый из которых отражен в истории коммитов git-репозитория:

Этап 1: Перевод программы в промежуточное представление

Этап 2: Формирование машинного кода

Этап 3: Интерпретатор и операции с памятью

Этап 4: Реализация арифметико-логического устройства (команда bswap)

Этап 5: Выполнение тестовой задачи (векторные операции)

Описание всех функций и настроек
Архитектура проекта
Проект имеет модульную архитектуру и состоит из следующих компонентов:

text
.
├── assembler.py          # Модуль ассемблера
├── interpreter.py        # Модуль интерпретатора
├── run.py               # Основной скрипт для полного цикла
├── requirements.txt     # Зависимости проекта
├── test_spec.yaml       # Тестовая программа для проверки спецификации
└── tests/               # Директория с тестовыми программами
    ├── test_copy_array.yaml     # Тест копирования массива
    ├── test_bswap_vector.yaml   # Тест вектора bswap
    ├── test_example_1.yaml      # Пример программы 1
    ├── test_example_2.yaml      # Пример программы 2
    └── test_example_3.yaml      # Пример программы 3
Модуль assembler.py
Назначение: Преобразование YAML-описания программы в бинарный машинный код.

Основные функции:

assemble(input_file, output_file, test_mode=False) - основная функция ассемблирования

Поддержка режимов тестирования:

--test-intermediate - вывод промежуточного представления команд

--test-bytecode - вывод сгенерированного байт-кода в hex-формате

Формат входного файла (YAML):

yaml
instructions:
  - load_const: <значение>    # Загрузка константы на стек
  - read: <адрес>             # Чтение из памяти
  - write: <адрес>            # Запись в память
  - bswap                     # Побайтовый разворот (без аргумента)
Кодирование команд:

load_const: 4 байта [46, b1, b2, b3], где b1,b2,b3 - little-endian представление константы

read: 3 байта [44, a1, a2], где a1,a2 - little-endian представление адреса

write: 3 байта [51, a1, a2], где a1,a2 - little-endian представление адреса

bswap: 1 байт [53]

Модуль interpreter.py
Назначение: Исполнение бинарного машинного кода на виртуальной машине.

Основные функции:

interpret(code_file, memory_dump_file) - интерпретация бинарного кода

Реализация стека для хранения промежуточных значений

Модель памяти в виде словаря (адрес → значение)

Сохранение дампа памяти в JSON-формате

Архитектура УВМ:

Стек: LIFO-структура для хранения 32-битных целых чисел

Память: ассоциативный массив адрес → 32-битное значение

Счетчик команд: указатель на текущую исполняемую команду

Формат команд: определен в спецификации варианта №13

Алгоритм работы:

Чтение бинарного файла с командами

Последовательная обработка команд согласно их формату

Выполнение операций над стеком и памятью

Сохранение конечного состояния памяти в JSON-файл

Модуль run.py
Назначение: Объединение ассемблера и интерпретатора в единый цикл обработки.

Функционал:

Прием параметров командной строки

Последовательный вызов assembler.py и interpreter.py

Вывод статусных сообщений о процессе выполнения

Описание команд для сборки проекта и запуска тестов
Предварительные требования
Установка Python: Требуется Python версии 3.8 или выше

Установка Git: Для работы с репозиторием

Установка зависимостей
bash
pip install -r requirements.txt
Файл requirements.txt содержит:

text
PyYAML>=6.0
Сборка и запуск проекта
1. Полный цикл обработки программы
bash
python run.py <input.yaml> <output.bin> <memory.json>
Параметры:

input.yaml - YAML-файл с исходной программой

output.bin - бинарный файл с машинным кодом

memory.json - JSON-файл с дампом памяти после выполнения

Пример:

bash
python run.py tests/test_copy_array.yaml program.bin result.json
2. Отдельное использование ассемблера
bash
python assembler.py <input.yaml> <output.bin> [--test-intermediate] [--test-bytecode]
Режимы тестирования:

--test-intermediate - вывод промежуточного представления (Этап 1)

--test-bytecode - вывод байт-кода в hex-формате (Этап 2)

Примеры:

bash
# Базовое ассемблирование
python assembler.py test_spec.yaml output.bin

# С выводом промежуточного представления
python assembler.py test_spec.yaml output.bin --test-intermediate

# С выводом байт-кода
python assembler.py test_spec.yaml output.bin --test-bytecode
3. Отдельное использование интерпретатора
bash
python interpreter.py <input.bin> <memory.json>
Пример:

bash
python interpreter.py program.bin memory_dump.json
Запуск тестов
Тест 1: Проверка соответствия спецификации
bash
# Создание тестовой программы
cat > test_spec.yaml << 'EOF'
instructions:
  - load_const: 630
  - read: 496
  - write: 421
  - bswap
EOF

# Проверка байт-кода
python assembler.py test_spec.yaml spec.bin --test-bytecode
# Ожидаемый вывод: AE 9D 00 00 2C 7C 00 33 A5 01 35
Тест 2: Копирование массива (Этап 3)
bash
python run.py tests/test_copy_array.yaml copy.bin copy.json
cat copy.json
# Ожидаемый результат: {"10": 100, "11": 200, "12": 300, "20": 100, "21": 200, "22": 300}
Тест 3: Вектор bswap (Этап 5)
bash
python run.py tests/test_bswap_vector.yaml vector.bin vector.json
python -c "import json; data = json.load(open('vector.json')); print(f'Обработано элементов: {len(data)}')"
# Ожидаемый результат: 10 элементов
Тест 4: Примеры программ (Этап 5)
bash
# Пример 1
python run.py tests/test_example_1.yaml ex1.bin ex1.json

# Пример 2
python run.py tests/test_example_2.yaml ex2.bin ex2.json

# Пример 3
python run.py tests/test_example_3.yaml ex3.bin ex3.json
Автоматический тест всех этапов
bash
# Создание тестового скрипта
cat > test_all.ps1 << 'EOF'
echo "=== Тестирование всех этапов ==="

echo "1. Этап 1: Промежуточное представление"
python assembler.py test_spec.yaml temp.bin --test-intermediate

echo ""
echo "2. Этап 2: Байт-код"
python assembler.py test_spec.yaml temp.bin --test-bytecode

echo ""
echo "3. Этап 3: Интерпретатор и память"
python run.py tests/test_copy_array.yaml temp.bin temp.json
python -c "import json; data = json.load(open('temp.json')); print(f'Скопировано значений: {len(data)}')"

echo ""
echo "4. Этап 4: Команда bswap"
python run.py tests/test_example_1.yaml temp.bin temp.json

echo ""
echo "5. Этап 5: Вектор bswap"
python run.py tests/test_bswap_vector.yaml temp.bin temp.json
python -c "import json; data = json.load(open('temp.json')); print(f'Элементов в векторе: {len(data)}')"

Remove-Item temp.* -ErrorAction SilentlyContinue
echo "=== Тестирование завершено ==="
EOF

# Запуск теста (Windows PowerShell)
powershell -ExecutionPolicy Bypass -File test_all.ps1
Примеры использования
Пример 1: Простая программа с bswap
Файл: tests/test_example_1.yaml

yaml
instructions:
  - load_const: 1000
  - write: 100
  - read: 100
  - bswap
  - write: 101
Запуск:

bash
python run.py tests/test_example_1.yaml example.bin example.json
Результат (файл example.json):

json
{
  "100": 1000,
  "101": 3523215360
}
Объяснение: Число 1000 (0x000003E8) после операции bswap преобразуется в 0xE8030000, что в десятичной системе равно 3523215360.

Пример 2: Работа с несколькими ячейками памяти
Файл: tests/test_example_2.yaml

yaml
instructions:
  - load_const: 0x00000001
  - write: 200
  - load_const: 0x00000002
  - write: 201
  - read: 200
  - bswap
  - write: 202
  - read: 201
  - bswap
  - write: 203
Запуск:

bash
python run.py tests/test_example_2.yaml example2.bin example2.json
Пример 3: Разворот конкретного числа
Файл: tests/test_example_3.yaml

yaml
instructions:
  - load_const: 0x00112233
  - write: 300
  - read: 300
  - bswap
  - write: 301
Запуск:

bash
python run.py tests/test_example_3.yaml example3.bin example3.json
Результат: Число 0x00112233 (1122867) после bswap становится 0x33221100 (856887552).

Пример 4: Копирование массива (Этап 3)
Файл: tests/test_copy_array.yaml

yaml
instructions:
  - load_const: 100
  - write: 10
  - load_const: 200
  - write: 11
  - load_const: 300
  - write: 12

  # Копируем из 10, 11, 12 в 20, 21, 22
  - read: 10
  - write: 20
  - read: 11
  - write: 21
  - read: 12
  - write: 22
Запуск:

bash
python run.py tests/test_copy_array.yaml copy.bin copy.json
cat copy.json
Результат:

json
{
  "10": 100,
  "11": 200,
  "12": 300,
  "20": 100,
  "21": 200,
  "22": 300
}
Пример 5: Векторная операция bswap (Этап 5)
Файл: tests/test_bswap_vector.yaml

yaml
instructions:
  # Инициализация вектора из 10 элементов
  - load_const: 0x12345678
  - write: 0
  - load_const: 0xabcdef00
  - write: 1
  - load_const: 0xfeedface
  - write: 2
  - load_const: 0xdeadbeef
  - write: 3
  - load_const: 0xcafebabe
  - write: 4
  - load_const: 0x11223344
  - write: 5
  - load_const: 0x55667788
  - write: 6
  - load_const: 0x99aabbcc
  - write: 7
  - load_const: 0xddeeff00
  - write: 8
  - load_const: 0x00ffeedd
  - write: 9

  # Применение bswap ко всем элементам
  - read: 0
  - bswap
  - write: 0
  - read: 1
  - bswap
  - write: 1
  - read: 2
  - bswap
  - write: 2
  - read: 3
  - bswap
  - write: 3
  - read: 4
  - bswap
  - write: 4
  - read: 5
  - bswap
  - write: 5
  - read: 6
  - bswap
  - write: 6
  - read: 7
  - bswap
  - write: 7
  - read: 8
  - bswap
  - write: 8
  - read: 9
  - bswap
  - write: 9
Запуск:

bash
python run.py tests/test_bswap_vector.yaml vector.bin vector.json
python -c "
import json
with open('vector.json', 'r') as f:
    data = json.load(f)
print('Обработано элементов:', len(data))
for i in range(3):
    print(f'[{i}] = {data[str(i)]}')
"
Пример 6: Проверка соответствия спецификации
Создание тестового файла:

bash
cat > my_test.yaml << 'EOF'
instructions:
  - load_const: 100
  - write: 1
  - read: 1
  - bswap
  - write: 2
EOF
Запуск:

bash
python run.py my_test.yaml my_program.bin my_result.json
cat my_result.json
Работа с Git-репозиторием
Структура коммитов
История разработки отражает поэтапное выполнение работы:

Initial commit - базовая структура проекта

Этап 1: Промежуточное представление - реализация ассемблера с YAML-парсингом

Этап 2: Формирование машинного кода - генерация бинарного кода, режимы тестирования

Этап 3: Интерпретатор и память - модель памяти, команды load/read/write

Этап 4: Реализация АЛУ - команда bswap

Этап 5: Тестовая задача - вектор bswap, примеры программ

Публикация репозитория
Репозиторий должен быть размещен на одном из поддерживаемых git-сервисов:

GitHub (рекомендуется): https://github.com/

GitLab: https://gitlab.com/

Gitea: https://gitea.com/

GitFlic: https://gitflic.ru/

Другие из утвержденного списка

Требования к коммитам
Каждый этап работы должен быть отражен отдельным коммитом

Сообщения коммитов должны подробно описывать внесенные изменения

Код должен быть чистым и соответствовать PEP8 (для Python)

Отладка и решение проблем
Распространенные проблемы
Ошибка "No such file or directory"

bash
# Проверьте существование файла
ls -la <имя_файла>

# Проверьте правильность пути
python assembler.py ./tests/test_copy_array.yaml output.bin
Ошибка кодировки YAML-файла

bash
# Сохраняйте файлы в UTF-8
notepad test.yaml
# При сохранении выберите кодировку UTF-8
Ошибка импорта модулей

bash
# Убедитесь, что все файлы в одной директории
ls assembler.py interpreter.py run.py

# Проверьте рабочую директорию
pwd
Верификация правильности реализации
Для проверки соответствия спецификации выполните:

bash
# 1. Проверка байт-кода load_const 630
python assembler.py test_spec.yaml verify.bin --test-bytecode
# Должно вывести: AE 9D 00 00 ... 35

# 2. Проверка интерпретатора
python run.py tests/test_copy_array.yaml verify.bin verify.json
python -c "
import json
with open('verify.json') as f:
    data = json.load(f)
expected = {'10': 100, '11': 200, '12': 300, '20': 100, '21': 200, '22': 300}
if data == expected:
    print('Интерпретатор работает корректно')
else:
    print('Ошибка в интерпретаторе')
"
Дополнительные материалы
Формат JSON-дампа памяти
Файл результата содержит состояние памяти после выполнения программы:

json
{
  "<адрес1>": <значение1>,
  "<адрес2>": <значение2>,
  ...
}
Адреса представлены в виде строк, значения - 32-битные целые числа.

Оптимизация производительности
Для больших программ можно рассмотреть:

Кэширование результатов операций

Оптимизацию алгоритмов работы со стеком

Использование более эффективных структур данных

Расширение функционала
Проект может быть расширен следующими способами:

Добавление новых команд АЛУ

Поддержка отладчика с пошаговым выполнением

Визуализация состояния стека и памяти

Поддержка подпрограмм и вызовов функций

Приложение: Полная спецификация команд УВМ (вариант 13)
load_const - Загрузка константы на стек
Поле	Биты	Значение
A	0-5	Код операции (46)
B	6-31	Константа (26 бит)
Размер: 4 байта
Действие: stack.push(B)
Тест: A=46, B=630 → 0xAE, 0x9D, 0x00, 0x00

read - Чтение из памяти на стек
Поле	Биты	Значение
A	0-5	Код операции (44)
B	6-23	Адрес (18 бит)
Размер: 3 байта
Действие: stack.push(memory[B])
Тест: A=44, B=496 → 0x2C, 0x7C, 0x00

write - Запись из стека в память
Поле	Биты	Значение
A	0-5	Код операции (51)
B	6-23	Адрес (18 бит)
Размер: 3 байта
Действие: memory[B] = stack.pop()

bswap - Побайтовый разворот
Поле	Биты	Значение
A	0-5	Код операции (53)
Размер: 1 байт
Действие: value = stack.pop(); stack.push(bswap(value))
Тест: A=53 → 0x35
