# 🏋️‍♀️ Fitness Tracker API

A backend REST API for tracking workouts, exercises, and user progress.

---

## 🚀 Tech Stack

* Python
* FastAPI
* SQLAlchemy (ORM)
* MySQL
* Uvicorn

---

## 📌 Features

* 👤 User management (create, view, delete users)
* 🏋️ Exercise management
* 📅 Workout tracking
* 🔗 Database relationships (one-to-many, many-to-many)
* 📖 Automatic API documentation (Swagger)

---

## ⚙️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/fitness-tracker-api.git
cd fitness-tracker-api
```

2. Create virtual environment:

```bash
python -m venv .venv
```

3. Activate it:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the server:

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Documentation

After запуск, open:

```
http://127.0.0.1:8000/docs
```

Here you can test all endpoints directly (Swagger UI).

---

## 🗄️ Database

The project uses MySQL with the following main tables:

* users
* exercises
* workouts
* workout_exercises

Relationships:

* One-to-Many → User → Workouts
* Many-to-Many → Workouts ↔ Exercises

---

## 💡 Project Purpose

This project was created to practice backend development using FastAPI, database design, and REST API principles.

---

## 📈 Future Improvements

* Authentication (JWT)
* Calories calculation
* User progress tracking
* Docker support

---

## 👩‍💻 Author

Victoria (Computer Engineering Student)
