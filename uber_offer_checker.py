import streamlit as st

st.title("Uber Eats Offer Checker")

with st.form("offer_form"):
    miles_input = st.text_input("Miles")
    time_input = st.text_input("Estimated Time (minutes)")
    offer_input = st.text_input("Offer Amount (£)")

    submitted = st.form_submit_button("Check Offer")

if submitted:
    try:
        miles = float(miles_input)
        time = float(time_input)
        offer = float(offer_input)

        hourly = (offer / time) * 60
        st.markdown(f"**Net Hourly Rate:** £{hourly:.2f}")

        if hourly >= 15:
            st.success("Acceptable Offer")
        else:
            st.error("Below £15/hour")
    except:
        st.warning("Please enter valid numbers.")
