import streamlit as st

st.set_page_config(page_title="H-V1 Panel", layout="wide")

st.title("📊 H-V1 Süper Agent Paneli")
st.markdown("Bu panel, kripto piyasasını fetheden H-V1'in yönetim merkezidir. 💥")

col1, col2 = st.columns(2)

with col1:
    st.header("📈 Günlük Performans")
    st.metric(label="Günlük PnL", value="+2.35%", delta="+0.91%")
    st.metric(label="Haftalık PnL", value="+7.80%", delta="+1.24%")

with col2:
    st.header("🌍 Makro Risk Skoru")
    st.metric(label="Risk Seviyesi", value="2 / 4", delta="-1")

st.divider()

st.subheader("📌 Açık İşlemler")
st.table({
    "Coin": ["BTC", "ETH"],
    "Pozisyon": ["Long", "Short"],
    "Giriş": ["58,230", "3,098"],
    "TP1": ["59,800", "2,950"],
    "SL": ["57,000", "3,250"]
})

st.divider()

st.subheader("🧠 LM Öğrenme Günlüğü")
st.write("Son yanlış sinyal: ETH short sinyali erken geldi. CVD negatifti ama likidite desteği gelmişti. Model güncellendi.")
