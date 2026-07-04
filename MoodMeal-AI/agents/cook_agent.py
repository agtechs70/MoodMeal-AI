import streamlit as st


def initialize_cook_state():

    if "cook_step" not in st.session_state:
        st.session_state.cook_step = 1

    if "food_type" not in st.session_state:
        st.session_state.food_type = ""

    if "meal_type" not in st.session_state:
        st.session_state.meal_type = ""

    if "budget" not in st.session_state:
        st.session_state.budget = 0

    if "cooking_time" not in st.session_state:
        st.session_state.cooking_time = ""

    if "mood" not in st.session_state:
        st.session_state.mood = ""

    if "health_goal" not in st.session_state:
        st.session_state.health_goal = ""

    if "ingredients" not in st.session_state:
        st.session_state.ingredients = ""
    if "recipe_result" not in st.session_state:
        st.session_state.recipe_result = ""