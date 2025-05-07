import streamlit as st

‎# هزینه هدف و هر مایل
HOURLY_MINIMUM = 15.00     # £15/hour
COST_PER_MILE = 0.35       # £0.35/mile

st.set_page_config(page_title="Uber Eats Offer Checker", page_icon="🛵")
st.title("Uber Eats Offer Checker")
st.write("Enter the details of the offer below to see if you should accept it.")

# Inputs
miles = st.number_input("Miles", min_value=0.0, step=0.01)
time_minutes = st.number_input("Estimated Time (minutes)", min_value=0, step=1)
offer_amount = st.number_input("Offer Amount (£)", min_value=0.0, step=0.01)

# Decision logic
if st.button("Check Offer"):
    time_cost = (time_minutes / 60) * HOURLY_MINIMUM
    mileage_cost = miles * COST_PER_MILE
    minimum_required = time_cost + mileage_cost

    st.markdown(f"### Minimum Acceptable Price: £{minimum_required:.2f}")

    if offer_amount >= minimum_required:
        st.success("ACCEPT – This offer meets your minimum requirements.")
    else:
        st.error("REJECT – This offer does not meet your minimum requirements.")
