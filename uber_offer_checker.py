import streamlit as st

# Fixed costs
HOURLY_MINIMUM = 15  # £15/hour target
COST_PER_MILE = 0.35  # £0.35 per mile

st.title("Uber Eats Offer Checker")
st.write("Enter the details of the offer below to see if you should accept it.")

# User inputs
miles = st.number_input("Miles", min_value=0.0, step=0.01)
time_minutes = st.number_input("Estimated Time (minutes)", min_value=0, step=1)
offer_amount = st.number_input("Offer Amount (£)", min_value=0.0, step=0.01)

if st.button("Check Offer"):
    # Calculate minimum acceptable price
    min_price = (time_minutes / 60) * HOURLY_MINIMUM + (miles * COST_PER_MILE)

    st.markdown(f"### Minimum Acceptable Price: £{min_price:.2f}")

    if offer_amount >= min_price:
        st.success("ACCEPT – This offer meets your minimum requirements.")
    else:
        st.error("REJECT – This offer does not meet your minimum requirements.")
