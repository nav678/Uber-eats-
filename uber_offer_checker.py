import streamlit as st

# Settings
HOURLY_MINIMUM = 15.00  # £15/hour
COST_PER_MILE = 0.35    # £0.35/mile

st.set_page_config(page_title="Uber Eats Checker", page_icon="🛵")
st.title("Uber Eats Offer Checker")

# User inputs (empty by default)
miles = st.text_input("Miles")
time_minutes = st.text_input("Estimated Time (minutes)")
offer_amount = st.text_input("Offer Amount (£)")

# Only run if all fields are filled
if miles and time_minutes and offer_amount:
    try:
        m = float(miles)
        t = float(time_minutes)
        offer = float(offer_amount)

        time_cost = (t / 60) * HOURLY_MINIMUM
        mileage_cost = m * COST_PER_MILE
        minimum_required = time_cost + mileage_cost

        if offer >= minimum_required:
            st.success("ACCEPT")
        else:
            st.error("REJECT")
    except:
        st.warning("Please enter valid numbers.") 
