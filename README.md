# Flask-MongoDB CRUD API

This project is a simple Flask API with MongoDB integration, providing CRUD operations (CREATE, READ, DELETE, UPDATE).

## Getting Started

### Prerequisites

Ensure you have the following installed on your device:
- Python 3.x
- Flask
- Flask-PyMongo
- MongoDB

## Run the Application

```bash 
python app.py
```

Endpoints
1. GET or POST Todo
   URL :/'get_or_post'
Methods:
GET: Retrieve all todos.
POST: Create a new todo.

2. Update or Delete Todo
   URL: /update_or_delete/<string:id>
Methods:
PUT: Update a todo by ID.
DELETE: Delete a todo by ID.
