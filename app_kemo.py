import streamlit as st
import math
from datetime import datetime, timedelta

st.title("💉 Kalkulator Kemoterapi")

# INPUT
bb = st.number_input("Berat Badan (kg)", 1.0)
tb = st.number_input("Tinggi Badan (cm)", 1.0)
tanggal_mulai = st.date_input("Tanggal Mulai")
jumlah_siklus = st.number_input("Jumlah Siklus", 1, 10, 6)
interval = st.number_input("Interval Hari", 1, 60, 21)

# HITUNG BSA
bsa = math.sqrt((bb * tb) / 3600)
st.write("BSA:", round(bsa,2))

# JADWAL
st.subheader("Jadwal Siklus")

tanggal = datetime.combine(tanggal_mulai, datetime.min.time())

for i in range(int(jumlah_siklus)):
    st.write(f"Siklus {i+1}: {tanggal.strftime('%Y-%m-%d')} ({tanggal.strftime('%A')})")
    tanggal += timedelta(days=interval)