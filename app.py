import streamlit as st
import numpy as np

st.markdown("""
# UberEats Trip Profit Calculator
This app calculates your trip profit given different parameters, including  expected payout, trip
length, cost of gas, and your whip's MPG.
""")
st.subheader("\nauthor: Czar Yobero\nemail: cyobero@gmail.com")


gas_cost = st.number_input("What is the cost of gas?", min_value=0.01, value=5.)
mpg = st.number_input(
    "How many miles-per-gallon (MPG) does your car get?", min_value=0.01, value=26.4)
payout = st.number_input("What is the expected payout for this trip?",
                         min_value=0.1, value=2.5)
miles = st.slider("How long is this trip in miles?", min_value=0.01, max_value=30.0,
                  step=0.01, value=2.7)

cost_per_mile = gas_cost / mpg
profit = payout - (miles * cost_per_mile)
margin = (profit / payout)

st.markdown(f"""
    ### Profit for an expected \${payout} trip payout is \${profit.__round__(2)}.
    ### Margin (what you keep for every \$1 in profit): {margin.__round__(2)}\n
    #### Trip gas cost: \${(miles * cost_per_mile).__round__(2)}
    #### Revenue per mile: \${(payout/miles).__round__(2)}
    #### Cost per mile: \${cost_per_mile.__round__(2)}
""")
