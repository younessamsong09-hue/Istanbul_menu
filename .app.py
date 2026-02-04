import streamlit as st
import time

# إعدادات الصفحة الملكية
st.set_page_config(page_title="Younes Azahrai Chat", page_icon="👑", layout="wide")

# زينة قوية: تصميم CSS مخصص للألوان والتحركات
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق */
    .stApp {
        background: linear-gradient(to bottom, #1e3c72, #2a5298);
        color: white;
    }
    /* تصميم العنوان الملكي */
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 0px;
    }
    /* تصميم الأزرار */
    .stButton>button {
        border-radius: 50px;
        border: 2px solid #FFD700;
        background-color: rgba(255, 215, 0, 0.1);
        color: white;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FFD700;
        color: #1e3c72;
        transform: scale(1.05);
    }
    /* زينة الرسائل */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        border-left: 5px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# الواجهة الرئيسية
st.markdown("<h1 class='main-title'>👑 YOUNES AZAHRAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>مرحباً بكم في المنصة العالمية لآل الزهراوي</p>", unsafe_allow_html=True)

# إضافة ساعة رقمية بتوقيت المغرب
t = time.strftime("%H:%M:%S")
st.markdown(f"<p style='text-align: center; color: #FFD700;'>🕒 توقيت تاوريرت الآن: {t}</p>", unsafe_allow_html=True)

st.divider()

# قسم الأزرار التفاعلية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 انضم الآن لمكالمة الفيديو"):
        st.balloons() # زينة احتفالية عند الضغط
        st.markdown("### [👉 اضغط هنا للدخول لغرفة الفيديو](https://meet.jit.si/YounesAzahraiFamily)")
        st.info("تم فتح الغرفة المؤمنة بنجاح.")

# منطقة الدردشة
st.subheader("💬 سجل التواصل الاجتماعي")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("اكتب رسالة لليونس..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
    
