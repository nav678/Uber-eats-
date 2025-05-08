import streamlit as st
import time

st.set_page_config(page_title="Uber Eats Offer Checker", layout="centered")

st.markdown("<h1 style='text-align: center;'>Uber Eats Offer Checker</h1>", unsafe_allow_html=True)

with st.form("offer_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        drive_time = st.number_input("Driving Time (minutes)", min_value=1, step=1, label_visibility="visible")
    with col2:
        miles = st.number_input("Miles", min_value=0.1, step=0.1, label_visibility="visible")

    col3, col4 = st.columns(2)
    with col3:
        fuel_cost = st.number_input("Fuel Cost (£/mile)", min_value=0.0, step=0.01, label_visibility="visible")
    with col4:
        insurance_hourly = st.number_input("Insurance (£/hour)", min_value=0.0, step=0.01, label_visibility="visible")

    offer_amount = st.number_input("Offer Amount (£)", min_value=0.01, step=0.01, label_visibility="visible")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown("### ⏳ Evaluating...")
    time.sleep(0.5)

    # Convert driving time to hours
    drive_hours = drive_time / 60

    # Calculate cost
    fuel_total = miles * fuel_cost
    insurance_total = insurance_hourly * drive_hours
    total_cost = fuel_total + insurance_total

    # Net profit and rate
    net_profit = offer_amount - total_cost
    net_per_hour = net_profit / drive_hours if drive_hours > 0 else 0

    # Result
    st.markdown("### ✅ Result:")
    st.write(f"**Net Profit:** £{net_profit:.2f}")
    st.write(f"**Net per Hour:** £{net_per_hour:.2f}")

    if net_per_hour >= 15:
        st.success("Great offer! Accept it.")
    else:
        st.error("Not worth it. Better to skip.")

    st.caption("Minimum target: £15/hour net profit")
