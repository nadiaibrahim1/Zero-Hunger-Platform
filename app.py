import streamlit as st
import pandas as pd

# 1. إعدادات تجعل التطبيق يملأ الشاشة بالكامل (Wide Mode)
st.set_page_config(page_title="Zero Hunger AI", page_icon="🌍", layout="wide")

# 2. إضافة لمسة جمالية بالألوان (Custom CSS)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر مع صورة أو أيقونة كبيرة
col_header1, col_header2 = st.columns([1, 4])
with col_header1:
    st.title("🌍")
with col_header2:
    st.title("Zero Hunger Smart Logistics System")
    st.write("Professional MIS Solution for Food Waste Management")

st.markdown("---")

# 4. القائمة الجانبية بشكل أشيك
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3771/3771144.png", width=100)
st.sidebar.title("Navigation Center")
menu = st.sidebar.radio("Go to:", ["📊 Analytics Dashboard", "🏬 Restaurant Portal", "🚚 Volunteer Tracking"])

# 5. لوحة التحكم (التحليلات) - دي بتخلي الشكل "جامد"
if menu == "📊 Analytics Dashboard":
    st.header("Global Impact Overview")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Meals Saved", "1,240", "+15%")
    kpi2.metric("Active Restaurants", "45", "+2")
    kpi3.metric("CO2 Reduction", "5.2 Tons", "+0.8")
    
    st.subheader("Recent Activity Map")
    # دي خريطة وهمية بتبين أماكن التوزيع
    map_data = pd.DataFrame({'lat': [30.0444, 30.0626, 30.05], 'lon': [31.2357, 31.2497, 31.22]})
    st.map(map_data)

# 6. بوابة المطاعم
elif menu == "🏬 Restaurant Portal":
    st.header("Restaurant Management Console")
    with st.expander("Add New Surplus Food Entry", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            res_name = st.text_input("Entity Name", placeholder="e.g. Grand Plaza Hotel")
            f_type = st.multiselect("Food Type", ["Cooked", "Raw", "Bakery", "Beverages"])
        with c2:
            portions = st.number_input("Portions", min_value=1)
            loc = st.text_input("Exact Pickup Address")
        
        desc = st.text_area("Logistics Notes (e.g. Cold storage required)")
        
        if st.button("🚀 Push to Cloud Network"):
            st.success("Data transmitted to AI routing system!")
            st.balloons()

# 7. بوابة المتطوعين
else:
    st.header("Logistics & Routing")
    st.info("The AI is currently matching 5 nearby volunteers to available pickups.")
    # جدول احترافي
    data = {
        "Route ID": ["RT-101", "RT-105"],
        "Destination": ["Charity A", "Shelter B"],
        "Priority": ["High", "Medium"],
        "ETA": ["15 mins", "40 mins"]
    }
    st.table(pd.DataFrame(data))

# Footer
st.sidebar.write("---")
st.sidebar.caption("System Status: Online 🟢")