import streamlit as st
import time

st.set_page_config(page_title="Uber Eats Offer Checker", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>Uber Eats Offer Checker</h1>", unsafe_allow_html=True)
st.markdown("Enter the details of the offer below to see if you should accept it.")

# CSS for larger font inputs
st.markdown("""
    <style>
        input[type=number] {
            font-size: 24px !important;
        }
        label {
            font-size: 20px !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Session state for countdown
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'triggered' not in st.session_state:
    st.session_state.triggered = False

# Function to calculate and show result
def evaluate_offer(miles, time_min, offer_amount):
    drive_hours = time_min / 60
    fuel_cost = miles * 0.09
    insurance_cost = drive_hours * 1.75
    total_cost = fuel_cost + insurance_cost
    target_profit = drive_hours * 15
    min_price = total_cost + target_profit

    st.markdown(f"### Minimum Acceptable Price: £{min_price:.2f}")

    if offer_amount >= min_price:
        st.success("ACCEPT – This offer meets your minimum requirements.")
    else:
        st.error("REJECT – This offer does not meet your minimum requirements.")

# Inputs
miles = st.number_input("Miles", min_value=0.1, step=0.1, key="miles")
time_min = st.number_input("Estimated Time (minutes)", min_value=1, step=1, key="time")
offer_amount = st.number_input("Offer Amount (£)", min_value=0.1, step=0.1, key="offer")

# Detect start of typing
if not st.session_state.start_time and (miles or time_min or offer_amount):
    st.session_state.start_time = time.time()

# Countdown logic
if st.session_state.start_time and not st.session_state.triggered:
    seconds_passed = time.time() - st.session_state.start_time
    remaining = 11 - int(seconds_passed)
    if remaining > 0:
        st.warning(f"⏳ Auto-checking in {remaining} seconds...")
        time.sleep(1)
        st.experimental_rerun()
    else:
        st.session_state.triggered = True
        st.experimental_rerun()

# After countdown & inputs filled
if st.session_state.triggered and all([miles, time_min, offer_amount]):
    evaluate_offer(miles, time_min, offer_amount)
