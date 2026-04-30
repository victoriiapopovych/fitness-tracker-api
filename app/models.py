from sqlalchemy import Integer, String, Column, Date, ForeignKey, Enum, Numeric
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base) :
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name =  Column(String(50), nullable=False)
    age = Column(Integer)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    workouts = relationship("Workout", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercises"

    exercise_id = Column(Integer, primary_key=True, index=True)
    exercise_name = Column(String(50), nullable=False)
    muscle_group = Column(String(50))
    complexity = Column(Enum("low", "medium", "high"), default="medium")

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")


class Workout(Base):
    __tablename__ = "workouts"

    workout_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    date = Column(Date, nullable=False)
    duration = Column(Integer)
    burned_calories = Column(Integer)

    user = relationship("User", back_populates="workouts")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout")


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    we_id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.workout_id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.exercise_id"), nullable=False)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Numeric(5, 2))

    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")