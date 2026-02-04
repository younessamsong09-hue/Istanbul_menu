import streamlit as st
st.title("🍔 Master Place - تاوريرت")
st.write("اختر وجبتك واطلبها عبر واتساب")
menu = {"طاكوس": "40 درهم", "بيتزا": "35 درهم"}
for dish, price in menu.items():
    if st.button(f"اطلب {dish} ({price})"):
        st.markdown(f"[✅ اضغط هنا لتأكيد الطلب](https://wa.me/212600000000?text=أريد_طلب_{dish})")
