import streamlit as st
import openai

# --- API Key input + link to generate key ---
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.markdown(
    """
    Need an OpenAI API key?  
    <a href="https://platform.openai.com/account/api-keys" target="_blank" style="color: #4CAF50; font-weight: bold;">
        Click here to create one
    </a>
    """,
    unsafe_allow_html=True
)

api_key_input = st.text_input(
    "Enter your OpenAI API Key:", type="password", value=st.session_state.api_key
)

if api_key_input:
    st.session_state.api_key = api_key_input
    openai.api_key = st.session_state.api_key
else:
    st.warning("Please enter your OpenAI API Key to use the chatbot.")
    st.stop()

# Optometry syllabus context
syllabus_context = """
Bachelor of Optometry Syllabus (India):

Semester 1:
- General Anatomy
- General Physiology
- Health Care Delivery Systems of India
- Communication Skills for Healthcare Professionals
- Medical Terminology and Record-keeping
- Computer Applications
- Nutrition
- Geometrical Optics I

Semester 2:
- General Biochemistry
- General Pharmacology
- Healthcare Professionalism and Values
- Ocular Anatomy
- Ocular Physiology
- Physical Optics
- Directed Clinical Education I

Semester 3:
- Ocular Biochemistry
- Geometrical Optics II
- General and Ocular Microbiology
- Visual Optics I
- Optometric Optics I
- Optometric Instruments
- Ocular Diseases I
- Directed Clinical Education II

Semester 4:
- Clinical Examination of the Ocular System
- Optometric Optics II
- Visual Optics II
- Ocular Diseases II
- General and Ocular Pathology
- Ocular Pharmacology
- Patient Safety and Quality Assurance
- Directed Clinical Education III

Semester 5:
- Contact Lens I
- Low Vision Care
- Geriatric and Pediatric Optometry
- Binocular Vision I
- Systemic Diseases and the Eye
- Medical Psychology
- Constitution of India, Medical Law and Ethics
- Environmental Science
- Open Elective I
- Directed Clinical Education IV

Semester 6:
- Contact Lens II
- Binocular Vision II
- Public Health and Community Optometry
- Occupational Optometry
- Practice Management
- Research Methodology and Biostatistics
- Communication Skills II
- Open Elective II
- Directed Clinical Education V

Semesters 7 & 8:
- Research Project
- Clinical Internship
"""

# System message for GPT
system_message = f"""
You are a helpful assistant for Bachelor of Optometry students in India.
Use the following syllabus to answer questions accurately and clearly.

{syllabus_context}
"""

# Inline CSS for user and bot chat bubbles
user_style = """
<div style="
    background-color:#4682B4;
    padding:10px;
    border-radius:10px;
    margin:10px 0;
    max-width:70%;
    font-family: Arial, sans-serif;
    word-wrap: break-word;
">
<b>You:</b> {}</div>
"""

bot_style = """
<div style="
    background-color:#006400;
    padding:10px;
    border-radius:10px;
    margin:10px 0;
    max-width:70%;
    font-family: Arial, sans-serif;
    word-wrap: break-word;
    color: #D0FFD6;
">
<b>Bot:</b> {}</div>
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI
st.title("🧑‍⚕️ Optometry Chatbot (India)")
user_input = st.text_input("Ask your question here:")

# Process input
if user_input:
    st.session_state.messages.append(("user", user_input))

    # Prepare messages for GPT
    chat_messages = [{"role": "system", "content": system_message}]
    for role, msg in st.session_state.messages:
        chat_messages.append({
            "role": "user" if role == "user" else "assistant",
            "content": msg
        })

    # Call OpenAI
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_messages,
            max_tokens=500,
            temperature=0.7
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"

    st.session_state.messages.append(("bot", bot_reply))

# Display messages
for role, msg in st.session_state.messages:
    style = user_style if role == "user" else bot_style
    st.markdown(style.format(msg), unsafe_allow_html=True)
