import streamlit as st
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
    os.system(f"ping {site}")

  time.sleep(3600)
