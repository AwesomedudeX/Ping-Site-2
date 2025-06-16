import streamlit as st
import os
import time

sites = [
  "pingsite1.streamlit.app"
]

def cmd(command):
  os.system(command)

cmd("apt-get update -y")
cmd("apt-get install -y iputils-ping")

st.title("Streamlit Ping Site 2")
st.subheader("Pinging Sites:")

for site in sites:
  st.write(f" - `{site}`")

while True:
  
  for site in sites:
    cmd(f"ping {site}")

  time.sleep(3600)
