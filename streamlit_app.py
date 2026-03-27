import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="GreenIQ", page_icon="🌱", layout="centered")

# Simple style
st.markdown("""
<style>
h1 { text-align: center; color: #2e7d32; }
</style>
""", unsafe_allow_html=True)

st.title("🌱 GreenIQ")
st.write("### Smart Energy Saver — تصميمك الخاص")

st.divider()

season = st.radio("🌦️ اختر الفصل", ["☀️ الصيف", "❄️ الشتاء"])

st.subheader("📊 ادخل استخدامك اليومي")
col1, col2, col3 = st.columns(3)
with col1:
    ac_hours = st.slider("❄️ مكيف", 0, 24, 6)
with col2:
    tv_hours = st.slider("📺 تلفزيون", 0, 24, 4)
with col3:
    pc_hours = st.slider("💻 كمبيوتر", 0, 24, 5)

if st.button("احسب 🔍"):
    if season == "☀️ الصيف":
        ac_power = 1.8
    else:
        ac_power = 0.5
    tv_power = 0.1
    pc_power = 0.2

    total = (ac_hours * ac_power) + (tv_hours * tv_power) + (pc_hours * pc_power)
    st.success(f"⚡ استهلاكك اليومي: {total:.2f} kWh")

    summer_total = (ac_hours * 1.8) + (tv_hours * tv_power) + (pc_hours * pc_power)
    winter_total = (ac_hours * 0.5) + (tv_hours * tv_power) + (pc_hours * pc_power)

    st.subheader("📊 مقارنة بين الفصول")
    st.write(f"☀️ الصيف: {summer_total:.2f} kWh")
    st.write(f"❄️ الشتاء: {winter_total:.2f} kWh")

    diff = summer_total - winter_total
    if diff > 0:
        st.warning(f"🔺 الاستهلاك في الصيف أكبر بـ {diff:.2f} kWh")
    else:
        st.success("✅ الاستهلاك متقارب")

    chart_data = pd.DataFrame({
        "Season": ["Summer", "Winter"],
        "Consumption": [summer_total, winter_total]
    })
    st.bar_chart(chart_data.set_index("Season"))

    st.divider()

    data = {
       "hours": [2, 4, 6, 8, 10, 12],
       "consumption": [3, 6, 9, 12, 15, 18]
    }
    df = pd.DataFrame(data)
    model = LinearRegression()
    model.fit(df[["hours"]], df["consumption"])

    total_hours = ac_hours + tv_hours + pc_hours
    prediction = model.predict([[total_hours]])
    st.subheader("🤖 التوقع الذكي")
    st.write(f"🔮 الاستهلاك المتوقع غداً: {prediction[0]:.2f} kWh")

    st.divider()
    st.subheader("💡 نصائح")
    if season == "☀️ الصيف" and ac_hours > 8:
        st.error("🚨 المكيف يستهلك طاقة عالية في الصيف!")
    if season == "❄️ الشتاء" and ac_hours > 5:
        st.warning("⚠️ استخدام المكيف ممكن تخفيضه في الشتاء")

    if total > 15:
        st.error("⚠️ استهلاكك عالي!")
    else:
        st.success("✅ استهلاكك ممتاز!")
    st.write("🌍 نحو بيئة أفضل")
