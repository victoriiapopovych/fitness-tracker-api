from pydantic import BaseModel

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

class Config:
    orm_mode = True