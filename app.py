
import streamlit as st

st.title("🤖 The Prompt Wrangler")
st.markdown("**LLM Prompt Tuning Tool for Clinical Note Extraction**")

# Input sections
system_prompt = st.text_area("🧠 System Prompt", height=150)
user_prompt = st.text_area("💬 User Prompt (with {{input_text}} placeholder)", height=150)
input_text = st.text_area("📄 Input Clinical Note", height=150)

# Model parameters
temperature = st.slider("🔥 Temperature", 0.0, 1.0, 0.7)
max_tokens = st.number_input("🔢 Max Tokens", min_value=100, max_value=2048, value=500)

# Display inputs for debug (optional)
st.subheader("🧪 Debug Output")
st.write("System Prompt:", system_prompt)
st.write("User Prompt:", user_prompt)
st.write("Input Text:", input_text)
st.write("Temperature:", temperature)
st.write("Max Tokens:", max_tokens)