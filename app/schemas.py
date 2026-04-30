from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    age: int | None = None
    email: str
    password: str

class User(BaseModel):
    user_id: int
    name: str
    age: int | None = None
    email: str


class ExerciseCreate(BaseModel):
    exercise_name: str
    muscle_group: str | None = None
    complexity: str = "medium"


class Exercise(BaseModel):
    exercise_id: int
    exercise_name: str
    muscle_group: str | None = None
    complexity: str


class WorkoutCreate(BaseModel):
    user_id: int
    date: date
    duration: int | None = None


class Workout(BaseModel):
    workout_id: int
    user_id: int
    date: date
    duration: int | None = None
    burned_calories: int | None = None

class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: int
    reps: int
    weight: float | None = None

class Config:
    orm_mode = True