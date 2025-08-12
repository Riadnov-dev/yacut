# 🔗 Yacut — URL Shortener (Flask)
A clean, production-ready URL shortener built with Flask.
Create compact links with optional custom IDs, redirect to original URLs, and use a simple web UI or a JSON API. Includes migrations (Alembic), tests (pytest), OpenAPI spec, and a Postman collection.

## 🧰 Tech Stack
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000?logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-8A2BE2?logo=python)](https://docs.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-DB%20Migrations-4B8BBE?logo=python)](https://alembic.sqlalchemy.org/)
[![WTForms](https://img.shields.io/badge/WTForms-Form%20Handling-FFB300?logo=python)](https://wtforms.readthedocs.io/)
[![Jinja2](https://img.shields.io/badge/Jinja2-Template%20Engine-orange?logo=jinja)](https://jinja.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing%20Framework-0A9EDC?logo=pytest)](https://docs.pytest.org/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-6BA539?logo=openapiinitiative&logoColor=white)](https://www.openapis.org/)
[![Postman](https://img.shields.io/badge/Postman-API%20Testing-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/)


### ✨ Features
Shorten long URLs with optional custom short IDs

Redirect short → original URL

Web UI (form + validation) and JSON API

OpenAPI spec (swagger-compatible) and Postman collection

Database migrations with Alembic

Error handlers with clean JSON responses

Automated tests (pytest)

### 🚀 Quick Start
Clone the repository:

```
git clone https://github.com/Riadnov-dev/yacut.git
cd yacut
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Set environment variables (example):

```
export FLASK_APP=yacut

export FLASK_ENV=development

export DATABASE_URI=sqlite:///yacut.db
```

Run migrations:

```
flask db upgrade
```

Start the app:

```
flask run
```

Open the web UI:

```
http://127.0.0.1:5000/
```

### 🔐 API (JSON)

Create a short URL (optional custom_id):

```
POST /api/id/
Content-Type: application/json

{
  "url": "https://www.example.com",
  "custom_id": "example"
}
```

Resolve a short URL to the original:

```
GET /api/id/<short_id>/
```
API schema (OpenAPI):

*openapi.yml* in the repository (import into Swagger UI / Postman if needed)

Postman collection:
*postman_collection/Yacut.postman_collection.json*

Setup script:
*postman_collection/set_up_data.sh*

### 🧪 Tests

Run the test suite:

```
pytest
```
Key tests: *tests/test_config.py*, *tests/test_database.py*, *tests/test_endpoints.py*, *tests/test_errorhandlers.py*, *tests/test_views.py*

### ⚙️ Configuration
Main settings live in *settings.py* / environment variables (e.g., *DATABASE_URI*).
Forms, validation, and custom constants live in *forms.py* / *constants.py*.

### 📂 Project Structure
```

yacut/
├── migrations/
│   ├── versions/                 # Alembic migration scripts
│   ├── alembic.ini
│   ├── env.py
│   └── script.py.mako
├── postman_collection/
│   ├── README.md
│   ├── Yacut.postman_collection.json
│   └── set_up_data.sh
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   ├── test_database.py
│   ├── test_endpoints.py
│   ├── test_errorhandlers.py
│   └── test_views.py
├── yacut/                        # Application package
│   ├── static/                   # css, img, js
│   ├── templates/                # base.html, index.html, 404.html, etc.
│   ├── __init__.py               # app factory
│   ├── api_views.py              # JSON API endpoints
│   ├── constants.py
│   ├── error_handlers.py
│   ├── forms.py                  # WTForms
│   ├── models.py                 # SQLAlchemy models
│   └── views.py                  # web views
├── openapi.yml
├── requirements.txt
├── settings.py
├── pytest.ini
├── .flake8
├── .gitignore
└── README.md
```

### 👤 Author

Nikita Riadnov 

GitHub: https://github.com/Riadnov-dev
