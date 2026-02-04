import streamlit as st

# إعدادات الصفحة الاحترافية باسمك
st.set_page_config(page_title="Younes Azahrai", page_icon="👑", layout="centered")

# إضافة لمسات جمالية باستخدام CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7f9;
    }
    .main-title {
        color: #1E3A8A;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 12px;
        width: 100%;
        border: none;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة المستخدم
st.markdown("<h1 class='main-title'>👑 Younes Azahrai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>مرحباً بك في منصة التواصل الخاصة بك</p>", unsafe_allow_html=True)

# ترتيب الأقسام بشكل جميل
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("📞 ابدأ فيديو"):
        st.markdown("### [اضغط هنا](https://meet.jit.si/YounesAzahraiFamily)")
        st.success("الغرفة جاهزة!")

with col2:
    if st.button("🔄 تحديث"):
        st.rerun()

st.divider()

# منطقة الدردشة المطورة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل بشكل فقاعات
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# إدخال الرسالة
if prompt := st.chat_input("اكتب رسالتك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
    
