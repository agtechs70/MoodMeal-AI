import streamlit as st
from agents.cook_agent import initialize_cook_state
from tools.gemini import recommend_meal
from tools.email_sender import send_email
from tools.pdf_generator import generate_recipe_pdf
from tools.open_apps import open_blinkit

def show_cook_page():

    initialize_cook_state()

    st.title("🍳 Cook at Home")
    st.success("Great Choice!")
    st.write("Let's decide your perfect meal.")

    st.divider()

    # ================= STEP 1 =================

    if st.session_state.cook_step == 1:

        food_type = st.radio(
            "🥦 Select your preference:",
            ["Veg 🥗", "Non-Veg 🍗"],
            key="food_type_radio"
        )

        if st.button("Next ➜", key="step1"):

            st.session_state.food_type = food_type
            st.session_state.cook_step = 2
            st.rerun()

    # ================= STEP 2 =================

    elif st.session_state.cook_step == 2:

        meal_type = st.radio(
            "🍽 What are you planning?",
            [
                "Breakfast 🌞",
                "Lunch 🍛",
                "Dinner 🌙",
                "Snack 🍟"
            ],
            key="meal_type_radio"
        )

        if st.button("Next ➜", key="step2"):

            st.session_state.meal_type = meal_type
            st.session_state.cook_step = 3
            st.rerun()

    # ================= STEP 3 =================

    elif st.session_state.cook_step == 3:

        budget = st.number_input(
            "💰 Enter your Budget (₹)",
            min_value=50,
            max_value=5000,
            step=50,
            key="budget_input"
        )

        if st.button("Next ➜", key="step3"):

            st.session_state.budget = budget
            st.session_state.cook_step = 4
            st.rerun()

    # ================= STEP 4 =================

    elif st.session_state.cook_step == 4:

        cooking_time = st.radio(
            "⏱ How much time do you have?",
            [
                "10 Minutes",
                "20 Minutes",
                "30 Minutes",
                "45+ Minutes"
            ],
            key="time_radio"
        )

        if st.button("Next ➜", key="step4"):

            st.session_state.cooking_time = cooking_time
            st.session_state.cook_step = 5
            st.rerun()
        # ================= STEP 5 =================

    elif st.session_state.cook_step == 5:

        mood = st.radio(
            "😊 What's your mood today?",
            [
                "Happy 😄",
                "Comfort Food 🤗",
                "Healthy 🌿",
                "Spicy 🌶️",
                "Light Meal 🥗"
            ],
            key="mood_radio"
        )

        if st.button("Next ➜", key="step5"):

            st.session_state.mood = mood
            st.session_state.cook_step = 6
            st.rerun()

    # ================= STEP 6 =================

    elif st.session_state.cook_step == 6:

        health_goal = st.radio(
            "🎯 What's your Health Goal?",
            [
                "Weight Loss 🥗",
                "Weight Gain 💪",
                "Muscle Building 🏋️",
                "Stay Healthy 🌿",
                "No Specific Goal 😊"
            ],
            key="goal_radio"
        )

        if st.button("Next ➜", key="step6"):

            st.session_state.health_goal = health_goal
            st.session_state.cook_step = 7
            st.rerun()

    # ================= STEP 7 =================

    elif st.session_state.cook_step == 7:

        ingredients = st.text_area(
            "🥕 Enter available ingredients (comma separated)",
            placeholder="Example: Onion, Tomato, Rice, Paneer",
            key="ingredients_box"
        )

        if st.button("Next ➜", key="step7"):

            st.session_state.ingredients = ingredients
            st.session_state.cook_step = 8
            st.rerun()

    # ================= STEP 8 =================

    elif st.session_state.cook_step == 8:

        st.success("✅ Please review your details")

        st.subheader("📋 Summary")

        st.write("🥦 Food Type:", st.session_state.food_type)
        st.write("🍽 Meal Type:", st.session_state.meal_type)
        st.write(f"💰 Budget: ₹{st.session_state.budget}")
        st.write("⏱ Cooking Time:", st.session_state.cooking_time)
        st.write("😊 Mood:", st.session_state.mood)
        st.write("🎯 Health Goal:", st.session_state.health_goal)
        st.write("🥕 Ingredients:", st.session_state.ingredients)

        st.divider()
            
        if st.button("🤖 Generate AI Recommendation", key="generate_ai"):

            with st.spinner("🧠 MoodMeal AI is thinking..."):

                result = recommend_meal(
                    st.session_state.food_type,
                    st.session_state.meal_type,
                    st.session_state.budget,
                    st.session_state.cooking_time,
                    st.session_state.mood,
                    st.session_state.health_goal,
                    st.session_state.ingredients
                )

            st.session_state.recipe_result = result

        if st.session_state.recipe_result != "":

            st.success("🎉 Recommendation Ready!")

            st.markdown(st.session_state.recipe_result)

            st.divider()

            if st.button("🛒 Buy Ingredients on Blinkit", key="blinkit_btn"):

                open_blinkit(st.session_state.ingredients)

            st.divider()

            pdf_file = generate_recipe_pdf(
                st.session_state.recipe_result
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📄 Download Recipe PDF",
                    data=file,
                    file_name="MoodMeal_Recipe.pdf",
                    mime="application/pdf",
                    key="download_pdf_button"
                )

            st.divider()

            email = st.text_input(
                "📧 Enter your Email",
                placeholder="example@gmail.com",
                key="cook_email"
            )

            if st.button("📧 Send Recipe", key="send_recipe"):

                if email.strip() == "":

                    st.warning("Please enter your email.")

                else:

                    send_email(
                        email,
                        "🍳 Your MoodMeal AI Recipe",
                        st.session_state.recipe_result
                    )

                    st.success("✅ Recipe sent successfully!")

            st.divider()

            if st.button("⬅ Back", key="back_button"):

                st.session_state.page = "home"
                st.session_state.cook_step = 1
                st.session_state.food_type = ""
                st.session_state.meal_type = ""
                st.session_state.budget = 0
                st.session_state.cooking_time = ""
                st.session_state.mood = ""
                st.session_state.health_goal = ""
                st.session_state.ingredients = ""
                st.session_state.recipe_result = ""

                st.rerun()