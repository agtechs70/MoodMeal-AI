import streamlit as st
from pathlib import Path
from app.cook_page import show_cook_page
from app.order_page import show_order_page
st.set_page_config(
    page_title="MoodMeal AI",
    page_icon="🥗",
    layout="centered"
)
css_path = Path("assets/css/style.css")

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
# ---------------- Session ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"


# ---------------- Home ----------------

if st.session_state.page == "home":

    col1, col2, col3 = st.columns([1, 6, 1])

    with col2:
        from PIL import Image

logo = Image.open("assets/logo.png")
st.image(logo, width=250)

    st.markdown(
            """
            <h1 style='text-align:center; margin-top:-95px; margin-left:90px;'>
            MoodMeal <span style='color:#FF6B6B;'>AI</span>
            </h1>
            """,
            unsafe_allow_html=True
        )
    st.markdown(
            """
            <h3 style='text-align:center;color:#FF7A59;'>
            ✨ From 'Kuch Bhi' to the Perfect Meal ✨
            </h3>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="
        background:rgba(255,255,255,0.55);
        backdrop-filter:blur(20px);
        padding:20px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,.4);
        margin-top:20px;
        margin-bottom:30px;
        ">

        <h3>🤖 Your AI Food Decision Partner</h3>

        <p>
        Answer a few simple questions and MoodMeal AI will recommend the perfect meal or restaurant based on your mood, budget, time and preferences.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("## 🍳 Cook at Home")
        st.caption("AI Recipe Generator")

        if st.button(
            "Start Cooking 🍽",
            use_container_width=True,
            key="cook_home"
        ):
            st.session_state.page = "cook"
            st.rerun()

    with col2:

        st.markdown("## 🛵 Order Food")
        st.caption("AI Restaurant Finder")

        if st.button(
            "Find Restaurant 🍕",
            use_container_width=True,
            key="order_home"
        ):
            st.session_state.page = "order"
            st.rerun()

# ---------------- Cook Page ----------------

elif st.session_state.page == "cook":
    show_cook_page()

# ---------------- Order Page ----------------

elif st.session_state.page == "order":
    show_order_page()
