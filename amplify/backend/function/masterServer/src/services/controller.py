from services.src.user import UserService, UserLoginService, UpsertPreferencesService
from services.src.ai import MealPlanService

{
    "days": 1,
    "meals": {
        "lunch": [
            {
                "meal_type": "lunch",
                "recipe_preview": {
                    "title": "Quinoa & Roasted Vegetable Mason Jar Salad (Make-Ahead)",
                    "servings": 2,
                    "tags": ["vegetarian", "gluten_free", "dairy_free", "meal_prep", "weight_loss"],
                    "description": "A vibrant, nutrient-dense salad layered in a jar with fiber-rich quinoa, roasted vegetables, chickpeas, and a zesty lemon-tahini vinaigrette. High in protein and healthy fats, low in added sugars—perfect for weight loss.",
                    "meal_type": "lunch",
                    "cook_time_minutes": 25,
                    "nutrition": {
                        "fat": 12,
                        "protein": 11,
                        "calories": 380,
                        "carbohydrates": 52
                    },
                    "difficulty": "easy"
                }
            }
        ],
        "dinner": [
            {
                "meal_type": "dinner",
                "recipe_preview": {
                    "title": "Lentil & Mushroom Stuffed Bell Peppers",
                    "servings": 2,
                    "tags": ["vegetarian", "gluten_free", "dairy_free", "high_fiber", "weight_loss"],
                    "description": "Bell halves stuffed with a savory blend of brown lentils, cremini mushrooms, garlic, and herbs, baked to perfection. Served with a side of steamed broccoli for added volume and nutrition.",
                    "meal_type": "dinner",
                    "cook_time_minutes": 30,
                    "nutrition": {
                        "fat": 8,
                        "protein": 18,
                        "calories": 420,
                        "carbohydrates": 68
                    },
                    "difficulty": "medium"
                }
            }
        ]
    }
}
