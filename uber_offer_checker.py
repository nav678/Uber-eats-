import streamlit as st
import time

# Settings
HOURLY_MINIMUM = 15.00  # £15/hour
COST_PER_MILE = 0.35    # £0.35/mile

st.set_page_config(page_title="Uber Eats Offer Checker", page_icon="🛵")

# Custom styles
st.markdown("""
    <style>
    .big-result {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }
    .timer {
        font-size: 28px;
        text-align: center;
        color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Uber Eats Offer Checker (15s Timer)")

# Inputs with empty defaults
miles = st.text_input("Miles")
time_minutes = st.text_input("Estimated Time (minutes)")
offer_amount = st.text_input("Offer Amount (£)")

if miles and time_minutes and offer_amount:
    try:
        m = float(miles)
        t = float(time_minutes)
        offer = float(offer_amount)

        # Countdown timer
        for i in range(15, 0, -1):
            st.markdown(f"<p class='timer'>Checking in {i} seconds...</p>", unsafe_allow_html=True)
            time.sleep(1)
            st.experimental_rerun()

        # Calculate minimum acceptable offer
        time_cost = (t / 60) * HOURLY_MINIMUM
        mileage_cost = m * COST_PER_MILE
        minimum_required = time_cost + mileage_cost

        if offer >= minimum_required:
            st.markdown('<p class="big-result" style="color: green;">ACCEPT</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="big-result" style="color: red;">REJECT</p>', unsafe_allow_html=True)
    except:
        st.warning("Please enter valid numbers.")
