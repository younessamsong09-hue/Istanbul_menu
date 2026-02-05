
    import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="واتساب عائلة يونس", page_icon="💬")

# الاتصال بجدول بيانات جوجل
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("👑 واتساب عائلة يونس")

# قراءة الرسائل من الجدول
df = conn.read(ttl="1s") # تحديث كل ثانية لجعلها سريعة

# عرض الرسائل بستايل جميل
for index, row in df.iterrows():
    style = "text-align: right; background-color: #dcf8c6;" if row['name'] == "يونس" else "text-align: left; background-color: #ffffff;"
    st.markdown(f"""
        <div style="padding: 10px; border-radius: 10px; margin: 5px; {style} border: 1px solid #ddd;">
            <b>{row['name']}</b>: {row['message']}<br>
            <small style="color: gray;">{row['time']}</small>
        </div>
    """, unsafe_allow_html=True)

# خانة الكتابة
with st.form("chat_form"):
    u_name = st.text_input("اسمك:", value="يونس")
    u_msg = st.text_input("اكتب رسالة...")
    submit = st.form_submit_button("إرسال 🚀")

    if submit and u_name and u_msg:
        new_data = pd.DataFrame([{
            "name": u_name,
            "message": u_msg,
            "time": datetime.now().strftime("%H:%M")
        }])
        updated_df = pd.concat([df, new_data], ignore_index=True)
        conn.update(data=updated_df)
        st.success("تم الإرسال!")
        st.rerun()
        
