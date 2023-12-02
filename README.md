# DRF_ToDo_List
Веб-сервис представляет собой систему управления задачами (To-Do List)

## Установка

1. Склонируйте репозиторий на ваше устройство.
2. Установите зависимости, выполнив команду: pip install -r requirements.txt.
3. Создайте файл .env в корневой папке проекта и скопируйте данные из файла .env.sample.
4. В файле .env заполните значения переменных среды для подключения к базе данных (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).
5. Создайте и примените миграции базы данных, выполнив команды:
   - python manage.py makemigrations
   - python manage.py migrate
6. Запустите сервер разработки, выполнив команду: python manage.py runserver.
7. Откройте веб-браузер и введите http://localhost:8000/ для доступа к приложению.

## Эндпоинты

### GET /api/tasks/

Возвращает список всех задач.

#### Параметры запроса

Нет параметров.

#### Пример ответа

[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description of Task 1",
        "created_at": "2022-01-01T00:00:00Z",
        "file": "task_file.pdf",
        "categories": [
            {
                "id": 1,
                "name": "Category 1",
                "description": "Description of Category 1"
            },
            {
                "id": 2,
                "name": "Category 2",
                "description": "Description of Category 2"
            }
        ]
    },
    // Другие задачи
]

### POST /api/tasks/

Создает новую задачу.

#### Параметры запроса

| Параметр      | Тип    | Обязательный | Описание                 |
|---------------|--------| ------------ | ------------------------ |
| title         | string | Да           | Заголовок задачи         |
| description   | string | Да | Описание задачи |
| created_at    | string | Да | Дата создания задачи |
| file          | file   | Нет | Файл, прикрепленный к задаче |
| categories    | array  | Нет | Список категорий, связанных с задачей |

#### Пример запроса

{
    "title": "New Task",
    "description": "Description of New Task",
    "created_at": "2022-01-01T00:00:00Z",
    "file": "new_task_file.pdf",
    "categories": [
        {
            "id": 1,
            "name": "Category 1",
            "description": "Description of Category 1"
        },
        {
            "id": 3,
            "name": "Category 3",
            "description": "Description of Category 3"
        }
    ]
}

#### Пример ответа

{
    "id": 2,
    "title": "New Task",
    "description": "Description of New Task",
    "created_at": "2022-01-01T00:00:00Z",
    "file": "new_task_file.pdf",
    "categories": [
        {
            "id": 1,
            "name": "Category 1",
            "description": "Description of Category 1"
        },
        {
            "id": 3,
            "name": "Category 3",
            "description": "Description of Category 3"
        }
    ]
}

### GET /api/tasks/{task_id}/

Возвращает информацию о задаче по заданному task_id.

#### Параметры запроса

Нет параметров.

#### Пример ответа

{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "created_at": "2022-01-01T00:00:00Z",
    "file": "task_file.pdf",
    "categories": [
        {
            "id": 1,
            "name": "Category 1",
            "description": "Description of Category 1"
        },
        {
            "id": 2,
            "name": "Category 2",
            "description": "Description of Category 2"
        }
    ]
}

### PUT /api/tasks/{task_id}/

Обновляет информацию о задаче по заданному task_id.

#### Параметры запроса

| Параметр      | Тип    | Обязательный | Описание                 |
|---------------|--------| ------------ | ------------------------ |
| title         | string | Нет          | Заголовок задачи         |
| description   | string | Нет | Описание задачи |
| created_at    | string | Нет | Дата создания задачи |
| file          | file   | Нет | Файл, прикрепленный к задаче |
| categories    | array  | Нет | Список категорий, связанных с задачей |

#### Пример запроса

{
    "title": "Updated Task",
    "description": "Updated description of Task 1"
}

#### Пример ответа

{
    "id": 1,
    "title": "Updated Task",
    "description": "Updated description of Task 1",
    "created_at": "2022-01-01T00:00:00Z",
    "file": "task_file.pdf",
    "categories": [
        {
            "id": 1,
            "name": "Category 1",
            "description": "Description of Category 1"
        },
        {
            "id": 2,
            "name": "Category 2",
            "description": "Description of Category 2"
        }
    ]
}

### DELETE /api/tasks/{task_id}/

Удаляет задачу по заданному task_id.

#### Параметры запроса

Нет параметров.

#### Пример ответа

Статус ответа: 204 No Content