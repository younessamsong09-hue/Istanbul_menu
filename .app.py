import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="واتساب يونس", page_icon="💬", layout="centered")

# تصميم CSS لجعل الرسائل تشبه الواتساب
st.markdown("""
    <style>
    .main { background-color: #e5ddd5; }
    .chat-bubble {
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px;
        max-width: 70%;
        font-family: sans-serif;
        position: relative;
    }
    .sent {
        background-color: #dcf8c6;
        align-self: flex-end;
        margin-left: auto;
        border-bottom-right-radius: 2px;
    }
    .received {
        background-color: #ffffff;
        align-self: flex-start;
        margin-right: auto;
        border-bottom-left-radius: 2px;
    }
    .time {
        font-size: 0.7em;
        color: #888;
        text-align: right;
        margin-top: 5px;
    }
    .name {
        font-weight: bold;
        font-size: 0.8em;
        color: #075e54;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👑 واتساب عائلة يونس")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل بستايل الواتساب
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        # إذا كان يونس هو المرسل نختار sent وإلا received
        style = "sent" if msg['name'] == "يونس" else "received"
        st.markdown(f"""
            <div class="chat-bubble {style}">
                <div class="name">{msg['name']}</div>
                <div>{msg['text']}</div>
                <div class="time">{msg['time']}</div>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# منطقة الكتابة (تشبه شريط الواتساب السفلي)
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        u_name = st.text_input("اسمك:", value="يونس", key="name_input")
        u_msg = st.text_input("اكتب رسالة...", key="msg_input")
    with col2:
        st.write(" ")
        if st.button("إرسال ✅"):
            if u_name and u_msg:
                now = datetime.now().strftime("%H:%M")
                st.session_state.messages.append({"name": u_name, "text": u_msg, "time": now})
                st.rerun()

st.divider()

# زر الفيديو
if st.button("🎥 بدء مكالمة فيديو عائلية"):
    st.info("انزل للأسفل واضغط على 'Join in browser'")
    components.html(
        f'<iframe src="https://meet.jit.si/YounesWhatsAppRoom" allow="camera; microphone; fullscreen" style="height: 450px; width: 100%; border:0;"></iframe>',
        height=450,
    )
    
