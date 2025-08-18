# 🔗 Yacut — URL Shortener (Flask)

A **production-ready URL shortener** built with **Flask**.  
Users can create compact links with optional custom IDs, redirect to original URLs, and interact via a simple **web UI** or a **JSON API**.  
The project includes **migrations (Alembic)**, **tests (pytest)**, **OpenAPI spec**, and a **Postman collection**.  

---

## 📌 About the Project  

**Yacut** is a minimal yet reliable **URL shortener service**.  
It allows users to:  
- Shorten long URLs into compact links  
- Optionally define their own short IDs  
- Use both a **browser-based UI** and a **RESTful API**  
- Explore API documentation via **OpenAPI spec** or **Postman collection**  

This project is structured for real-world deployment, with database migrations, validation, and automated tests.  

---

## 🧰 Tech Stack  

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/SQLAlchemy-8A2BE2?style=for-the-badge&logo=alchemy&logoColor=white"/> <img src="https://img.shields.io/badge/Alembic-4B8BBE?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/WTForms-FFB300?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Jinja2-B4172D?style=for-the-badge&logo=jinja&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/> <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/> <img src="https://img.shields.io/badge/OpenAPI-6BA539?style=for-the-badge&logo=openapiinitiative&logoColor=white"/> <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>

---

## ✨ Features  

- 🔗 **Shorten long URLs** with optional custom short IDs  
- ↪️ **Redirect short → original URL**  
- 🖥️ **Web UI** with form validation + **JSON API**  
- 📑 **OpenAPI spec** (Swagger-compatible) and **Postman collection**  
- 🗄️ **Database migrations** with Alembic  
- ⚡ **Error handlers** with clean JSON responses  
- 🧪 **Automated tests** with pytest  

---

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
