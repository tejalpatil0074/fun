import streamlit as st

# ---------- CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffd1dc, #ffe6f0);
    }

    h1, h2, h3, p, label {
        color: #C11C84;
        font-family: 'Georgia', serif;
    }

    .stTextInput > div > div > input {
        background-color: #fff0f5;
        color: black;
        border-radius: 10px;
        border: 1px solid #ff69b4;
        padding: 10px;
    }

    .stButton > button {
        background-color: #000000;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        font-size: 16px;
    }

    .stButton > button:hover {
        background-color: #ff1a66;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}


# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("Hello My Love!!")


    q1 = st.text_area("What comes to your mind when you hear the word *love*?", height=100)
    q2 = st.text_input("Tell me one thing about your girlfriend that she does for you and you likes it the most")
    q3 = st.text_input("What is your expectations from your partner!")

    def has_enough_words(text, min_words=5):
        return len(text.strip().split()) >= min_words


    if st.button("Next ➡️"):
        if not q1 or not q2 or not q3:
            st.warning("Please answer all questions ✨")

        elif (
            not has_enough_words(q1)
            or not has_enough_words(q2)
            or not has_enough_words(q3)
        ):
            st.toast(
                "No one or two word answers allowed 💔\nWrite with big love and big feelings 💖",
                icon="💌"
            )
        else:
            st.session_state.answers["q1"] = q1
            st.session_state.answers["q2"] = q2
            st.session_state.answers["q3"] = q3

            st.session_state.page = 2
            st.rerun()

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.title("💖 A Little Something")

    st.write(
        "From random smiles to meaningful conversations, every moment feels special. "
        "Love isn’t about perfection, it’s about choosing each other every single day. "
        "And with you, that choice feels effortless."
    )

    st.subheader("Will you be my Valentine? 💘")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💕"):
            st.success("Yayyy! You just made my heart so happy 💖🥰")

    with col2:
        if st.button("No 😢"):
            st.warning("Oh no 😭 Think again… love is knocking on your door 💔")
