import streamlit as st


# --- API Key input + link to generate key ---




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
user_input = st.text_input("Ask your question here(by pressing on the link https://cdn.botpress.cloud/webchat/v3.0/shareable.html?configUrl=https://files.bpcontent.cloud/2025/06/20/11/20250620115114-AGZK5VDG.json")

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
   

# Display messages
for role, msg in st.session_state.messages:
    style = user_style if role == "user" else bot_style
    st.markdown(style.format(msg), unsafe_allow_html=True)
