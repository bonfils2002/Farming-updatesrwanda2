import streamlit as st
from agri_bot import get_response

st.title("AgriBot Rwanda")
st.write(
    "Your AI assistant for farming advice in Rwanda. "
    "Ask about crops, seasons, livestock, and more!"
)

user_input = st.text_input("Ask AgriBot:")
if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
        st.write("**AgriBot:**", reply)
