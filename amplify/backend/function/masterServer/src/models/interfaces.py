from enum import Enum
from bson import ObjectId
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    _id: Optional[ObjectId] = None
    createdDate: datetime = field(default_factory=datetime.now)


@dataclass
class LoginInput:
    phone: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


@dataclass
class GeneratePlanInput:
    user_id: str


@dataclass
class MealPreferences:
    days: Optional[int] = None
    goal: Optional[str] = None
    servings: Optional[int] = None
    cook_time: Optional[str] = None
    skill_level: Optional[str] = None
    meal_types: Optional[list[str]] = None
    restrictions: Optional[list[str]] = None


@dataclass
class Ingredient:
    name: str
    ran_out: bool = field(default_factory=False)


@dataclass
class UpsertPreferencesInput:
    user_id: str
    preferences: Optional[MealPreferences] = None
    ingredients: Optional[list[Ingredient]] = None
    ingredients_to_exclude: Optional[list[str]] = None


class MealType(str, Enum):
    snack = 'snack'
    lunch = 'lunch'
    dinner = 'dinner'
    breakfast = 'breakfast'


class DifficultyLevel(str, Enum):
    easy = 'easy'
    hard = 'hard'
    medium = 'medium'


class NutritionInfo(BaseModel):
    fat: float
    protein: float
    calories: float
    carbohydrates: float


class PreRecipe(BaseModel):
    title: str
    servings: int
    tags: list[str]
    description: str
    meal_type: MealType
    cook_time_minutes: int
    nutrition: NutritionInfo
    difficulty: DifficultyLevel


class Recipe(BaseModel):
    preview: PreRecipe
    ingredients: list[str]
    instructions: list[str]


class MealProposal(BaseModel):
    meal_type: MealType
    recipe_preview: PreRecipe


class MealPlan(BaseModel):
    days: int
    meals: dict[str, list[MealProposal]]


@dataclass
class Output:
    msg: str = field(default_factory=lambda: '')
    data: dict = field(default_factory=lambda: {})
    status: str = field(default_factory=lambda: 'SUCCESS')
