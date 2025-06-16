import streamlit
import os
import time

sites = [
  "pingsite1.streamlit.app"
]

st.title("Streamlit Ping Site 2")
st.subheader("Sites to Ping:")

for site in sites:
  st.write(f" - {site}")

while True:
  for site in sites:
    os.terminal(f"ping {site}")
