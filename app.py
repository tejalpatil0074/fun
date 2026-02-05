import streamlit as st

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("💭 Quick Questions")

    st.write("Do you believe in love?")
    st.write("❤️ ❤️ ❤️")

    if st.button("Next ➡️"):
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
