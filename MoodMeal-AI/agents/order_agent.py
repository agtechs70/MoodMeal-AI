import streamlit as st


def initialize_order_state():

    if "order_step" not in st.session_state:
        st.session_state.order_step = 1

    if "food_type_order" not in st.session_state:
        st.session_state.food_type_order = ""

    if "meal_type_order" not in st.session_state:
        st.session_state.meal_type_order = ""

    if "budget_order" not in st.session_state:
        st.session_state.budget_order = 0

    if "cuisine_order" not in st.session_state:
        st.session_state.cuisine_order = ""

    if "distance_order" not in st.session_state:
        st.session_state.distance_order = ""

    if "mood_order" not in st.session_state:
        st.session_state.mood_order = ""

    if "restaurant_result" not in st.session_state:
        st.session_state.restaurant_result = ""