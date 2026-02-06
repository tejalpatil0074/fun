import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="For My Valentine",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 📸 IMAGE LOADER FUNCTION ---
# This allows you to use local files! 
def get_img_as_base64(file_path):
    """Reads a local image file and converts it to a base64 string for HTML."""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        # Detect extension for correct MIME type
        ext = file_path.split('.')[-1].lower()
        mime_type = "image/gif" if ext == "gif" else "image/jpeg"
        if ext == "png": mime_type = "image/png"
        
        return f"data:{mime_type};base64,{encoded}"
    except FileNotFoundError:
        # Fallback if image isn't found (prevents crash)
        return "https://api.dicebear.com/7.x/avataaars/svg?seed=Error"

# --- ⚙️ UPDATE YOUR IMAGES HERE ---
# Just put the image names here. Ensure these files are in the SAME FOLDER as this script.
# You can use .jpg, .png, or .gif
IMG_1_PATH = "pic1.jpeg"   # Replace with your actual file name
IMG_2_PATH = "pic2.jpeg"   # Replace with your actual file name
IMG_3_PATH = "pic3.jpeg"   # Replace with your actual file name
SUCCESS_GIF_PATH = "success.gif" # You can use a local GIF or a URL

# Convert local paths to base64 data so HTML can read them
img_1_src = get_img_as_base64(IMG_1_PATH)
img_2_src = get_img_as_base64(IMG_2_PATH)
img_3_src = get_img_as_base64(IMG_3_PATH)

# For the GIF, we check if it's a URL or a file
if SUCCESS_GIF_PATH.startswith("http"):
    success_src = SUCCESS_GIF_PATH
else:
    success_src = get_img_as_base64(SUCCESS_GIF_PATH)


# --- CSS TO REMOVE STREAMLIT PADDING ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# --- THE HTML CODE ---
# We use placeholders like {{IMG_1}} which we will replace with the Base64 data
html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Valentine</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            font-family: 'Quicksand', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
            overflow-x: hidden;
            color: #5c2c2c;
        }

        /* Floating Hearts Animation Background */
        .hearts-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            pointer-events: none;
            overflow: hidden;
        }

        .heart-particle {
            position: absolute;
            color: rgba(255, 255, 255, 0.5);
            animation: floatUp 10s linear infinite;
            font-size: 20px;
        }

        @keyframes floatUp {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }

        /* Container for pages */
        .container {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 90%;
            position: relative;
            border: 4px solid #fff;
        }

        h1 {
            font-family: 'Pacifico', cursive;
            color: #ff4d6d;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 0px rgba(255,255,255,0.5);
        }

        p {
            font-size: 1.2em;
            margin-bottom: 20px;
            font-weight: 600;
        }

        /* Forced White Background and Black Text for Inputs */
        input, textarea {
            width: 80%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #ffccd5;
            border-radius: 10px;
            font-family: 'Quicksand', sans-serif;
            font-size: 1em;
            outline: none;
            transition: border-color 0.3s;
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        input:focus, textarea:focus {
            border-color: #ff4d6d;
            box-shadow: 0 0 8px rgba(255, 77, 109, 0.3);
        }
        
        ::placeholder {
            color: #999;
        }

        button {
            background-color: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1.1em;
            cursor: pointer;
            font-family: 'Quicksand', sans-serif;
            font-weight: bold;
            transition: transform 0.2s, background 0.2s;
            margin: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        button:hover {
            transform: scale(1.05);
            background-color: #ff2a50;
        }

        button.secondary {
            background-color: #ffccd5;
            color: #5c2c2c;
        }

        /* Hide all pages by default, logic will show them */
        .page {
            display: none;
            animation: fadeIn 0.8s ease;
        }

        .page.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Custom Styles for Gallery */
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
        }

        .photo-frame {
            background: white;
            padding: 10px 10px 30px 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transform: rotate(-3deg);
            width: 120px;
            transition: transform 0.3s;
            border-radius: 4px;
        }

        .photo-frame:nth-child(even) {
            transform: rotate(3deg);
        }

        .photo-frame:hover {
            transform: scale(1.1) rotate(0deg);
            z-index: 10;
        }

        .photo-frame img {
            width: 100%;
            height: 120px; /* Fixed height for consistency */
            object-fit: cover;
            border: 1px solid #eee;
            border-radius: 2px;
        }

        .photo-frame span {
            display: block;
            margin-top: 8px;
            font-family: 'Pacifico', cursive;
            font-size: 1em;
            color: #555;
        }

        /* Modal Styles with Blur Effect */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.4); /* Dark dimming */
            backdrop-filter: blur(8px);      /* The blur effect you wanted */
            -webkit-backdrop-filter: blur(8px); /* Safari support */
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }

        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            max-width: 320px;
            border: 4px solid #ffccd5;
            box-shadow: 0 15px 40px rgba(0,0,0,0.2);
            animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes popIn {
            from { transform: scale(0.5); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

    </style>
</head>
<body>

    <!-- Floating Hearts Background -->
    <div class="hearts-bg" id="hearts-bg"></div>

    <div class="container">
        
        <!-- PAGE 1: AUTHENTICATION -->
        <div id="page1" class="page active">
            <h1>Hey Handsome! ❤️</h1>
            <p>Before we start, I need to know who is here.</p>
            <p><strong>What is the name of your girlfriend?</strong></p>
            <input type="text" id="gfNameInput" placeholder="Type her name..." autocomplete="off">
            <br>
            <button onclick="checkName()">Enter</button>
        </div>

        <!-- PAGE 2: QUIZ -->
        <div id="page2" class="page">
            <h1>Pop Quiz! 📝</h1>
            <p>Let's see how well you know us...</p>
            
            <div style="text-align: left; margin-top: 20px;">
                <label>1. Where did we first meet?</label>
                <input type="text" id="q1" placeholder="Your answer...">
                
                <label>2. What is my favorite thing to eat?</label>
                <input type="text" id="q2" placeholder="Your answer...">
                
                <label>3. Why do you love me? (Be cute!)</label>
                <textarea id="q3" rows="3" placeholder="Write something sweet..."></textarea>
            </div>
            
            <button onclick="submitQuiz()">Submit Answers</button>
        </div>

        <!-- PAGE 3: GALLERY -->
        <div id="page3" class="page">
            <h1>Us & Memories ✨</h1>
            <p>Every moment with you is my favorite.</p>
            
            <div class="gallery">
                <div class="photo-frame">
                    <img src="{{IMG_1}}" alt="You">
                    <span>Cutie</span>
                </div>
                
                <div class="photo-frame">
                    <img src="{{IMG_2}}" alt="Us">
                    <span>Love</span>
                </div>
                
                <div class="photo-frame">
                    <img src="{{IMG_3}}" alt="Fun">
                    <span>Forever</span>
                </div>
            </div>

            <p style="font-style: italic; color: #ff4d6d;">"You are the best thing that's ever been mine."</p>
            <button onclick="goToProposal()">Next ➡️</button>
        </div>

        <!-- PAGE 4: PROPOSAL -->
        <div id="page4" class="page">
            <h1 style="font-size: 3em; margin-bottom: 10px;">Will you be my Valentine? 🌹</h1>
            <div style="font-size: 5em; margin: 20px;">🥺👉👈</div>
            
            <div style="margin-top: 30px;">
                <button onclick="acceptProposal()" style="font-size: 1.5em; padding: 15px 40px;">YES! ❤️</button>
                <button class="secondary" onclick="rejectProposal()" style="font-size: 1.2em;">No 🙄</button>
            </div>
        </div>

        <!-- PAGE 5: SUCCESS -->
        <div id="page5" class="page">
            <h1>Yay!!! 🎉❤️</h1>
            <img src="{{SUCCESS_GIF}}" alt="Happy" style="width: 100%; border-radius: 10px; margin-bottom: 20px;">
            <p style="font-size: 1.5em; color: #ff4d6d; font-weight: bold;">
                Thank you, I love you! <br>
                It's a very special Valentine for me.
            </p>
            <p style="font-size: 2em;">❤️❤️❤️</p>
        </div>

    </div>

    <!-- Custom Modal for Alerts -->
    <div id="customModal" class="modal">
        <div class="modal-content">
            <h2 id="modalTitle" style="color: #ff4d6d;">Oops!</h2>
            <p id="modalMessage">Something went wrong.</p>
            <button onclick="closeModal()">Okay...</button>
        </div>
    </div>

    <script>
        // --- LOGIC ---

        function checkName() {
            const name = document.getElementById('gfNameInput').value.trim().toLowerCase();
            
            if (name === "tejal") {
                showModal("Wait a minute!", "No, that's not correct! 😤 Please write what you love to call her. It should be either 'Baby' or 'Teju'.");
            } else if (name === "baby" || name === "teju") {
                nextPage('page1', 'page2');
            } else {
                showModal("Hmm...", "That's not the magic word! Try 'Baby' or 'Teju'. 😉");
            }
        }

        function submitQuiz() {
            const q1 = document.getElementById('q1').value;
            const q2 = document.getElementById('q2').value;
            const q3 = document.getElementById('q3').value;

            if(q1 && q2 && q3) {
                // Moving to gallery
                nextPage('page2', 'page3');
            } else {
                showModal("Hey!", "You have to answer all the questions! No skipping! 😠");
            }
        }

        function goToProposal() {
            nextPage('page3', 'page4');
        }

        function rejectProposal() {
            showModal("Excuse me?", "You can't say no! Try hitting the other button. 😤🔪");
        }

        function acceptProposal() {
            createConfetti();
            nextPage('page4', 'page5');
        }

        // --- UTILS ---

        function nextPage(currentId, nextId) {
            document.getElementById(currentId).classList.remove('active');
            document.getElementById(nextId).classList.add('active');
        }

        function showModal(title, message) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalMessage').innerText = message;
            document.getElementById('customModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('customModal').style.display = 'none';
        }

        // --- BACKGROUND EFFECTS ---

        // Floating Hearts Background
        function createHearts() {
            const container = document.getElementById('hearts-bg');
            for(let i=0; i<20; i++) {
                const heart = document.createElement('div');
                heart.classList.add('heart-particle');
                heart.innerHTML = '❤';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.animationDuration = Math.random() * 5 + 5 + 's';
                heart.style.fontSize = Math.random() * 20 + 10 + 'px';
                container.appendChild(heart);
            }
        }
        
        // Confetti Effect for Yes
        function createConfetti() {
            const colors = ['#ff4d6d', '#ffccd5', '#ffffff', '#ffeb3b'];
            for (let i = 0; i < 100; i++) {
                const confetti = document.createElement('div');
                confetti.style.position = 'fixed';
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.top = '-10px';
                confetti.style.width = '10px';
                confetti.style.height = '10px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.animation = `floatUp ${Math.random() * 2 + 3}s linear`;
                confetti.style.zIndex = '9999';
                document.body.appendChild(confetti);
            }
        }

        // Start background hearts immediately
        createHearts();

    </script>
</body>
</html>
"""

# --- INJECT USER VARIABLES INTO HTML ---
# This replaces the {{PLACEHOLDERS}} in the HTML with your Python base64 strings
final_html = html_code.replace("{{IMG_1}}", img_1_src) \
                      .replace("{{IMG_2}}", img_2_src) \
                      .replace("{{IMG_3}}", img_3_src) \
                      .replace("{{SUCCESS_GIF}}", success_src)

# --- RENDER THE HTML ---
components.html(final_html, height=1000, scrolling=True)
