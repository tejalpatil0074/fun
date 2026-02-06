import streamlit as st

# ---------- CSS ----------
st.markdown(
    """
    <style>

    .blur {
        filter: blur(6px);
        pointer-events: none;
        user-select: none;
    }

    .modal-overlay {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.4);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal-box {
        background: white;
        padding: 35px;
        border-radius: 18px;
        width: 55%;
        text-align: center;
        font-family: Georgia, serif;
        color: #C11C84;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .modal-box button {
        margin-top: 20px;
        padding: 10px 30px;
        border-radius: 20px;
        border: none;
        background: #ff4d88;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }
    .stApp {
        background: linear-gradient(135deg, #ffd1dc, #ffe6f0);
    }

    h1, h2, h3, p, label {
        color: #C11C84;
        font-family: 'Georgia', serif;
    }

    .stTextArea textarea {
        background-color: #fff0f5 !important;
        color: black !important;
        border-radius: 10px !important;
        border: 1px solid #ff69b4 !important;
        padding: 10px !important;
        font-family: Georgia, serif !important;
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
# ---------- SESSION STATE INITIALIZATION ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "show_valentine_modal" not in st.session_state:
    st.session_state.show_valentine_modal = False

if "valentine_response" not in st.session_state:
    st.session_state.valentine_response = ""


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
    content_class = "blur" if st.session_state.show_valentine_modal else ""

    st.markdown(f"<div class='{content_class}'>", unsafe_allow_html=True)

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
            st.session_state.valentine_response = (
                "Yayyy 💖🥰<br><br>"
                "You just made my heart the happiest ever!"
            )
            st.session_state.show_valentine_modal = True
            st.rerun()

    with col2:
        if st.button("No 😢"):
            st.session_state.valentine_response = (
                "Oh no 💔😭<br><br>"
                "Think again… love is knocking on your door 💌"
            )
            st.session_state.show_valentine_modal = True
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.show_valentine_modal:
    st.markdown(
        f"""
        <div class="modal-overlay">
            <div class="modal-box">
                <h2>💌</h2>
                <p>{st.session_state.valentine_response}</p>
                <button onclick="window.location.reload()">Close 💖</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
