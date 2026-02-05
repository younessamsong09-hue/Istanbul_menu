import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# إعداد واجهة التطبيق
st.set_page_config(page_title="واتساب يونس", page_icon="💬")

# الاتصال بالجدول (يجب أن يكون الرابط في Secrets)
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(ttl="1s")

st.title("👑 واتساب عائلة يونس")

# عرض الرسائل القديمة
for index, row in df.iterrows():
    st.info(f"**{row['name']}**: {row['message']} ({row['time']})")

# كتابة رسالة جديدة
with st.form("chat"):
    u_name = st.text_input("اسمك:", value="يونس")
    u_msg = st.text_input("رسالتك:")
    if st.form_submit_button("إرسال"):
        new_row = pd.DataFrame([{"name": u_name, "message": u_msg, "time": datetime.now().strftime("%H:%M")}])
        updated_df = pd.concat([df, new_row], ignore_index=True)
        conn.update(data=updated_df)
        st.success("تم الإرسال!")
        st.rerun()
        
