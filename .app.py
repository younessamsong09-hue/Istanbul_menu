import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="عائلة يونس", page_icon="👑")

st.title("👑 تطبيق يونس العائلي")
st.write("دردشة مباشرة ومكالمات فيديو سريعة")

# نظام الدردشة البسيط (في الذاكرة)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for msg in st.session_state.messages:
    st.chat_message("user").write(f"**{msg['name']}:** {msg['text']}")

# إدخال رسالة جديدة
with st.container():
    name = st.text_input("اسمك:", placeholder="اكتب اسمك هنا")
    text = st.text_input("رسالتك:", placeholder="اكتب رسالتك هنا")
    if st.button("إرسال 🚀"):
        if name and text:
            st.session_state.messages.append({"name": name, "text": text})
            st.rerun()

st.divider()

# زر مكالمة الفيديو
if st.button("🎥 ابدأ مكالمة فيديو الآن"):
    st.info("اضغط على 'Join in browser' في الأسفل للدخول فوراً")
    components.html(
        f'<iframe src="https://meet.jit.si/YounesFamilyRoom123" allow="camera; microphone; fullscreen; display-capture" style="height: 500px; width: 100%; border:0;"></iframe>',
        height=500,
    )
    
