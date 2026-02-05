import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="واتساب يونس", page_icon="💬")

# الاتصال بالجدول
conn = st.connection("gsheets", type=GSheetsConnection)

# قراءة البيانات مع تحديث سريع
df = conn.read(ttl="1s")

st.title("👑 واتساب عائلة يونس")

# عرض الرسائل بشكل جميل
if not df.empty:
    for index, row in df.iterrows():
        with st.chat_message("user"):
            st.write(f"**{row['name']}**: {row['message']}")
            st.caption(f"🕒 {row['time']}")

# منطقة الإرسال
with st.container():
    u_name = st.text_input("اسمك:", value="يونس", key="u_name")
    u_msg = st.text_input("رسالتك:", key="u_msg")
    
    if st.button("إرسال 🚀"):
        if u_name and u_msg:
            # تجهيز السطر الجديد بنفس عناوين جدولك
            new_row = pd.DataFrame([{
                "name": u_name,
                "message": u_msg,
                "time": datetime.now().strftime("%H:%M")
            }])
            # دمج وإرسال
            updated_df = pd.concat([df, new_row], ignore_index=True)
            conn.update(data=updated_df)
            st.success("تم إرسال رسالتك بنجاح!")
            st.rerun()
            
