import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="centered"
)

# --------------------
# Header & Description
# --------------------
st.title("📊 Lauki Finance: Credit Risk Modelling")

st.markdown(
    """
    This app helps **assess credit risk** for loan applicants using 
    a machine learning model.  
    Provide customer and loan details below, and the model will predict:  
    - Default Probability  
    - Credit Score  
    - Risk Rating  

    ⚡ Designed to support better loan approval decisions.
    """
)

st.markdown("---")

# --------------------
# Input Form
# --------------------
with st.form("credit_risk_form"):
    st.subheader("Applicant & Loan Details")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Age', min_value=18, max_value=100, value=28)
        income = st.number_input('Annual Income (₹)', min_value=0, value=1200000)
        residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
        num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=10, value=2)

    with col2:
        loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)
        loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

    st.subheader("Credit Behavior")
    col3, col4, col5 = st.columns(3)
    with col3:
        avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)
    with col4:
        delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, value=30)
    with col5:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, value=30)

    # Loan-to-income ratio
    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    st.caption(f"💡 Loan-to-Income Ratio: **{loan_to_income_ratio:.2f}**")

    # Submit button
    submitted = st.form_submit_button("🔍 Calculate Risk")

# --------------------
# Prediction Output
# --------------------
if submitted:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("### 📊 Prediction Results")
    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("Default Probability", f"{probability:.2%}")
    with colB:
        st.metric("Credit Score", f"{credit_score}")
    with colC:
        st.metric("Risk Rating", rating)

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray; font-size:0.9em;'>Project developed as part of Lauki Finance ML initiative.</p>",
    unsafe_allow_html=True
)
