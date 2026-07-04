import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt):

    response = model.generate_content(prompt)

    return response.text


def recommend_meal(
    food_type,
    meal_type,
    budget,
    cooking_time,
    mood,
    health_goal,
    ingredients
):

    prompt = f"""
You are MoodMeal AI.

You are an expert chef, nutritionist and food recommendation assistant.

Recommend ONLY ONE best meal.

User Details:

Food Type: {food_type}

Meal Type: {meal_type}

Budget: ₹{budget}

Cooking Time: {cooking_time}

Mood: {mood}

Health Goal: {health_goal}

Available Ingredients: {ingredients}

Return your answer in EXACTLY this format:

🍽 Meal Name

💡 Why this meal?

🥗 Required Ingredients

👨‍🍳 Recipe

🔥 Calories

💪 Protein

💰 Approx Cost

⏱ Cooking Time

✨ One Healthy Tip
IMPORTANT:
Write each section on a separate line.

Calories, Protein, Approx Cost and Cooking Time must each appear on their own separate line.

Do NOT combine them into one paragraph or one sentence.
"""

    response = model.generate_content(prompt)

    return response.text

def recommend_restaurant(
    food_type,
    meal_type,
    budget,
    cuisine,
    distance,
    mood
):

    prompt = f"""
You are MoodMeal AI.

You are an expert food recommendation assistant.

Recommend ONLY ONE restaurant and ONE best dish.

User Details:

Food Type: {food_type}
Meal Type: {meal_type}
Budget: ₹{budget}
Cuisine: {cuisine}
Distance: {distance}
Mood: {mood}

Return exactly in this format:

🏪 Restaurant

🍽 Best Dish

💡 Why this restaurant?

💰 Approx Price

⭐ Rating

⏱ Delivery Time
"""

    response = model.generate_content(prompt)

    return response.text