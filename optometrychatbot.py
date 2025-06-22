import streamlit as st
import streamlit.components.v1 as components

# --- App Title ---
st.title("🧑‍⚕️ Optometry Chatbot (India)")
st.markdown("Chat with the Optometry Assistant below (powered by Botpress):")

# --- Embed Botpress Chat Widget ---
components.html("""
    <script src="https://cdn.botpress.cloud/webchat/v3.0/ui.js"></script>
    <script>
        window.botpressWebChat.init({
            "configUrl": "https://files.bpcontent.cloud/2025/06/20/11/20250620115114-AGZK5VDG.json",
            "botId": "optometry-bot",
            "hostUrl": "https://cdn.botpress.cloud/webchat/v3.0",
            "showCloseButton": true,
            "showPoweredBy": false,
            "enableConversationDeletion": false,
            "containerWidth": "100%",
            "layoutWidth": "100%",
        });
    </script>
""", height=600)
