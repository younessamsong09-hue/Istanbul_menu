import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="واتساب يونس", page_icon="💬")

# الاتصال بالجدول
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(ttl="1s")
except:
    st.error("تأكد من وضع رابط الجدول في Secrets")
    st.stop()

st.title("👑 واتساب عائلة يونس")

# عرض الرسائل
for index, row in df.iterrows():
    style = "background-color: #dcf8c6; text-align: right;" if row['name'] == "يونس" else "background-color: #ffffff; text-align: left;"
    st.markdown(f"""
        <div style="padding: 10px; border-radius: 10px; margin: 5px; {style} border: 1px solid #ddd;">
            <b>{row['name']}</b>: {row['message']}<br>
            <small style="color: gray;">{row['time']}</small>
        </div>
    """, unsafe_allow_html=True)

# نموذج الإرسال
with st.form("chat_form", clear_on_submit=True):
    u_name = st.text_input("اسمك:", value="يونس")
    u_msg = st.text_input("اكتب رسالة...")
    if st.form_submit_button("إرسال 🚀"):
        if u_name and u_msg:
            new_data = pd.DataFrame([{"name": u_name, "message": u_msg, "time": datetime.now().strftime("%H:%M")}])
            updated_df = pd.concat([df, new_data], ignore_index=True)
            conn.update(data=updated_df)
            st.rerun()
            
