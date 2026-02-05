import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعداد واجهة فخمة (الستايل الحديث)
st.set_page_config(page_title="Younes Pro Chat", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%); color: white; }
    .stTextInput>div>div>input { background-color: #3d3d5c; color: white; border-radius: 10px; }
    .chat-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #00ff88;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .user-name { color: #00ff88; font-weight: bold; font-size: 0.9em; }
    .msg-text { color: #ffffff; font-size: 1.1em; margin-top: 5px; }
    .msg-time { color: #aaa; font-size: 0.7em; text-align: right; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Younes Pro Chat v2.0")
st.write("---")

# 2. جلب البيانات (سنستخدم طريقة القراءة المباشرة لتجنب الأخطاء)
sheet_url = st.secrets["connections"]["gsheets"]["spreadsheet"]
csv_url = sheet_url.replace("/edit?usp=drivesdk", "/export?format=csv")
csv_url = csv_url.replace("/edit#gid=0", "/export?format=csv")

try:
    df = pd.read_csv(csv_url)
except:
    st.error("يرجى التأكد من أن الجدول 'Editor' للجميع")
    st.stop()

# 3. عرض الرسائل بتصميم عصري
for index, row in df.tail(10).iterrows(): # عرض آخر 10 رسائل
    st.markdown(f"""
        <div class="chat-card">
            <div class="user-name">@{row['name']}</div>
            <div class="msg-text">{row['message']}</div>
            <div class="msg-time">{row['time']}</div>
        </div>
    """, unsafe_allow_html=True)

# 4. منطقة الإرسال (تجاوز خطأ الكتابة)
with st.container():
    with st.form("modern_chat", clear_on_submit=True):
        col1, col2 = st.columns([1, 3])
        with col1: u_name = st.text_input("اليوزر:", value="يونس")
        with col2: u_msg = st.text_input("اكتب شيئاً مذهلاً...")
        
        submit = st.form_submit_button("إرسال فوري 🚀")
        
        if submit and u_msg:
            st.warning("يونس، الكتابة التلقائية في الجداول تتطلب 'Google Apps Script' لتعمل بدون أخطاء حمراء.")
            st.info("سأعطيك كود صغير تضعه داخل جدول جوجل ليفتح لك الطريق فوراً!")
            
