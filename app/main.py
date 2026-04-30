from fastapi import FastAPI
from app.database import engine
from app import models, schemas

from app.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness Tracker API",
    description="API for tracking users, exercises and workouts",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Fitness Tracker API is running"}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        name=user.name,
        age=user.age,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()

    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted"}

    return {"error": "User not found"}


@app.post("/exercises", response_model=schemas.Exercise)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    db_exercise = models.Exercise(
        exercise_name=exercise.exercise_name,
        muscle_group=exercise.muscle_group,
        complexity=exercise.complexity
    )

    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)

    return db_exercise

@app.get("/exercises", response_model=list[schemas.Exercise])
def get_exercises(complexity: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Exercise)

    if complexity:
        query = query.filter(models.Exercise.complexity == complexity)

    return query.all()

@app.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    return db.query(models.Exercise).filter(
        models.Exercise.exercise_id == exercise_id
    ).first()

@app.put("/exercises/{exercise_id}", response_model=schemas.Exercise)
def update_exercise(exercise_id: int, updated: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    exercise = db.query(models.Exercise).filter(
        models.Exercise.exercise_id == exercise_id
    ).first()

    if not exercise:
        return {"error": "Exercise not found"}

    exercise.exercise_name = updated.exercise_name
    exercise.muscle_group = updated.muscle_group
    exercise.complexity = updated.complexity

    db.commit()
    db.refresh(exercise)

    return exercise

@app.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.query(models.Exercise).filter(
        models.Exercise.exercise_id == exercise_id
    ).first()

    if not exercise:
        return {"error": "Exercise not found"}

    db.delete(exercise)
    db.commit()

    return {"message": "Exercise deleted"}


@app.post("/workouts", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = models.Workout(
        user_id=workout.user_id,
        date=workout.date,
        duration=workout.duration
    )

    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    return db_workout

@app.get("/workouts", response_model=list[schemas.Workout])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(models.Workout).all()

@app.post("/workouts/{workout_id}/exercise")
def add_exercise_to_workout(
    workout_id: int,
    data: schemas.WorkoutExerciseCreate,
    db: Session = Depends(get_db)
):
    we = models.WorkoutExercise(
        workout_id=workout_id,
        exercise_id=data.exercise_id,
        sets=data.sets,
        reps=data.reps,
        weight=data.weight
    )

    db.add(we)
    db.commit()

    return {"message": "Exercise added to workout"}

@app.get("/workouts/{workout_id}")
def get_workout_with_exercises(workout_id: int, db: Session = Depends(get_db)):
    workout = db.query(models.Workout).filter(
        models.Workout.workout_id == workout_id
    ).first()

    if not workout:
        return {"error": "Workout not found"}

    result = {
        "workout_id": workout.workout_id,
        "date": workout.date,
        "exercises": []
    }

    for we in workout.workout_exercises:
        result["exercises"].append({
            "exercise_id": we.exercise.exercise_id,
            "name": we.exercise.exercise_name,
            "sets": we.sets,
            "reps": we.reps,
            "weight": float(we.weight) if we.weight else None
        })

    return result

