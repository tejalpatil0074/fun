import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="For My Valentine",
    page_icon="❤️",
    layout="centered"
)

# --- CSS STYLING ---
# Injecting custom CSS to match the pink theme, fonts, and animations from your original HTML
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Headings */
    h1 {
        font-family: 'Pacifico', cursive;
        color: #ff4d6d !important;
        text-align: center;
        font-size: 3em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Text */
    p, label, .stTextInput > label, .stTextArea > label, div.stMarkdown {
        color: #5c2c2c !important;
        font-family: 'Quicksand', sans-serif;
        font-size: 1.2em;
        text-align: center;
    }
    
    /* Buttons */
    div.stButton > button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 50px;
        padding: 10px 30px;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        border: none;
        width: 100%;
        font-size: 1.2em;
        transition: transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #ff2a50;
        color: white;
        border: none;
    }
    div.stButton > button:active {
        background-color: #ff2a50;
        color: white;
    }

    /* Input Fields - White Background & Black Text */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        border: 2px solid #ffccd5;
        border-radius: 10px;
        color: #000000 !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #ff4d6d;
        box-shadow: 0 0 5px rgba(255, 77, 109, 0.5);
        color: #000000 !important;
    }
    /* Ensure placeholder text is visible on white background */
    ::placeholder {
        color: #888888 !important;
        opacity: 1;
    }

    /* Photo Frames for Gallery */
    .photo-frame {
        background: white;
        padding: 15px 15px 40px 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: rotate(-3deg);
        transition: transform 0.3s;
        margin-bottom: 20px;
        text-align: center;
        border-radius: 5px;
    }
    .photo-frame:nth-child(even) {
        transform: rotate(3deg);
    }
    .photo-frame:hover {
        transform: scale(1.05) rotate(0deg);
        z-index: 10;
    }
    .caption {
        font-family: 'Pacifico', cursive;
        color: #555;
        margin-top: 10px;
        font-size: 1.2rem;
    }

    /* Floating Hearts Animation */
    @keyframes floatUp {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0.8; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }
    .heart-bg {
        position: fixed;
        color: rgba(255, 255, 255, 0.6);
        animation: floatUp 10s linear infinite;
        font-size: 24px;
        z-index: 0;
        pointer-events: none;
    }
    </style>
    
    <!-- Injecting Floating Hearts -->
    <div class="heart-bg" style="left: 10%; animation-duration: 12s; font-size: 30px;">❤</div>
    <div class="heart-bg" style="left: 25%; animation-duration: 15s; font-size: 20px;">❤</div>
    <div class="heart-bg" style="left: 40%; animation-duration: 8s; font-size: 35px;">❤</div>
    <div class="heart-bg" style="left: 60%; animation-duration: 11s; font-size: 25px;">❤</div>
    <div class="heart-bg" style="left: 75%; animation-duration: 14s; font-size: 32px;">❤</div>
    <div class="heart-bg" style="left: 90%; animation-duration: 9s; font-size: 28px;">❤</div>
    """, unsafe_allow_html=True)

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 1

# --- PAGE 1: AUTHENTICATION ---
if st.session_state.page == 1:
    st.markdown("<h1>Hey Handsome! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p>Before we start, I need to know who is here.</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>What is the name of your girlfriend?</strong></p>", unsafe_allow_html=True)
    
    # Using a form to allow 'Enter' key submission
    with st.form("name_form"):
        name_input = st.text_input("Type her name...", label_visibility="collapsed")
        submitted = st.form_submit_button("Enter")
        
        if submitted:
            name = name_input.strip().lower()
            if name == "tejal":
                st.error("Wait a minute! No, that's not correct! 😤 Please write what you love to call her. It should be either 'Baby' or 'Teju'.")
            elif name in ["baby", "teju"]:
                st.session_state.page = 2
                st.rerun()
            else:
                st.error("Hmm... That's not the magic word! Try 'Baby' or 'Teju'. 😉")

# --- PAGE 2: QUIZ ---
elif st.session_state.page == 2:
    st.markdown("<h1>Pop Quiz! 📝</h1>", unsafe_allow_html=True)
    st.markdown("<p>Let's see how well you know us...</p>", unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        q1 = st.text_input("1. Where did we first meet?")
        q2 = st.text_input("2. What is my favorite thing to eat?")
        q3 = st.text_area("3. Why do you love me? (Be cute!)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            if q1 and q2 and q3:
                st.session_state.page = 3
                st.rerun()
            else:
                st.error("Hey! You have to answer all the questions! No skipping! 😠")

# --- PAGE 3: GALLERY ---
elif st.session_state.page == 3:
    st.markdown("<h1>Us & Memories ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p>Every moment with you is my favorite.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gallery Columns
    c1, c2, c3 = st.columns(3)
    
    # You can replace the src links below with actual image URLs or local paths
    with c1:
        st.markdown("""
        <div class="photo-frame">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Teju" width="100%" style="border-radius: 5px;">
            <div class="caption">Cutie</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="photo-frame">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Love" width="100%" style="border-radius: 5px;">
            <div class="caption">Love</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="photo-frame">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Happy" width="100%" style="border-radius: 5px;">
            <div class="caption">Forever</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ff4d6d; font-style: italic;'>\"You are the best thing that's ever been mine.\"</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Next ➡️"):
        st.session_state.page = 4
        st.rerun()

# --- PAGE 4: PROPOSAL ---
elif st.session_state.page == 4:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1>Will you be my Valentine? 🌹</h1>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 5em; text-align: center;'>🥺👉👈</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("YES! ❤️"):
            st.session_state.page = 5
            st.balloons()
            st.rerun()
            
    with col2:
        if st.button("No 🙄"):
            st.error("Excuse me? You can't say no! Try hitting the other button. 😤🔪")

# --- PAGE 5: SUCCESS ---
elif st.session_state.page == 5:
    st.markdown("<h1>Yay!!! 🎉❤️</h1>", unsafe_allow_html=True)
    
    # Centered Image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size: 1.5em; color: #ff4d6d; font-weight: bold;">
            Thank you, I love you! <br>
            It's a very special Valentine for me.
        </p>
        <p style="font-size: 2em;">❤️❤️❤️</p>
    </div>
    """, unsafe_allow_html=True)
