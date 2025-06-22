import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Optometry Chatbot", layout="centered")

st.title("🧑‍⚕️ Optometry Chatbot (India)")

st.markdown("Chat live with the assistant below:")

# Embed Botpress WebChat widget
components.html("""
    <script src="https://cdn.botpress.cloud/webchat/v3.0/ui.js"></script>
    <script>
      window.botpressWebChat.init({
        "botId": "optometry-bot",
        "hostUrl": "https://cdn.botpress.cloud/webchat/v3.0",
        "messagingUrl": "https://messaging.botpress.cloud",
        "clientId": "optometry-bot",
        "webhookId": "default",
        "configUrl": "https://files.bpcontent.cloud/2025/06/20/11/20250620115114-AGZK5VDG.json",
        "containerWidth": "100%",
        "layoutWidth": "100%",
        "showCloseButton": true,
        "showPoweredBy": false,
        "enableConversationDeletion": false,
        "embedded": true
      });
    </script>
    <div id="bp-web-widget" style="height: 600px;"></div>
""", height=600)
