
import streamlit as st

st.set_page_config(page_title="Uber Eats Offer Checker", page_icon="🛵")

st.title("Uber Eats Offer Checker")

st.markdown("Enter the details of the offer below to see if you should accept it.")

miles = st.number_input("Miles", min_value=0.0, step=0.1, format="%.2f")
minutes = st.number_input("Estimated Time (minutes)", min_value=0, step=1)
offer_amount = st.number_input("Offer Amount (£)", min_value=0.0, step=0.1, format="%.2f")

# Decision formula based on user's cost structure
min_required = 0.90 * miles + 0.11 * minutes

if st.button("Check Offer"):
    st.markdown(f"### Minimum Acceptable Price: £{min_required:.2f}")
    if offer_amount >= min_required:
        st.success("ACCEPT – This offer meets your minimum requirements.")
    else:
        st.error("REJECT – This offer does not meet your minimum requirements.")
