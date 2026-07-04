import streamlit as st
from agents.order_agent import initialize_order_state
from tools.gemini import recommend_restaurant
from tools.open_apps import open_swiggy, open_zomato


def show_order_page():

    initialize_order_state()

    st.title("🛵 Order Food")
    st.success("Let's find your perfect order!")

    st.divider()

    # ================= STEP 1 =================

    if st.session_state.order_step == 1:

        food_type = st.radio(
            "🥦 Select your preference:",
            ["Veg 🥗", "Non-Veg 🍗"],
            key="order_food_type"
        )

        if st.button("Next ➜", key="order_step1"):

            st.session_state.food_type_order = food_type
            st.session_state.order_step = 2
            st.rerun()

    # ================= STEP 2 =================

    elif st.session_state.order_step == 2:

        meal_type = st.radio(
            "🍽 What do you want to order?",
            [
                "Breakfast 🌞",
                "Lunch 🍛",
                "Dinner 🌙",
                "Snacks 🍟"
            ],
            key="order_meal_type"
        )

        if st.button("Next ➜", key="order_step2"):

            st.session_state.meal_type_order = meal_type
            st.session_state.order_step = 3
            st.rerun()

    # ================= STEP 3 =================

    elif st.session_state.order_step == 3:

        budget = st.number_input(
            "💰 Your Budget (₹)",
            min_value=100,
            max_value=5000,
            step=50,
            key="order_budget"
        )

        if st.button("Next ➜", key="order_step3"):

            st.session_state.budget_order = budget
            st.session_state.order_step = 4
            st.rerun()

    # ================= STEP 4 =================

    elif st.session_state.order_step == 4:

        cuisine = st.selectbox(
            "🍜 Select Cuisine",
            [
                "North Indian",
                "South Indian",
                "Chinese",
                "Italian",
                "Pizza",
                "Burger",
                "Biryani",
                "Street Food"
            ],
            key="order_cuisine"
        )

        if st.button("Next ➜", key="order_step4"):

            st.session_state.cuisine_order = cuisine
            st.session_state.order_step = 5
            st.rerun()
        # ================= STEP 5 =================

    elif st.session_state.order_step == 5:

        distance = st.selectbox(
            "📍 Preferred Distance",
            [
                "Within 2 km",
                "Within 5 km",
                "Within 10 km",
                "Anywhere"
            ],
            key="order_distance"
        )

        if st.button("Next ➜", key="order_step5"):

            st.session_state.distance_order = distance
            st.session_state.order_step = 6
            st.rerun()

    # ================= STEP 6 =================

    elif st.session_state.order_step == 6:

        mood = st.radio(
            "😊 What's your mood?",
            [
                "Comfort Food 🤗",
                "Healthy 🌿",
                "Spicy 🌶️",
                "Party 🎉",
                "Something Different 😋"
            ],
            key="order_mood"
        )

        if st.button("Next ➜", key="order_step6"):

            st.session_state.mood_order = mood
            st.session_state.order_step = 7
            st.rerun()

    # ================= STEP 7 =================

    elif st.session_state.order_step == 7:

        st.success("✅ Review Your Choices")

        st.subheader("📋 Order Summary")

        st.write("🥦 Food Type:", st.session_state.food_type_order)
        st.write("🍽 Meal Type:", st.session_state.meal_type_order)
        st.write(f"💰 Budget: ₹{st.session_state.budget_order}")
        st.write("🍜 Cuisine:", st.session_state.cuisine_order)
        st.write("📍 Distance:", st.session_state.distance_order)
        st.write("😊 Mood:", st.session_state.mood_order)

        st.divider()

        if st.button("🤖 Find Best Restaurant", key="restaurant_ai"):

            with st.spinner("🍽 Finding the best restaurant..."):

                result = recommend_restaurant(
                    st.session_state.food_type_order,
                    st.session_state.meal_type_order,
                    st.session_state.budget_order,
                    st.session_state.cuisine_order,
                    st.session_state.distance_order,
                    st.session_state.mood_order
                )

            st.session_state.restaurant_result = result
        if st.session_state.restaurant_result != "":

            st.success("🎉 Recommendation Ready!")

            st.markdown(st.session_state.restaurant_result)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                if st.button("🛵 Open Swiggy", key="swiggy_btn"):

                    open_swiggy(st.session_state.cuisine_order)

            with col2:

                if st.button("🍽 Open Zomato", key="zomato_btn"):

                    open_zomato(st.session_state.cuisine_order)

    st.divider()

    if st.button("⬅ Back", key="order_back"):

        st.session_state.page = "home"
        st.session_state.order_step = 1

        st.session_state.food_type_order = ""
        st.session_state.meal_type_order = ""
        st.session_state.budget_order = 0
        st.session_state.cuisine_order = ""
        st.session_state.distance_order = ""
        st.session_state.mood_order = ""
        st.session_state.restaurant_result = ""

        st.rerun()                    