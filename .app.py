import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Younes Azahrai", page_icon="👑")

st.markdown("<h1 style='text-align: center;'>👑 Younes Azahrai</h1>", unsafe_allow_html=True)

# --- قسم مكالمة الفيديو ---
st.subheader("📞 التواصل المباشر")
# رابط غرفة فيديو فريدة لعائلتك
video_room_url = "https://meet.jit.si/YounesAzahraiFamily2026"

if st.button("🚀 ابدأ مكالمة الفيديو الآن"):
    st.balloons()
    # فتح الرابط في صفحة جديدة
    st.markdown(f'<a href="{video_room_url}" target="_blank" style="text-decoration: none;"><button style="width:100%; background-color: #28a745; color: white; padding: 15px; border: none; border-radius: 10px; font-size: 18px; cursor: pointer;">👉 اضغط هنا لدخول الغرفة</button></a>', unsafe_allow_html=True)
    st.info("سيتم فتح الكاميرا في صفحة جديدة، تأكد من إعطاء إذن الكاميرا.")

st.divider()

# --- قسم الدردشة العائلية ---
st.subheader("💬 سجل الرسائل")

# ملاحظة لليونس: حالياً الرسائل تظهر لكل شخص بمفرده
# لجعلها تظهر للكل، سنحتاج لخطوة بسيطة لربط Google Sheets لاحقاً
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# إدخال رسالة جديدة
if prompt := st.chat_input("اكتب رسالتك هنا..."):
    # إضافة الرسالة للذاكرة
    st.session_state.messages.append({"role": "user", "content": prompt})
    # إعادة تحميل الصفحة لإظهار الرسالة
    st.rerun()
    
