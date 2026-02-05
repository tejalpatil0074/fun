import streamlit as st

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("Hello My Love!!")

    q1 = st.text_input("1️⃣ What comes to your mind when you hear the word *love*?")
    q2 = st.text_input("2️⃣ Do you believe small moments matter more than big ones?")
    q3 = st.text_input("3️⃣ One word that makes you smile? 😊")

    if st.button("Next ➡️"):
        if not q1 or not q2 or not q3:
            st.warning("Please answer all questions ✨")
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
