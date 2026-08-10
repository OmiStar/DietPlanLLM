import os

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


st.set_page_config(
    page_title="AI Diet Planner",
    page_icon="🥗",
    layout="centered"
)


st.title("🥗 AI Diet Planner")

st.write(
    "Choose your goal and generate a simple daily diet plan with Gemini."
)


st.info(
    "This app provides general nutrition information only. "
    "It is not a substitute for advice from a doctor or registered dietitian."
)


api_key = (
    os.getenv("GOOGLE_API_KEY")
    or os.getenv("GEMINI_API_KEY")
)


if not api_key:
    st.error(
        "Gemini API key not found. "
        "Add GOOGLE_API_KEY to your .env file."
    )
    st.stop()


model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)


goal = st.selectbox(
    "What is your goal?",
    [
        "Gain weight",
        "Lose weight"
    ]
)


if st.button(
    "Generate Diet Plan",
    type="primary",
    use_container_width=True
):

    selected_goal = goal.lower()

    prompt = f"""
    You are a nutrition assistant.

    The user's fitness goal is to {selected_goal}.

    Create a simple and practical daily diet plan for this goal.

    Include:

    - Breakfast
    - Morning snack
    - Lunch
    - Evening snack
    - Dinner
    - Approximate calories for each meal
    - Approximate protein for each meal
    - Total daily calories
    - Total daily protein

    Use common, affordable foods.

    Keep the explanation simple and easy to follow.

    Do not recommend extreme dieting,
    unsafe calorie restriction,
    or rapid weight change.

    Do not diagnose medical conditions.

    Mention that people with medical conditions,
    allergies, pregnancy, eating-disorder concerns,
    or specific clinical nutrition needs should seek
    advice from a qualified healthcare professional.
    """

    try:

        with st.spinner("Creating your diet plan..."):

            response = model.invoke(prompt)

        st.subheader("Your Diet Plan")

        st.markdown(response.text)

    except Exception as exc:

        st.error(
            "The diet plan could not be generated. "
            "Please check your API key and try again."
        )

        with st.expander("Technical details"):
            st.code(str(exc))