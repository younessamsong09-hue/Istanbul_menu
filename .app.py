import streamlit as st
from datetime import datetime

# إعداد واجهة VIP (تصميم الهاكرز المحترفين)
st.set_page_config(page_title="Younes Elite", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #00ff00; }
    .chat-bubble {
        background: #111;
        border: 1px solid #00ff00;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
    }
    .user-name { color: #ffffff; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff00; border: 1px solid #00ff00; }
    .stButton>button { background-color: #00ff00; color: black; border-radius: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ YOUNES ELITE SYSTEM")
st.write("---")

# مخزن الرسائل (بدلاً من الجدول الذي يسبب أخطاء حمراء)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"name": "SYSTEM", "text": "تم تفعيل نظام الدردشة المشفر", "time": "00:00"}
    ]

# عرض الرسائل بتصميم فخم
for msg in st.session_state.messages:
    st.markdown(f"""
        <div class="chat-bubble">
            <span class="user-name">@{msg['name']}</span>: 
            <span>{msg['text']}</span>
            <div style="text-align:right; font-size:0.7em; color:#555;">{msg['time']}</div>
        </div>
    """, unsafe_allow_html=True)

# منطقة الإرسال
with st.container():
    u_name = st.text_input("اليوزر:", value="يونس")
    u_msg = st.text_input("رسالة مشفرة...")
    if st.button("إرسال فوري 🚀"):
        if u_msg:
            new_msg = {
                "name": u_name,
                "text": u_msg,
                "time": datetime.now().strftime("%H:%M")
            }
            st.session_state.messages.append(new_msg)
            st.balloons() # تأثير احتفالي مذهل
            st.rerun()

st.info("هذا التطبيق مطور بواسطة المهندس يونس بسيرفرات خاصة.")
