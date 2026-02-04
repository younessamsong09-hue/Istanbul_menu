import streamlit as st

# الإعدادات الجديدة بالاسم الذي طلبته
st.set_page_config(page_title="Younes Azahrai", page_icon="💬")

st.title("💬 Younes Azahrai - دردشة وفيديو")

# قسم مكالمة الفيديو
st.sidebar.header("📞 الإتصال")
if st.sidebar.button("بدء مكالمة فيديو"):
    st.markdown("### [اضغط هنا للدخول للمكالمة](https://meet.jit.si/YounesAzahraiFamily)")
    st.info("سيتم فتح غرفة فيديو آمنة لعائلتك.")

# نظام الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("اكتب رسالتك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
