#DRF_ToDo_List
The web service is a task management system (To-Do List)

## Installation

1. Clone the repository to your device.
2. Install the dependencies by running: pip install -r requirements.txt.
3. Create a .env file in the root folder of the project and copy the data from the .env.sample file.
4. Fill in the environment variable values in the .env file for connecting to the database (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).
5. Create and apply database migrations by running the following commands:
   - python manage.py makemigrations
   - python manage.py migrate
6. Start the development server by running: python manage.py runserver.
7. Open a web browser and enter http://localhost:8000/ to access the application.

## Endpoints

### GET /api/tasks/

Returns a list of all tasks.

#### Request Parameters

No parameters.

#### Example Response

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
    // Other tasks
]

### POST /api/tasks/

Creates a new task.

#### Request Parameters

| Parameter   | Type   | Required    | Description              |
| ----------- | ------ | ----------- | ------------------------ |
| title       | string | Yes         | Title of the task         |
| description | string | Yes         | Description of the task   |
| created_at  | string | Yes         | Creation date of the task |
| file        | file   | No          | File attached to the task |
| categories  | array  | No          | List of categories associated with the task |

#### Example Request

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

#### Example Response

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

Returns information about a task based on the given task_id.

#### Request Parameters

No parameters.

#### Example Response

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

Updates information about a task based on the given task_id.

#### Request Parameters

| Parameter   | Type   | Required    | Description              |
| ----------- | ------ | ----------- | ------------------------ |
| title       | string | No          | Title of the task         |
| description | string | No          | Description of the task   |
| created_at  | string | No          | Creation date of the task |
| file        | file   | No          | File attached to the task |
| categories  | array  | No          | List of categories associated with the task |

#### Example Request

{
    "title": "Updated Task",
    "description": "Updated description of Task 1"
}

#### Example Response

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

Deletes a task based on the given task_id.

#### Request Parameters

No parameters.

#### Example Response

Response status: 204 No Content

